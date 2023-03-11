def print_table(c_coord): # Принт шахматной доски со всеми фигурами.
    print("   A B C D E F G H   ")
    for y in range(len(c_coord)):
        print(f"{8 - y}  ", end='')
        for x in range(len(c_coord[y])):
            print(c_coord[y][x], end=' ')
        print(f" {8 - y}")
    print("   A B C D E F G H   ")


def input_coordinates(c_coord): # Ввод координат. Сохранение координат в двух видах.
    dct_coord = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
    p_coord_hu = input("Введите координату перемещаемой фигуры вида 'буква число', слитно (пример: A1): ")
    p_move_coord_hu = input("Введите координату поля для перемещения вида 'буква число', слитно (пример: A1): ")
    p_coord = (8 - int(p_coord_hu[1]), dct_coord[p_coord_hu[0]])
    p_move_coord = (8 - int(p_move_coord_hu[1]), dct_coord[p_move_coord_hu[0]])
    p = c_coord[p_coord[0]][p_coord[1]]
    if p_move_coord != ".":
        t = "-" # Ход без взятия фигуры.
    else:
        t = "x" # Ход со взятием фигуры.
    return p, p_coord, t, p_move_coord, p_coord_hu, p_move_coord_hu # Возвращает фигуру, её координату, тип хода,
    # координаты клетки для хода и другую фигню.


