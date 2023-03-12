def print_table(c_coord):  # Принт шахматной доски со всеми фигурами.
    print("   A B C D E F G H   ")
    for y in range(len(c_coord)):
        print(f"{8 - y}  ", end='')
        for x in range(len(c_coord[y])):
            print(c_coord[y][x], end=' ')
        print(f" {8 - y}")
    print("   A B C D E F G H   ")


def input_coordinates(c_coord):  # Ввод координат. Сохранение координат в двух видах.
    dct_let = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    dct_num = [1, 2, 3, 4, 5, 6, 7, 8]
    flag = True
    while flag:
        p_coord_hu = input("Введите координату перемещаемой фигуры вида 'буква число', слитно (пример: A1): ")
        if len(p_coord_hu) == 2 and p_coord_hu[0] in dct_let and int(p_coord_hu[1]) in dct_num:
            flag = not flag
        else:
            print("Введите правильную клетку.")
    flag = True
    while flag:
        p_move_coord_hu = input("Введите координату поля для перемещения вида 'буква число', слитно (пример: A1): ")
        if len(p_move_coord_hu) == 2 and p_move_coord_hu[0] in dct_let and int(p_move_coord_hu[1]) in dct_num:
            flag = not flag
        else:
            print("Введите правильную клетку.")
    p_coord = (8 - int(p_coord_hu[1]), dct_let[p_coord_hu[0]])
    p_move_coord = (8 - int(p_move_coord_hu[1]), dct_let[p_move_coord_hu[0]])
    p = c_coord[p_coord[0]][p_coord[1]]
    if p_move_coord != ".":
        t = "-"  # Ход без взятия фигуры.
    else:
        t = "x"  # Ход со взятием фигуры.
    return p, p_coord, t, p_move_coord, p_coord_hu, p_move_coord_hu
    # Возвращает фигуру, её координату, тип хода,координаты клетки для хода и другую фигню.


