play_tests = [

# code, list of moves to play, board representation, simple ko point

('blank', [
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .  .  .
3  .  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .  .
1  .  .  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", None, 0),

('twostone', [
('b', 1, 1),
('w', 1, 2),
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .  .  .
3  .  .  .  .  .  .  .  .  .
2  .  #  o  .  .  .  .  .  .
1  .  .  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", None, 0),

('many-groups-1-capture', [
('b', 2, 2),
('w', 2, 3),
('b', 4, 2),
('b', 3, 2),
('w', 3, 3),
('b', 0, 7),
('b', 8, 1),
('b', 5, 8),
('b', 6, 0),
('b', 6, 1),
('w', 2, 0),
('w', 1, 8),
('w', 1, 7),
('w', 1, 6),
('w', 2, 8),

('b', 6, 5),

('w', 5, 4),
('w', 7, 6),
('w', 5, 6),
('w', 7, 5),
('w', 6, 4),
('w', 5, 5),
('w', 6, 6),
('w', 7, 4),
], """\
9  .  #  .  .  .  .  .  .  .
8  .  .  .  .  o  o  o  .  .
7  #  #  .  .  o  .  o  .  .
6  .  .  .  .  o  o  o  .  #
5  .  .  #  .  .  .  .  .  .
4  .  .  #  o  .  .  .  .  .
3  o  .  #  o  .  .  .  .  o
2  .  .  .  .  .  .  o  o  o
1  .  .  .  .  .  .  .  #  .
   A  B  C  D  E  F  G  H  J
""", None, -8),

('corner-bl', [
('b', 0, 0),
('w', 0, 1),
('w', 1, 0),
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .  .  .
3  .  .  .  .  .  .  .  .  .
2  o  .  .  .  .  .  .  .  .
1  .  o  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", None, -81),

('corner-all', [
('b', 0, 0),
('w', 0, 1),
('w', 1, 0),

('b', 0, 8),
('w', 0, 7),
('w', 1, 8),

('b', 8, 0),
('w', 8, 1),
('w', 7, 0),

('b', 8, 8),
('w', 8, 7),
('w', 7, 8),

], """\
9  .  o  .  .  .  .  .  o  .
8  o  .  .  .  .  .  .  .  o
7  .  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .  .  .
3  .  .  .  .  .  .  .  .  .
2  o  .  .  .  .  .  .  .  o
1  .  o  .  .  .  .  .  o  .
   A  B  C  D  E  F  G  H  J
""", None, -81),

('multiple', [
('w', 3, 3),
('b', 2, 3),
('w', 4, 2),
('b', 3, 2),
('w', 4, 4),
('b', 3, 4),
('b', 4, 1),
('b', 4, 5),
('b', 5, 2),
('b', 5, 4),
('b', 6, 3),
('w', 5, 3),

('b', 4, 3),
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  #  .  .  .  .  .
6  .  .  #  .  #  .  .  .  .
5  .  #  .  #  .  #  .  .  .
4  .  .  #  .  #  .  .  .  .
3  .  .  .  #  .  .  .  .  .
2  .  .  .  .  .  .  .  .  .
1  .  .  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", None, 81),

('large', [
('w', 1, 3),
('w', 1, 6),
('w', 2, 4),
('w', 2, 5),
('w', 3, 5),
('w', 4, 3),
('w', 4, 4),
('w', 4, 5),
('b', 1, 4),
('b', 1, 5),
('b', 2, 3),
('b', 2, 6),
('b', 3, 3),
('b', 3, 6),
('b', 4, 2),
('b', 4, 6),
('b', 5, 3),
('b', 5, 4),
('b', 5, 5),
('b', 3, 4),
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .
6  .  .  .  #  #  #  .  .  .
5  .  .  #  .  .  .  #  .  .
4  .  .  .  #  #  .  #  .  .
3  .  .  .  #  .  .  #  .  .
2  .  .  .  o  #  #  o  .  .
1  .  .  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", None, 16),

('pre-recapture', [
('w', 0, 0),
('w', 0, 1),
('w', 1, 1),
('w', 1, 2),
('w', 2, 3),
('w', 2, 4),
('w', 3, 0),
('w', 3, 1),
('w', 3, 2),
('w', 3, 4),
('b', 1, 0),
('b', 1, 3),
('b', 1, 4),
('b', 2, 0),
('b', 2, 1),
('b', 2, 5),
('b', 3, 3),
('b', 3, 5),
('b', 4, 4),

('b', 2, 2),
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .  .
5  .  .  .  .  #  .  .  .  .
4  o  o  o  #  .  #  .  .  .
3  #  #  #  .  .  #  .  .  .
2  #  o  o  #  #  .  .  .  .
1  o  o  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", None, 6),

('recapture', [
('w', 0, 0),
('w', 0, 1),
('w', 1, 1),
('w', 1, 2),
('w', 2, 3),
('w', 2, 4),
('w', 3, 0),
('w', 3, 1),
('w', 3, 2),
('w', 3, 4),
('b', 1, 0),
('b', 1, 3),
('b', 1, 4),
('b', 2, 0),
('b', 2, 1),
('b', 2, 5),
('b', 3, 3),
('b', 3, 5),
('b', 4, 4),

('b', 2, 2),
('w', 2, 3),
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .  .
5  .  .  .  .  #  .  .  .  .
4  o  o  o  #  .  #  .  .  .
3  .  .  .  o  .  #  .  .  .
2  .  o  o  #  #  .  .  .  .
1  o  o  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", None, -6),

('self-capture-1', [
('b', 3, 3),
('b', 4, 2),
('b', 4, 4),
('b', 5, 3),
('w', 4, 3),
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .
6  .  .  .  #  .  .  .  .  .
5  .  .  #  .  #  .  .  .  .
4  .  .  .  #  .  .  .  .  .
3  .  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .  .
1  .  .  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", None, 81),

('self-capture-2', [
('b', 3, 3),
('b', 3, 4),
('b', 4, 2),
('b', 4, 5),
('b', 5, 3),
('b', 5, 4),
('w', 4, 3),
('w', 4, 4),
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .
6  .  .  .  #  #  .  .  .  .
5  .  .  #  .  .  #  .  .  .
4  .  .  .  #  #  .  .  .  .
3  .  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .  .
1  .  .  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", None, 81),

('self-capture-3', [
('b', 3, 3),
('b', 3, 4),
('b', 3, 5),
('b', 4, 2),
('b', 4, 6),
('b', 5, 3),
('b', 5, 4),
('b', 5, 5),
('w', 4, 3),
('w', 4, 5),
('w', 4, 4),
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .
6  .  .  .  #  #  #  .  .  .
5  .  .  #  .  .  .  #  .  .
4  .  .  .  #  #  #  .  .  .
3  .  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .  .
1  .  .  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", None, 81),

('self-capture-many', [
('b', 1, 4),
('b', 2, 3),
('b', 2, 5),
('b', 3, 3),
('b', 3, 5),
('b', 3, 6),
('b', 4, 2),
('b', 4, 7),
('b', 5, 2),
('b', 5, 5),
('b', 5, 6),
('b', 6, 3),
('b', 6, 4),
('w', 2, 4),
('w', 3, 4),
('w', 4, 3),
('w', 4, 5),
('w', 4, 6),
('w', 5, 3),
('w', 5, 4),
('w', 4, 4),
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  #  #  .  .  .  .
6  .  .  #  .  .  #  #  .  .
5  .  .  #  .  .  .  .  #  .
4  .  .  .  #  .  #  #  .  .
3  .  .  .  #  .  #  .  .  .
2  .  .  .  .  #  .  .  .  .
1  .  .  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", None, 81),

('ko-corner', [
('b', 0, 0),
('b', 1, 1),
('b', 2, 0),
('w', 0, 1),
('w', 1, 0),
], """\
9  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .  .  .
3  #  .  .  .  .  .  .  .  .
2  o  #  .  .  .  .  .  .  .
1  .  o  .  .  .  .  .  .  .
   A  B  C  D  E  F  G  H  J
""", 'A1', -1),

]

