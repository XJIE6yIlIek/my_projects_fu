def print_table(c_coord):
    print("   A B C D E F G H   ")
    for y in range(len(c_coord)):
        print(f"{8 - y}  ", end='')
        for x in range(len(c_coord[y])):
            print(c_coord[y][x], end=' ')
        print(f" {8 - y}")
    print("   A B C D E F G H   ")


def input_coordinates(c_coord):
    dct_coord = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
    p_coord_hu = input("Введите координату перемещаемой фигуры вида 'буква число', слитно (пример: A1): ")
    p_coord_lst = list(p_coord_hu)
    p_coord = (dct_coord[p_coord_lst[0]] - 1, 8 - int(p_coord_lst[1]))[::-1]
    p_move_coord_hu = input("Введите координату поля для перемещения вида 'буква число', слитно (пример: A1): ")
    p_move_coord_lst = list(p_move_coord_hu)
    p_move_coord = (dct_coord[p_move_coord_lst[0]] - 1, 8 - int(p_move_coord_lst[1]))[::-1]
    p = c_coord[p_coord[0]][p_coord[1]]
    if p_move_coord != ".":
        t = "-" # Ход без взятия фигуры.
    else:
        t = "x" # Ход со взятием фигуры.
    return p, p_coord, t, p_move_coord, p_coord_hu, p_move_coord_hu # Возвращает фигуру, её координату, тип хода,
    # координаты клетки для хода и другую фигню.


def move_proverka(p, c_coord, p_coord, p_move_coord):
    x = p_coord[1]
    y = p_coord[0]
    xm = p_move_coord[1]
    ym = p_move_coord[0]
    flag = False
    er_c = 0
    if p == "P":
        if y == 6 and y - ym == 2 and c_coord[ym + 1][xm] != "." and c_coord[ym][xm] != ".":
            flag = not flag
        elif y - ym == 1 and (x == xm and c_coord[ym][xm] == "." or (abs(x - xm) == 1 and c_coord[ym][xm] != ".")):
            flag = not flag
    elif p == "p":
        if y == 1 and ym - y == 2 and c_coord[ym - 1][xm] != "." and c_coord[ym][xm] != ".":
            flag = not flag
        elif ym - y == 1 and (x == xm and c_coord[ym][xm] == "." or (abs(x - xm) == 1 and c_coord[ym][xm] != ".")):
            flag = not flag
    elif p.lower() == "r":
        if y == ym and x < xm:
            for i in range(1, abs(xm - x) - 1):
                if c_coord[y][xm - i] != ".":
                    er_c = 1
        elif y == ym and x > xm:
            for i in range(1, abs(xm - x) - 1):
                if c_coord[y][x - i] != ".":
                    er_c = 1
        elif x == xm and y < ym:
            for i in range(abs(ym - y) - 1):
                if c_coord[ym - i][x] != ".":
                    er_c = 1
        elif x == xm and y > ym:
            for i in range(abs(ym - y) - 1):
                if c_coord[y - i][x] != ".":
                    er_c = 1
        if er_c == 0:
            flag = not flag
    elif p.lower() == "n":

    elif p.lower() == "b":

    elif p.lower() == "q":

    elif p.lower() == "k":



def move(c_coord, p_coord, p_move_coord):
    c_coord[p_move_coord[0]][p_move_coord[1]] = c_coord[p_coord[0]][p_coord[1]]
    c_coord[p_coord[0]][p_coord[1]] = "."
    return c_coord


def turn_record(p, records, p_coord_hu, t, p_move_coord_hu):
    dct_coord = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "F", "7": "G", "8": "H"}
    records.append([p, p_coord_hu, t, p_move_coord_hu])
    return records


turn_records = []
coordinates = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p" for o in range(8)],
    ["." for o in range(8)],
    ["." for o in range(8)],
    ["." for o in range(8)],
    ["." for o in range(8)],
    ["P" for o in range(8)],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]


piece, piece_coordinates, turn, piece_move_coordinates, piece_coordinates_hu, piece_move_coordinates_hu =\
    input_coordinates(coordinates)
move(coordinates, piece_coordinates, piece_move_coordinates)
turn_records = turn_record(piece, turn_records, piece_coordinates_hu, turn, piece_move_coordinates_hu)
print_table(coordinates)

print(turn_records)