def proverka_check(c_coord, wking, bking):  # Проверка шаха и вскрытого шаха.
    if count % 2 == 0:
        xk = bking[1]  # Координаты короля (должны быть 2, добавить), ИСПРАВИТЬ!!
        yk = bking[0]  # Координаты короля (должны быть 2, добавить), ИСПРАВИТЬ!!
    elif count % 2 == 1:
        xk = wking[1]
        yk = wking[0]
    er_c = 0  # Фигнюшка для шаха.
    if count % 2 == 1:
        for i in range(8):
            if c_coord[i][xk] == "r" or c_coord[i][xk] == "q" and yk > i and er_c == 0:
                # Проверка вертикали. (король снизу)
                j = i + 1
                while c_coord[j][xk] == "." and j != yk:
                    j += 1
                if j == yk:
                    er_c = 1
            elif c_coord[i][xk] == "r" or c_coord[i][xk] == "q" and yk < i and er_c == 0:
                # Проверка вертикали. (король сверху)
                j = i - 1
                while c_coord[j][xk] == "." and j != yk:
                    j -= 1
                if j == yk:
                    er_c = 1
            if c_coord[yk][i] == "r" or c_coord[yk][i] == "q" and xk > i and er_c == 0:
                # Проверка горизонтали. (король справа)
                j = i + 1
                while c_coord[yk][j] == "." and j != xk:
                    j += 1
                if j == xk:
                    er_c = 1
            elif c_coord[yk][i] == "r" or c_coord[yk][i] == "q" and xk < i and er_c == 0:
                # Проверка горизонтали. (король слева)
                j = i - 1
                while c_coord[yk][j] == "." and j != xk:
                    j -= 1
                if j == xk:
                    er_c = 1
        if xk - yk >= 0:  # Проверка диагонали (сверху вниз) над большой белой диагональю.
            for i in range(8 - xk + yk):
                if (c_coord[i][xk - yk + i] == "b" or c_coord[i][xk - yk + i] == "q") and yk > i:
                    j = 1
                    while c_coord[i + j][xk - yk + i + j] == "." and xk - yk + i + j != xk:
                        j += 1
                    if xk - yk + i + j == xk:
                        er_c = 1
                if (c_coord[i][xk - yk + i] == "b" or c_coord[i][xk - yk + i] == "q") and yk < i:
                    j = 1
                    while c_coord[i - j][xk - yk + i - j] == "." and xk - yk + i - j != xk:
                        j += 1
                    if xk - yk + i - j == xk:
                        er_c = 1
        elif xk - yk < 0:  # Проверка диагонали (сверху вниз) под большой белой диагональю.
            for i in range(8 + xk - yk):
                if (c_coord[yk - xk + i][i] == "b" or c_coord[yk - xk + i][i] == "q") and yk > yk - xk + i:
                    j = 1
                    while c_coord[yk - xk + i + j][i + j] == "." and i + j != xk:
                        j += 1
                    if i + j == xk:
                        er_c = 1
                if (c_coord[yk - xk + i][i] == "b" or c_coord[yk - xk + i][i] == "q") and yk < yk - xk + i:
                    j = 1
                    while c_coord[yk - xk + i - j][i - j] == "." and i - j != xk:
                        j += 1
                    if i - j == xk:
                        er_c = 1
        if xk - 7 + yk >= 0:  # Проверка диагонали (снизу вверх) под большой чёрной диагональю.
            for i in range(15 - xk - yk):
                if (c_coord[xk + yk - 7 + i][7 - i] == "b" or c_coord[xk + yk - 7 + i][7 - i] == "q")\
                        and yk > xk + yk - 7 + i:
                    j = 1
                    while c_coord[xk + yk - 7 + i + j][7 - i - j] == "." and 7 - i - j != xk:
                        j += 1
                    if 7 - i - j == xk:
                        er_c = 1
                elif (c_coord[xk + yk - 7 + i][7 - i] == "b" or c_coord[xk + yk - 7 + i][7 - i] == "q")\
                        and yk < xk + yk - 7 + i:
                    j = 1
                    while c_coord[xk + yk - 7 + i - j][7 - i + j] == "." and 7 - i + j != xk:
                        j += 1
                    if 7 - i + j == xk:
                        er_c = 1
        elif xk - 7 + yk < 0:  # Проверка диагонали (снизу вверх) над большой чёрной диагональю.
            for i in range(xk + yk + 1):
                if (c_coord[i][xk + yk - i] == "b" or c_coord[i][xk + yk - i] == "q") and yk > i:
                    j = 1
                    while c_coord[i + j][xk + yk - i - j] == "." and xk + yk - i - j != xk:
                        j += 1
                    if xk + yk - i - j == xk:
                        er_c = 1
                elif (c_coord[i][xk + yk - i] == "b" or c_coord[i][xk + yk - i] == "q") and yk < i:
                    j = 1
                    while c_coord[i - j][xk + yk - i + j] == "." and xk + yk - i + j != xk:
                        j += 1
                    if xk + yk - i + j == xk:
                        er_c = 1
        if 0 <= yk - 2 <= 7 and 0 <= xk - 1 <= 7:
            if c_coord[yk - 2][xk - 1] == "n":
                er_c = 1
        if 0 <= yk - 2 <= 7 and 0 <= xk + 1 <= 7:
            if c_coord[yk - 2][xk + 1] == "n":
                er_c = 1
        if 0 <= yk - 1 <= 7 and 0 <= xk - 2 <= 7:
            if c_coord[yk - 1][xk - 2] == "n":
                er_c = 1
        if 0 <= yk - 1 <= 7 and 0 <= xk + 2 <= 7:
            if c_coord[yk - 1][xk + 2] == "n":
                er_c = 1
        if 0 <= yk + 1 <= 7 and 0 <= xk - 2 <= 7:
            if c_coord[yk + 1][xk - 2] == "n":
                er_c = 1
        if 0 <= yk + 1 <= 7 and 0 <= xk + 2 <= 7:
            if c_coord[yk + 1][xk + 2] == "n":
                er_c = 1
        if 0 <= yk + 2 <= 7 and 0 <= xk - 1 <= 7:
            if c_coord[yk + 2][xk - 1] == "n":
                er_c = 1
        if 0 <= yk + 2 <= 7 and 0 <= xk + 1 <= 7:
            if c_coord[yk + 2][xk + 1] == "n":
                er_c = 1
        if yk - 1 >= 1 and xk - 1 >= 0:
            if c_coord[yk - 1][xk - 1] == "p":
                er_c = 1
        if yk - 1 >= 1 and xk + 1 <= 7:
            if c_coord[yk - 1][xk + 1] == "p":
                er_c = 1
    elif count % 2 == 0:
        for i in range(8):
            if (c_coord[i][xk] == "R" or c_coord[i][xk] == "Q") and yk > i and er_c == 0:
                # Проверка вертикали. (король снизу)
                j = i + 1
                while c_coord[j][xk] == "." and j != yk:
                    j += 1
                if j == yk:
                    er_c = 1
            elif (c_coord[i][xk] == "R" or c_coord[i][xk] == "Q") and yk < i and er_c == 0:
                # Проверка вертикали. (король сверху)
                j = i - 1
                while c_coord[j][xk] == "." and j != yk:
                    j -= 1
                if j == yk:
                    er_c = 1
            if (c_coord[yk][i] == "R" or c_coord[yk][i] == "Q") and xk > i and er_c == 0:
                # Проверка горизонтали. (король справа)
                j = i + 1
                while c_coord[yk][j] == "." and j != xk:
                    j += 1
                if j == xk:
                    er_c = 1
            elif (c_coord[yk][i] == "R" or c_coord[yk][i] == "Q") and xk < i and er_c == 0:
                # Проверка горизонтали. (король слева)
                j = i - 1
                while c_coord[yk][j] == "." and j != xk:
                    j -= 1
                if j == xk:
                    er_c = 1
        if xk - yk >= 0:  # Проверка диагонали (сверху вниз) над большой белой диагональю.
            for i in range(8 - xk + yk):
                if (c_coord[i][xk - yk + i] == "B" or c_coord[i][xk - yk + i] == "Q") and yk > i:
                    j = 1
                    while c_coord[i + j][xk - yk + i + j] == "." and xk - yk + i + j != xk:
                        j += 1
                    if xk - yk + i + j == xk:
                        er_c = 1
                if (c_coord[i][xk - yk + i] == "B" or c_coord[i][xk - yk + i] == "Q") and yk < i:
                    j = 1
                    while c_coord[i - j][xk - yk + i - j] == "." and xk - yk + i - j != xk:
                        j += 1
                    if xk - yk + i - j == xk:
                        er_c = 1
        elif xk - yk < 0:  # Проверка диагонали (сверху вниз) под большой белой диагональю.
            for i in range(8 + xk - yk):
                if (c_coord[yk - xk + i][i] == "B" or c_coord[yk - xk + i][i] == "Q") and yk > yk - xk + i:
                    j = 1
                    while c_coord[yk - xk + i + j][i + j] == "." and i + j != xk:
                        j += 1
                    if i + j == xk:
                        er_c = 1
                if (c_coord[yk - xk + i][i] == "B" or c_coord[yk - xk + i][i] == "Q") and yk < yk - xk + i:
                    j = 1
                    while c_coord[yk - xk + i - j][i - j] == "." and i - j != xk:
                        j += 1
                    if i - j == xk:
                        er_c = 1
        if xk - 7 + yk >= 0:  # Проверка диагонали (снизу вверх) под большой чёрной диагональю.
            for i in range(15 - xk - yk):
                if (c_coord[xk + yk - 7 + i][7 - i] == "B" or c_coord[xk + yk - 7 + i][7 - i] == "Q") and\
                        yk > xk + yk - 7 + i:
                    j = 1
                    while c_coord[xk + yk - 7 + i + j][7 - i - j] == "." and 7 - i - j != xk:
                        j += 1
                    if 7 - i - j == xk:
                        er_c = 1
                elif (c_coord[xk + yk - 7 + i][7 - i] == "B" or c_coord[xk + yk - 7 + i][7 - i] == "Q")\
                        and yk < xk + yk - 7 + i:
                    j = 1
                    while c_coord[xk + yk - 7 + i - j][7 - i + j] == "." and 7 - i + j != xk:
                        j += 1
                    if 7 - i + j == xk:
                        er_c = 1
        elif xk - 7 + yk < 0:  # Проверка диагонали (снизу вверх) над большой чёрной диагональю.
            for i in range(xk + yk + 1):
                if (c_coord[i][xk + yk - i] == "B" or c_coord[i][xk + yk - i] == "Q") and yk > i:
                    j = 1
                    while c_coord[i + j][xk + yk - i - j] == "." and xk + yk - i - j != xk:
                        j += 1
                    if xk + yk - i - j == xk:
                        er_c = 1
                elif (c_coord[i][xk + yk - i] == "B" or c_coord[i][xk + yk - i] == "Q") and yk < i:
                    j = 1
                    while c_coord[i - j][xk + yk - i + j] == "." and xk + yk - i + j != xk:
                        j += 1
                    if xk + yk - i + j == xk:
                        er_c = 1
        if 0 <= yk - 2 <= 7 and 0 <= xk - 1 <= 7:
            if c_coord[yk - 2][xk - 1] == "N":
                er_c = 1
        if 0 <= yk - 2 <= 7 and 0 <= xk + 1 <= 7:
            if c_coord[yk - 2][xk + 1] == "N":
                er_c = 1
        if 0 <= yk - 1 <= 7 and 0 <= xk - 2 <= 7:
            if c_coord[yk - 1][xk - 2] == "N":
                er_c = 1
        if 0 <= yk - 1 <= 7 and 0 <= xk + 2 <= 7:
            if c_coord[yk - 1][xk + 2] == "N":
                er_c = 1
        if 0 <= yk + 1 <= 7 and 0 <= xk - 2 <= 7:
            if c_coord[yk + 1][xk - 2] == "N":
                er_c = 1
        if 0 <= yk + 1 <= 7 and 0 <= xk + 2 <= 7:
            if c_coord[yk + 1][xk + 2] == "N":
                er_c = 1
        if 0 <= yk + 2 <= 7 and 0 <= xk - 1 <= 7:
            if c_coord[yk + 2][xk - 1] == "N":
                er_c = 1
        if 0 <= yk + 2 <= 7 and 0 <= xk + 1 <= 7:
            if c_coord[yk + 2][xk + 1] == "N":
                er_c = 1
        if yk + 1 >= 1 and xk - 1 >= 0:
            if c_coord[yk + 1][xk - 1] == "P":
                er_c = 1
        if yk + 1 >= 1 and xk + 1 <= 7:
            if c_coord[yk + 1][xk + 1] == "P":
                er_c = 1
    return bool(er_c)


