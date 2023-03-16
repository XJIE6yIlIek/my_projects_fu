class Chess:
    def __init__(self):
        c_coord = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p" for o in range(8)],
            ["." for o in range(8)],
            ["." for o in range(8)],
            ["." for o in range(8)],
            ["." for o in range(8)],
            ["P" for o in range(8)],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        self.c_coord = c_coord

    def print_table(self):
        print("   A B C D E F G H   ")
        for y in range(len(self.c_coord)):
            print(f"{8 - y}  ", end='')
            for x in range(len(self.c_coord[y])):
                print(self.c_coord[y][x], end=' ')
            print(f" {8 - y}")
        print("   A B C D E F G H   ")


class Piece:
    def __init__(self, ptype, team):
        self.ptype = ptype
        self.team = team

# class Pawn(Piece):
#     def move_check(self):
#
#
# class Knight(Piece):
#     def move_check(self):
#
# class Bishop(Piece):
#     def move_check(self):
#
# class Queen(Piece):
#     def move_check(self):
#
# class King(Piece):
#     def move_check(self):



chess = Chess()