def proverka_check(c_coord, p_coord, p_move_coord): # Проверка шаха и вскрытого шаха. ПРОВЕРИТЬ НА РАБОТОСПОСОБНОСТЬ!!!
    xk = p_coord[1] # Координаты короля (должны быть 2, добавить), ИСПРАВИТЬ!!
    yk = p_coord[0] # Координаты короля (должны быть 2, добавить), ИСПРАВИТЬ!!
    xm = p_move_coord[1] # Координаты короля (должны быть 2, добавить), ИСПРАВИТЬ!!
    ym = p_move_coord[0] # Координаты короля (должны быть 2, добавить), ИСПРАВИТЬ!!
    er_c = 0 # Фигнюшка для шаха.
    if count % 2 == 1:
        for i in range(8):
            if c_coord[i][xk] == "r" or c_coord[i][xk] == "q" and yk > i and er_c == 0: #  Проверка вертикали. (король снизу)
                # for j in range(i + 1, yk):
                #     if c_coord[j][xk] != ".":
                #         er_c = 0
                #     else:
                #         er_c = 1
                j = i + 1
                while c_coord[j][xk] == "." and j != yk:
                    j += 1
                if j == yk:
                    er_c = 1
            elif c_coord[i][xk] == "r" or c_coord[i][xk] == "q" and yk < i and er_c == 0: #  Проверка вертикали. (король сверху)
                # for j in range(yk + 1, i):
                #     if c_coord[j][xk] != ".":
                #         er_c = 0
                #     else:
                #         er_c = 1
                j = i - 1
                while c_coord[j][xk] == "." and j != yk:
                    j -= 1
                if j == yk:
                    er_c = 1
            if c_coord[yk][i] == "r" or c_coord[yk][i] == "q" and xk > i and er_c == 0: #  Проверка горизонтали. (король справа)
                # for j in range(i + 1, xk):
                #     if c_coord[yk][j] != ".":
                #         er_c = 0
                #     else:
                #         er_c = 1
                j = i + 1
                while c_coord[yk][j] == "." and j != xk:
                    j += 1
                if j == xk:
                    er_c = 1
            elif c_coord[yk][i] == "r" or c_coord[yk][i] == "q" and xk < i and er_c == 0: #  Проверка горизонтали. (король слева)
                # for j in range(xk + 1, i):
                #     if c_coord[yk][j] != ".":
                #         er_c = 0
                #     else:
                #         er_c = 1
                j = i - 1
                while c_coord[yk][j] == "." and j != xk:
                    j -= 1
                if j == xk:
                    er_c = 1
        if xk - yk >= 0: #  Проверка диагонали (сверху вниз) над большой белой диагональю.
            # for i in range(8 - xk + yk):
            #     if c_coord[i][xk - yk + i] == "b" or c_coord[i][xk - yk + i] == "q" and yk > i:
            #         for j in range(1, yk - i):
            #             if c_coord[i + j][xk - yk + i + j] != ".":
            #                 er_c = 0
            #             else:
            #                 er_c = 1
            for i in range(8 - xk + yk):
                if c_coord[i][xk - yk + i] == "b" or c_coord[i][xk - yk + i] == "q" and yk > i:
                    j = i + 1
                    while c_coord[i + j][xk - yk + i + j] == "." and xk - yk + i + j != xk:
                        j += 1
                    if xk - yk + i + j == xk:
                        er_c = 1
                if c_coord[i][xk - yk + i] == "b" or c_coord[i][xk - yk + i] == "q" and yk < i:
                    j = i - 1
                    while c_coord[i - j][xk - yk + i - j] == "." and xk - yk + i - j != xk:
                        j += 1
                    if xk - yk + i - j == xk:
                        er_c = 1
        elif xk - yk < 0: #  Проверка диагонали (сверху вниз) под большой белой диагональю.
            # for i in range(xk - yk + 8):
            #     if (c_coord[i][yk - xk + i] == "b" or c_coord[i][yk - xk + i] == "q") and yk > i:
            #         for j in range(yk):
            #             if c_coord[j][yk - xk + j] != ".":
            #                 er_c = 0
            #             else:
            #                 er_c = 1
            #     if (c_coord[i][yk - xk + i] == "b" or c_coord[i][yk - xk + i] == "q") and yk < i:
            #         for j in range(1, 8 - yk):
            #             if c_coord[j][yk - xk + j] != ".":
            #                 er_c = 0
            #             else:
            #                 er_c = 1
        if xk - 7 + yk >= 0: #  Проверка диагонали (снизу вверх) под большой чёрной диагональю.
            for i in range(15 - xk - yk):
                if (c_coord[xk + yk - 7 + i][7 - i] == "b" or c_coord[xk + yk - 7 + i][7 - i] == "q") and yk > i:
                    j = i + 1
                    while c_coord[xk + yk - 7 + i + j][7 - i - j] == "." and 7 - i - j != xk:
                        j += 1
                    if 7 - i - j == xk:
                        er_c = 1
                elif (c_coord[xk + yk - 7 + i][7 - i] == "b" or c_coord[xk + yk - 7 + i][7 - i] == "q") and yk < i:
                    j = i - 1
                    while c_coord[xk + yk - 7 + i - j][7 - i + j] == "." and 7 - i + j != xk:
                        j += 1
                    if 7 - i + j == xk:
                        er_c = 1
        elif xk - 7 + yk < 0: #  Проверка диагонали (снизу вверх) над большой чёрной диагональю.
            for i in range(xk + yk + 1):
                if (c_coord[i][xk + yk - i] == "b" or c_coord[i][xk + yk - i] == "q") and yk > i:
                    j = i + 1
                    while c_coord[i + j][xk + yk - i - j] == "." and xk + yk - i - j != xk:
                        j += 1
                    if xk + yk - i - j == xk:
                        er_c = 1
                elif (c_coord[i][xk + yk - i] == "b" or c_coord[i][xk + yk - i] == "q") and yk < i:
                    j = i - 1
                    while c_coord[i - j][xk + yk - i + j] == "." and xk + yk - i + j != xk:
                        j += 1
                    if xk + yk - i + j == xk:
                        er_c = 1
    if count % 2 == 0:
        for i in range(8):
            if (c_coord[i][xk] == "R" or c_coord[i][xk] == "Q") and yk > i and er_c == 0: #  Проверка вертикали. (король снизу)
                # for j in range(i + 1, yk):
                #     if c_coord[j][xk] != ".":
                #         er_c = 0
                #     else:
                #         er_c = 1
                j = i + 1
                while c_coord[j][xk] == "." and j != yk:
                    j += 1
                if j == yk:
                    er_c = 1
            elif (c_coord[i][xk] == "R" or c_coord[i][xk] == "Q") and yk < i and er_c == 0: #  Проверка вертикали. (король сверху)
                # for j in range(yk + 1, i):
                #     if c_coord[j][xk] != ".":
                #         er_c = 0
                #     else:
                #         er_c = 1
                j = i - 1
                while c_coord[j][xk] == "." and j != yk:
                    j -= 1
                if j == yk:
                    er_c = 1
            if (c_coord[yk][i] == "R" or c_coord[yk][i] == "Q") and xk > i and er_c == 0: #  Проверка горизонтали. (король справа)
                # for j in range(i + 1, xk):
                #     if c_coord[yk][j] != ".":
                #         er_c = 0
                #     else:
                #         er_c = 1
                j = i + 1
                while c_coord[yk][j] == "." and j != xk:
                    j += 1
                if j == xk:
                    er_c = 1
            elif (c_coord[yk][i] == "R" or c_coord[yk][i] == "Q") and xk < i and er_c == 0: #  Проверка горизонтали. (король слева)
                # for j in range(xk + 1, i):
                #     if c_coord[yk][j] != ".":
                #         er_c = 0
                #     else:
                #         er_c = 1
                j = i - 1
                while c_coord[yk][j] == "." and j != xk:
                    j -= 1
                if j == xk:
                    er_c = 1
        if xk - yk >= 0: #  Проверка диагонали (сверху вниз) над большой белой диагональю.
            # for i in range(8 - xk + yk):
            #     if c_coord[i][xk - yk + i] == "b" or c_coord[i][xk - yk + i] == "q" and yk > i:
            #         for j in range(1, yk - i):
            #             if c_coord[i + j][xk - yk + i + j] != ".":
            #                 er_c = 0
            #             else:
            #                 er_c = 1
            for i in range(8 - xk + yk):
                if (c_coord[i][xk - yk + i] == "B" or c_coord[i][xk - yk + i] == "Q") and yk > i:
                    j = i + 1
                    while c_coord[i + j][xk - yk + i + j] == "." and xk - yk + i + j != xk:
                        j += 1
                    if xk - yk + i + j == xk:
                        er_c = 1
                if (c_coord[i][xk - yk + i] == "B" or c_coord[i][xk - yk + i] == "Q") and yk < i:
                    j = i - 1
                    while c_coord[i - j][xk - yk + i - j] == "." and xk - yk + i - j != xk:
                        j += 1
                    if xk - yk + i - j == xk:
                        er_c = 1
        elif xk - yk < 0: #  Проверка диагонали (сверху вниз) под большой белой диагональю.
            # for i in range(xk - yk + 8):
            #     if (c_coord[i][yk - xk + i] == "b" or c_coord[i][yk - xk + i] == "q") and yk > i:
            #         for j in range(yk):
            #             if c_coord[j][yk - xk + j] != ".":
            #                 er_c = 0
            #             else:
            #                 er_c = 1
            #     if (c_coord[i][yk - xk + i] == "b" or c_coord[i][yk - xk + i] == "q") and yk < i:
            #         for j in range(1, 8 - yk):
            #             if c_coord[j][yk - xk + j] != ".":
            #                 er_c = 0
            #             else:
            #                 er_c = 1
        if xk - 7 + yk >= 0: #  Проверка диагонали (снизу вверх) под большой чёрной диагональю.
            for i in range(15 - xk - yk):
                if (c_coord[xk + yk - 7 + i][7 - i] == "B" or c_coord[xk + yk - 7 + i][7 - i] == "Q") and yk > i:
                    j = i + 1
                    while c_coord[xk + yk - 7 + i + j][7 - i - j] == "." and 7 - i - j != xk:
                        j += 1
                    if 7 - i - j == xk:
                        er_c = 1
                elif (c_coord[xk + yk - 7 + i][7 - i] == "B" or c_coord[xk + yk - 7 + i][7 - i] == "Q") and yk < i:
                    j = i - 1
                    while c_coord[xk + yk - 7 + i - j][7 - i + j] == "." and 7 - i + j != xk:
                        j += 1
                    if 7 - i + j == xk:
                        er_c = 1
        elif xk - 7 + yk < 0: #  Проверка диагонали (снизу вверх) над большой чёрной диагональю.
            for i in range(xk + yk + 1):
                if (c_coord[i][xk + yk - i] == "B" or c_coord[i][xk + yk - i] == "Q") and yk > i:
                    j = i + 1
                    while c_coord[i + j][xk + yk - i - j] == "." and xk + yk - i - j != xk:
                        j += 1
                    if xk + yk - i - j == xk:
                        er_c = 1
                elif (c_coord[i][xk + yk - i] == "B" or c_coord[i][xk + yk - i] == "Q") and yk < i:
                    j = i - 1
                    while c_coord[i - j][xk + yk - i + j] == "." and xk + yk - i + j != xk:
                        j += 1
                    if xk + yk - i + j == xk:
                        er_c = 1
