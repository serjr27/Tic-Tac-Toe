# write your code here
cells = '         '
field = [[el for el in cells[i:i+3]] for i in range(0, 9, 3)]


def user_move(x_or_o: str):
    x, y = input("Enter the coordinates: ").split()
    if not x.isdigit() or not y.isdigit():
        print("You should enter numbers")
        user_move(x_or_o)
    elif not (0 < int(x) <= 3) or not (0 < int(y) <= 3):
        print("Coordinates should be from 1 to 3")
        user_move(x_or_o)
    elif field[3 - int(y)][int(x) - 1] == 'X' or field[3 - int(y)][int(x) - 1] == 'O':
        print("This cell occupied! Choose another one!")
        user_move(x_or_o)
    else:
        field[3-int(y)][int(x) - 1] = x_or_o
        show_field()


def show_field():
    print('-' * 9)
    str_ = '| '
    for i in range(3):
        for j in range(3):
            str_ += field[i][j] + ' '
        str_ += '|'
        print(str_)
        str_ = '| '
    print('-' * 9)


def count_elem(elem: str):
    count = 0
    for i in range(3):
        for j in range(3):
            if field[i][j] == elem:
                count += 1
    return count


def is_win_row(elem: str):
    for row in range(3):
        if elem == field[row][0] and elem == field[row][1] and elem == field[row][2]:
            return True
    return False


def is_win_col(elem: str):
    for col in range(3):
        if elem == field[0][col] and elem == field[1][col] and elem == field[2][col]:
            return True
    return False


def is_win_diagonal(elem: str):
    if (elem == field[0][0] and elem == field[1][1] and elem == field[2][2]) or \
         (elem == field[0][2] and elem == field[1][1] and elem == field[2][0]):
        return True
    return False


def analysis():
    if is_win_row('X') or is_win_col('X') or is_win_diagonal('X'):
        print('X wins')
        return True
    elif is_win_row('O') or is_win_col('O') or is_win_diagonal('O'):
        print('O wins')
        return True
    elif (count_elem('X') + count_elem('O')) == 9:
        print('Draw')
        return True
    else:
        return False


show_field()
x_move = True
while True:
    if x_move:
        user_move('X')
        x_move = False
    else:
        user_move('O')
        x_move = True
    if analysis():
        break