def move_proverka(p, c_coord, p_coord, p_move_coord, count, records, wkt, bkt):  # Проверка легальности хода.
    x = p_coord[1]  # Координата движимой фигуры по Х.
    y = p_coord[0]  # Координата движимой фигуры по У.
    xm = p_move_coord[1]  # Координата целевой клетки по Х.
    ym = p_move_coord[0]  # Координата целевой клетки по У.
    flag = False  # Флаг хода, ход нелегален по дефолту.
    er_c = 0  # Вспомогательная проверка нелегальности хода.
    en_p = None
    f = True
    zamena = None
    rok = 0
    if count % 2 == 1 and p != p.lower() and (
            c_coord[ym][xm] == "." or c_coord[ym][xm] != "." and c_coord[ym][xm].lower() == c_coord[ym][xm]) or count %\
            2 == 0 and p == p.lower() and (
            c_coord[ym][xm] == "." or c_coord[ym][xm] != "." and c_coord[ym][xm].lower() != c_coord[ym][xm]):
        if p == "P":  # Условие хода белой пешки.
            if x - 1 >= 0:
                if c_coord[y][x - 1] == "p" and records[-1][0] == "p" and records[-1][2] == (y, x - 1) and ym == y - 1\
                        and xm == x - 1:
                    flag = not flag
                    en_p = (y, x - 1)
            if x + 1 <= 7:
                if c_coord[y][x + 1] == "p" and records[-1][0] == "p" and records[-1][2] == (y, x + 1) and ym == y - 1\
                        and xm == x + 1:
                    flag = not flag
                    en_p = (y, x + 1)
            if y == 6 and y - ym == 2 and c_coord[ym + 1][xm] == "." and c_coord[ym][xm] == ".":
                # Проверка на возможность двойного хода пешки.
                flag = not flag
            elif y - ym == 1 and (x == xm and c_coord[ym][xm] == "." or (abs(x - xm) == 1 and c_coord[ym][xm] != ".")):
                # Проверка на возможность обычного хода пешки и взятия фигуры пешкой.
                flag = not flag
            if ym == 0:
                while f:
                    zamena = input("Введите фигуру для превращения пешки. (R, N, B, Q)")
                    if zamena in ["R", "N", "B", "Q"]:
                        f = not f
                    else:
                        print("Введена неверная фигура.")
        elif p == "p":  # Условие хода чёрной пешки.
            if x - 1 >= 0:
                if c_coord[y][x - 1] == "P" and records[-1][0] == "P" and records[-1][2] == (y, x - 1) and ym == y + 1\
                        and xm == x - 1:
                    flag = not flag
                    en_p = (y, x - 1)
            if x + 1 <= 7:
                if c_coord[y][x + 1] == "P" and records[-1][0] == "P" and records[-1][2] == (y, x + 1) and ym == y + 1\
                        and xm == x + 1:
                    flag = not flag
                    en_p = (y, x + 1)
            if y == 1 and ym - y == 2 and c_coord[ym - 1][xm] == "." and c_coord[ym][xm] == ".":
                # Проверка на возможность двойного хода пешки.
                flag = not flag
            elif ym - y == 1 and (x == xm and c_coord[ym][xm] == "." or (abs(x - xm) == 1 and c_coord[ym][xm] != ".")):
                # Проверка на возможность обычного хода пешки и взятия фигуры пешкой.
                flag = not flag
            if ym == 7:
                while f:
                    zamena = input("Введите фигуру для превращения пешки. (r, n, b, q)")
                    if zamena in ["r", "n", "b", "q"]:
                        f = not f
                    else:
                        print("Введена неверная фигура.")
        elif p.lower() == "r":  # Условие хода ладьи.
            if y == ym and x < xm:  # Ход вправо.
                for i in range(1, abs(xm - x)):
                    if c_coord[y][xm - i] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
            elif y == ym and x > xm:  # Ход влево.
                for i in range(1, abs(xm - x)):
                    if c_coord[y][xm + i] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
            elif x == xm and y < ym:  # Ход вниз.
                for i in range(1, abs(ym - y)):
                    if c_coord[ym - i][x] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
            elif x == xm and y > ym:  # Ход вверх.
                for i in range(1, abs(ym - y)):
                    if c_coord[ym + i][x] != ".":
                        er_c = 1
                if er_c == 0:
                    flag = not flag
        elif p.lower() == "n":  # Условие хода коня.
            if abs(x - xm) == 1 and abs(y - ym) == 2 or abs(x - xm) == 2 and abs(y - ym) == 1:
                flag = not flag
        elif p.lower() == "b":  # Условие хода слона.
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
        elif p.lower() == "q":  # Условие хода ферзя. (сложение условий ладьи и слона)
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
        elif p == "K":  # Условие хода короля.
            if wkt == 0 and ym == y and xm == x + 2 and c_coord[y][x + 1] == "." and c_coord[y][x + 2] == "." and\
                    c_coord[y][x + 3] == "R":
                flag = not flag
                rok = 1
            elif wkt == 0 and ym == y and xm == x - 3 and c_coord[y][x - 1] == "." and c_coord[y][x - 2] == "." and\
                    c_coord[y][x - 3] == "." and c_coord[y][x - 4] == "R":
                flag = not flag
                rok = 2
            elif abs(x - xm) <= 1 and abs(y - ym) <= 1:
                flag = not flag
        elif p == "k":  # Условие хода короля.
            if bkt == 0 and ym == y and xm == x + 2 and c_coord[y][x + 1] == "." and c_coord[y][x + 2] == "." and\
                    c_coord[y][x + 3] == "r":
                flag = not flag
                rok = 1
            elif bkt == 0 and ym == y and xm == x - 3 and c_coord[y][x - 1] == "." and c_coord[y][x - 2] == "." and\
                    c_coord[y][x - 3] == "." and c_coord[y][x - 4] == "r":
                flag = not flag
                rok = 2
            elif abs(x - xm) <= 1 and abs(y - ym) <= 1:
                flag = not flag
    return flag, en_p, zamena, rok


