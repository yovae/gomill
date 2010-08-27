"""Organise processing jobs based around playing many GTP games."""

import os
import shlex
import sys

from gomill import game_jobs
from gomill import handicap_layout
from gomill import settings


def log_to_stdout(s):
    print s

def log_discard(s):
    pass

NoGameAvailable = object()

class CompetitionError(StandardError):
    """Error from competition code.

    Might be a bug in tuner code, or an error in a user-provided function.

    The ringmaster should display the error and terminate immediately.

    """

class Player_config(object):
    """Player description for use in tournament files."""
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class Matchup_config(object):
    """Matchup description for use in tournament files."""
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

control_file_globals = {
    'Player' : Player_config,
    'Matchup' : Matchup_config,
    }

def game_jobs_player_from_config(player_config):
    """Make a game_jobs.Player from a Player_config.

    Raises ValueError if there is an error in the configuration.

    Returns a game_jobs.Player with all required attributes set except 'code'.

    """
    args = player_config.args
    kwargs = player_config.kwargs
    player = game_jobs.Player()
    for key in kwargs:
        if key not in ('command_string', 'gtp_translations',
                       'startup_gtp_commands'):
            raise ValueError("unknown argument '%s'" % key)
    try:
        if len(args) > 1:
            raise ValueError("too many arguments")
        if len(args) == 1:
            if 'command_string' in kwargs:
                raise ValueError(
                    "command_string specified both implicitly and explicitly")
            command_string = args[0]
        else:
            command_string = kwargs['command_string']

        try:
            player.cmd_args = shlex.split(command_string)
            player.cmd_args[0] = os.path.expanduser(player.cmd_args[0])
        except ValueError, e:
            raise ValueError("%s in command_string" % e)

        player.startup_gtp_commands = []
        for s in kwargs.get('startup_gtp_commands', []):
            words = s.split()
            player.startup_gtp_commands.append((words[0], words[1:]))

        # FIXME: Ought to validate properly
        player.gtp_translations = kwargs.get('gtp_translations', {})

    except KeyError, e:
        raise ValueError("%s not specified" % e)
    return player

class Competition(object):
    """A resumable processing job based around playing many GTP games.

    This is an abstract base class.

    """
    def __init__(self, competition_code):
        self.competition_code = competition_code
        self.logger = log_to_stdout
        self.history_logger = log_discard

    def set_logger(self, logger):
        self.logger = logger

    def log(self, s):
        self.logger(s)

    def set_history_logger(self, logger):
        self.history_logger = logger

    def log_history(self, s):
        self.history_logger(s)

    # List of Settings, for overriding in subclasses.
    global_settings = []

    def initialise_from_control_file(self, config):
        """Initialise competition data from the control file.

        config -- namespace produced by the control file.

        (When resuming from saved state, this is called before set_state()).

        This processes all global_settings and sets attributes (named by the
        setting names).

        """
        try:
            # Not supporting defaults yet
            for setting in self.global_settings:
                v = config[setting.name]
                try:
                    v = setting.interpret(v)
                except ValueError, e:
                    raise ValueError("%s: %s" % (setting.name, e))
                setattr(self, setting.name, v)

            # ought to be Settings
            self.description = config['description']
            self.use_internal_scorer = False
            self.preferred_scorers = config.get('preferred_scorers')
            if 'scorer' in config:
                if config['scorer'] == "internal":
                    self.use_internal_scorer = True
                elif config['scorer'] != "players":
                    raise ValueError("invalid 'scorer' value")

            self.players = {}
            for player_code, player_config in config['players'].items():
                if not isinstance(player_config, Player_config):
                    raise ValueError("player %s is %r, not a Player" %
                                     (player_code, player_config))
                try:
                    player = game_jobs_player_from_config(player_config)
                except ValueError, e:
                    raise ValueError("player %s: %s" % (player_code, e))
                player.code = player_code
                self.players[player_code] = player

        except KeyError, e:
            raise ValueError("%s not specified" % e)

    def get_status(self):
        """Return full state of the competition, so it can be resumed later.

        The returned result must be serialisable using json. In addition, it can
        include Game_result objects.

        """
        raise NotImplementedError

    def set_status(self, status):
        """Reset competition state to previously a reported value.

        'status' will be a value previously reported by get_status().

        This is called for the 'show' command, so it mustn't log anything.

        """
        raise NotImplementedError

    def set_clean_status(self):
        """Reset competition state to its initial value.

        This is called before logging is set up, so it mustn't log anything.

        """
        raise NotImplementedError

    def get_game(self):
        """Return the details of the next game to play.

        Returns a game_jobs.Game_job, or NoGameAvailable

        (Doesn't set sgf_pathname: the ringmaster does that).

        """
        raise NotImplementedError

    def process_game_result(self, response):
        """Process the results from a completed game.

        response -- game_jobs.Game_job_result

        """
        raise NotImplementedError

    def process_game_error(self, job, previous_error_count):
        """Process a report that a job failed.

        job                  -- game_jobs.Game_job
        previous_error_count -- int >= 0

        Returns a pair (stop_competition, retry_game)

        The job is one previously returned by get_game(). previous_error_count
        is the number of times that this particular job has failed before.

        Failed jobs are ones in which there was an error more serious than one
        which just causes an engine to forfeit the game. For example, the job
        will fail if one of the engines fails to respond to GTP commands at all,
        or (in particular) if it exits as soon as it's invoked because it
        doesn't like its command-line options.

        (Competition provides a default implementation which will retry a game
         once and then stop the competition, leaving the game to be retried on
         the next run.)

        """
        if previous_error_count > 0:
            return (True, True)
        else:
            return (False, True)

    def write_static_description(self, out):
        """Write a description of the competition.

        out -- writeable file-like object

        This reports on 'static' data, rather than the game results.

        """
        raise NotImplementedError

    def write_status_summary(self, out):
        """Write a summary of current competition status.

        out -- writeable file-like object

        This reports on the game results, and shouldn't duplicate information
        from write_static_description().

        """
        raise NotImplementedError

    def write_results_report(self, out):
        """Write a detailed report of a completed competition.

        out -- writeable file-like object

        This reports on the game results, and shouldn't duplicate information
        from write_static_description() or write_status_summary().

        """
        raise NotImplementedError


## Helper functions for settings

def interpret_board_size(i):
    i = settings.interpret_int(i)
    if i < 2:
        raise ValueError("too small")
    if i > 25:
        raise ValueError("too large")
    return i

def validate_handicap(handicap, handicap_style, board_size):
    """Check whether a handicap is allowed.

    handicap       -- int or None
    handicap_style -- 'free' or 'fixed'
    board_size     -- int

    Raises ValueError with a description if it isn't.

    """
    if handicap is None:
        return True
    if handicap < 2:
        raise ValueError("handicap too small")
    if handicap_style == 'fixed':
        try:
            handicap_layout.handicap_points(handicap, board_size)
        except ValueError:
            raise ValueError("fixed handicap out of range for board size %d"
                             % board_size)
    else:
        if handicap > \
            handicap_layout.max_free_handicap_for_board_size(board_size):
            raise ValueError("free handicap too large for board size %d"
                             % board_size)