#  ОСТАЛОСЬ ДОПИСАТЬ ШАХ КОНЁМ, ПЕШКОЙ, НЕВОЗМОЖНОСТЬ ОБЪЯТИЙ КОРОЛЕЙ!!! А ещё проверить, работает ли это...чудо...


def move_proverka(p, c_coord, p_coord, p_move_coord, count): # Проверка легальности хода.
    x = p_coord[1] # Координата движимой фигуры по Х.
    y = p_coord[0] # Координата движимой фигуры по У.
    xm = p_move_coord[1] # Координата целевой клетки по Х.
    ym = p_move_coord[0] # Координата целевой клетки по У.
    flag = False # Флаг хода, ход нелегален по дефолту.
    er_c = 0 # Вспомогательная проверка нелегальности хода.
    if count % 2 == 1 and p != p.lower() and (c_coord[ym][xm] == "." or c_coord[ym][xm] != "." and c_coord[ym][xm].lower() == c_coord[ym][xm]) or count % 2 == 0 and p == p.lower() and (c_coord[ym][xm] == "." or c_coord[ym][xm] != "." and c_coord[ym][xm].lower() != c_coord[ym][xm]):
        if p == "P": # Условие хода белой пешки.
            if y == 6 and y - ym == 2 and c_coord[ym + 1][xm] == "." and c_coord[ym][xm] == ".": # Проверка на возможность двойного хода пешки.
                flag = not flag
            elif y - ym == 1 and (x == xm and c_coord[ym][xm] == "." or (abs(x - xm) == 1 and c_coord[ym][xm] != ".")): # Проверка на возможность обычного хода пешки и взятия фигуры пешкой.
                flag = not flag
        elif p == "p": # Условие хода чёрной пешки.
            if y == 1 and ym - y == 2 and c_coord[ym - 1][xm] == "." and c_coord[ym][xm] == ".": # Проверка на возможность двойного хода пешки.
                flag = not flag
            elif ym - y == 1 and (x == xm and c_coord[ym][xm] == "." or (abs(x - xm) == 1 and c_coord[ym][xm] != ".")): # Проверка на возможность обычного хода пешки и взятия фигуры пешкой.
                flag = not flag
        elif p.lower() == "r": # Условие хода ладьи.
            if y == ym and x < xm: # Ход вправо.
                for i in range(1, abs(xm - x)):
                    if c_coord[y][xm - i] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
            elif y == ym and x > xm: # Ход влево.
                for i in range(1, abs(xm - x)):
                    if c_coord[y][xm + i] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
            elif x == xm and y < ym: # Ход вниз.
                for i in range(1, abs(ym - y)):
                    if c_coord[ym - i][x] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
            elif x == xm and y > ym: # Ход вверх.
                for i in range(1, abs(ym - y)):
                    if c_coord[ym + i][x] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
        elif p.lower() == "n": # Условие хода коня.
            if abs(x - xm) == 1 and abs(y - ym) == 2 or abs(x - xm) == 2 and abs(y - ym) == 1:
                flag = not flag
        elif p.lower() == "b": # Условие хода слона.
            if abs(x - xm) == abs(y - ym):
                if y < ym and x > xm:
                    for i in range(1, abs(x - xm)):
                        if c_coord[ym - i][xm + i] != ".":
                            er_c = 1
                    if er_c == 0:
                        flag = not flag
                elif y < ym and x < xm:
                    for i in range(1, abs(x - xm)):
                        if c_coord[ym - i][xm - i] != ".":
                            er_c = 1
                    if er_c == 0:
                        flag = not flag
                elif y > ym and x > xm:
                    for i in range(1, abs(x - xm)):
                        if c_coord[ym + i][xm + i] != ".":
                            er_c = 1
                    if er_c == 0:
                        flag = not flag
                elif y > ym and x < xm:
                    for i in range(1, abs(x - xm)):
                        if c_coord[ym + i][xm - i] != ".":
                            er_c = 1
                    if er_c == 0:
                        flag = not flag
        elif p.lower() == "q": # Условие хода ферзя. (сложение условий ладьи и слона)
            if y == ym and x < xm:
                for i in range(1, abs(xm - x)):
                    if c_coord[y][xm - i] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
            elif y == ym and x > xm:
                for i in range(1, abs(xm - x)):
                    if c_coord[y][x - i] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
            elif x == xm and y < ym:
                for i in range(1, abs(ym - y)):
                    if c_coord[ym - i][x] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
            elif x == xm and y > ym:
                for i in range(1, abs(ym - y)):
                    if c_coord[y - i][x] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
            elif abs(x - xm) == abs(y - ym):
                if y < ym and x > xm:
                    for i in range(1, abs(x - xm)):
                        if c_coord[ym - i][xm + i] != ".":
                            er_c = 1
                    if er_c == 0:
                        flag = not flag
                elif y < ym and x < xm:
                    for i in range(1, abs(x - xm)):
                        if c_coord[ym - i][xm - i] != ".":
                            er_c = 1
                    if er_c == 0:
                        flag = not flag
                elif y > ym and x > xm:
                    for i in range(1, abs(x - xm)):
                        if c_coord[ym + i][xm + i] != ".":
                            er_c = 1
                    if er_c == 0:
                        flag = not flag
                elif y > ym and x < xm:
                    for i in range(1, abs(x - xm)):
                        if c_coord[ym + i][xm - i] != ".":
                            er_c = 1
                    if er_c == 0:
                        flag = not flag
        elif p.lower() == "k": # Условие хода короля.
            if abs(x - xm) <= 1 and abs(y - ym) <= 1:
                flag = not flag
    return flag


def move(c_coord, p_coord, p_move_coord): # Функция хода фигуры. Без проверки на легальность.
    c_coord[p_move_coord[0]][p_move_coord[1]] = c_coord[p_coord[0]][p_coord[1]]
    c_coord[p_coord[0]][p_coord[1]] = "."
    return c_coord


def turn_record(p, records, p_coord_hu, t, p_move_coord_hu): # Запись партии.
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

flag = True
count = 1
while flag:
    piece, piece_coordinates, turn, piece_move_coordinates, piece_coordinates_hu, piece_move_coordinates_hu = input_coordinates(coordinates)
    if move_proverka(piece, coordinates, piece_coordinates, piece_move_coordinates, count):
        move(coordinates, piece_coordinates, piece_move_coordinates)
        count += 1
    else:
        print("Нелегальный ход, переделывай, Стасян.")
    turn_records = turn_record(piece, turn_records, piece_coordinates_hu, turn, piece_move_coordinates_hu)
    print_table(coordinates)

print(turn_records)
# Я не знаю что я делаю.