def move(c_coord, p_coord, p_move_coord, en_p, zamena, wking, bking, wkt, bkt, rok):
    # Функция хода фигуры. Без # проверки на легальность.
    if c_coord[p_coord[0]][p_coord[1]] == "K":
        wking = (p_move_coord[0], p_move_coord[1])
        wkt = 1
        if rok == 1:
            c_coord[p_move_coord[0]][p_move_coord[1]] = "K"
            c_coord[p_move_coord[0]][p_move_coord[1] - 1] = "R"
            c_coord[p_coord[0]][p_coord[1]] = "."
            c_coord[7][7] = "."
        elif rok == 2:
            c_coord[p_move_coord[0]][p_move_coord[1]] = "K"
            c_coord[p_move_coord[0]][p_move_coord[1] + 1] = "R"
            c_coord[p_coord[0]][p_coord[1]] = "."
            c_coord[7][0] = "."
    elif c_coord[p_coord[0]][p_coord[1]] == "k":
        bking = (p_move_coord[0], p_move_coord[1])
        bkt = 1
        if rok == 1:
            c_coord[p_move_coord[0]][p_move_coord[1]] = "k"
            c_coord[p_move_coord[0]][p_move_coord[1] - 1] = "r"
            c_coord[p_coord[0]][p_coord[1]] = "."
            c_coord[0][7] = "."
        elif rok == 2:
            c_coord[p_move_coord[0]][p_move_coord[1]] = "k"
            c_coord[p_move_coord[0]][p_move_coord[1] + 1] = "r"
            c_coord[p_coord[0]][p_coord[1]] = "."
            c_coord[0][0] = "."
    if zamena != None:
        c_coord[p_move_coord[0]][p_move_coord[1]] = zamena
        c_coord[p_coord[0]][p_coord[1]] = "."
    elif en_p != None:
        c_coord[p_move_coord[0]][p_move_coord[1]] = c_coord[p_coord[0]][p_coord[1]]
        c_coord[en_p[0]][en_p[1]] = "."
        c_coord[p_coord[0]][p_coord[1]] = "."
    elif en_p == None and rok != 1:
        c_coord[p_move_coord[0]][p_move_coord[1]] = c_coord[p_coord[0]][p_coord[1]]
        c_coord[p_coord[0]][p_coord[1]] = "."
    return c_coord, wking, bking, wkt, bkt


def move_sim(c_coord, p_coord, p_move_coord):  # Симуляция хода для проверки шаха после следующего хода.
    c_cl_coord = [x.copy() for x in c_coord]
    c_cl_coord[p_move_coord[0]][p_move_coord[1]] = c_cl_coord[p_coord[0]][p_coord[1]]
    c_cl_coord[p_coord[0]][p_coord[1]] = "."
    return c_cl_coord


def turn_record(p, records_hu, records, p_coord_hu, t, p_move_coord_hu, p_coord, p_move_coord):  # Запись партии.
    records_hu.append([p, p_coord_hu, t, p_move_coord_hu])
    records.append([p, p_coord, p_move_coord])
    return records, records_hu


turn_records = []
turn_records_hu = []
wkt = 0
bkt = 0
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
wking_coord = (7, 4)
bking_coord = (0, 4)
wking_turns = 0
bking_turns = 0

flag = True
count = 1

while flag:
    if proverka_check(coordinates, wking_coord, bking_coord):
        print("Вам шах.")
    piece, piece_coordinates, turn, piece_move_coordinates, piece_coordinates_hu, piece_move_coordinates_hu = \
        input_coordinates(coordinates)
    legal, en_passant, zamena, rok = move_proverka(piece, coordinates, piece_coordinates, piece_move_coordinates, count,
                                                   turn_records, wking_turns, bking_turns)
    if proverka_check(coordinates, wking_coord, bking_coord) and legal:
        print(move_sim(coordinates, piece_coordinates, piece_move_coordinates))
        if not proverka_check(move_sim(coordinates, piece_coordinates, piece_move_coordinates), wking_coord,
            bking_coord):
            coordinates, wking_coord, bking_coord, wking_turns, bking_turns = move(coordinates, piece_coordinates,
                piece_move_coordinates, en_passant, zamena, wking_coord, bking_coord, wking_turns, bking_turns, rok)
            count += 1
            turn_records, turn_records_hu = turn_record(piece, turn_records_hu, turn_records, piece_coordinates_hu,
                turn, piece_move_coordinates_hu, piece_coordinates, piece_move_coordinates)
        if proverka_check(move_sim(coordinates, piece_coordinates, piece_move_coordinates), wking_coord, bking_coord):
            print("Нелегальный ход.")
    elif not proverka_check(move_sim(coordinates, piece_coordinates, piece_move_coordinates), wking_coord, bking_coord)\
            and legal:
        coordinates, wking_coord, bking_coord, wking_turns, bking_turns = move(coordinates, piece_coordinates,
            piece_move_coordinates, en_passant, zamena, wking_coord, bking_coord, wking_turns, bking_turns, rok)
        count += 1
        turn_records, turn_records_hu = turn_record(piece, turn_records_hu, turn_records, piece_coordinates_hu, turn,
            piece_move_coordinates_hu, piece_coordinates, piece_move_coordinates)
    else:
        print("Нелегальный ход.")
    print_table(coordinates)