import random

X = 'X'
O = '0'
board_size = 100
steps = ' '
NICHYA = 'Ничья'
ROW_COUNT = 10
COLUMN_COUNT = 10


def description():
    print('''
Привет! Это "Обратные Крестики-нолики".
Для того, чтобы сделать ход, нужно выбрать и ввести номер нужного поля:

 0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9
10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 
20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29
30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39
40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49
50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59
60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69
70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79
10 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89
90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99


''')


def start(qestion):
    answer = None
    while answer not in ('да', 'нет'):
        answer = input(qestion).lower()
    return answer


def who_x_0():
    first_step = start("Хотите ходить первым? \
(да/нет)?  ")
    if first_step == 'да':
        print('Твой ход. Ставь крестики')
        human = X
        comp = O
    else:
        print('Ход компьютера')
        human = O
        comp = X
    return comp, human


def number_steps(low, high):
    answer = None
    while answer not in range(low, high):
        answer = int(input("Делай свой ход - введи номер поля (0-99): "))
    return answer


def new_board():
    board = []
    for i in range(board_size):
        board.append(steps)
    return board


def show_board(board):
    print('\n', board[0], '|', board[1], '|', board[2], '|', board[3], '|', board[4], '|', board[5], '|', board[6], '|',
          board[7], '|', board[8], '|', board[9])
    print('----------------------------------------')
    print('\n', board[10], '|', board[11], '|', board[12], '|', board[13], '|', board[14], '|', board[15], '|',
          board[16], '|', board[17], '|', board[18], '|', board[19])
    print('----------------------------------------')
    print('\n', board[20], '|', board[21], '|', board[22], '|', board[23], '|', board[24], '|', board[25], '|',
          board[26], '|', board[27], '|', board[28], '|', board[29])
    print('----------------------------------------')
    print('\n', board[30], '|', board[31], '|', board[32], '|', board[33], '|', board[34], '|', board[35], '|',
          board[36], '|', board[37], '|', board[38], '|', board[39])
    print('----------------------------------------')
    print('\n', board[40], '|', board[41], '|', board[42], '|', board[43], '|', board[44], '|', board[45], '|',
          board[46], '|', board[47], '|', board[48], '|', board[49])
    print('----------------------------------------')
    print('\n', board[50], '|', board[51], '|', board[52], '|', board[53], '|', board[54], '|', board[55], '|',
          board[56], '|', board[57], '|', board[58], '|', board[59])
    print('----------------------------------------')
    print('\n', board[60], '|', board[61], '|', board[62], '|', board[63], '|', board[64], '|', board[65], '|',
          board[66], '|', board[67], '|', board[68], '|', board[69])
    print('----------------------------------------')
    print('\n', board[70], '|', board[71], '|', board[72], '|', board[73], '|', board[74], '|', board[75], '|',
          board[76], '|', board[77], '|', board[78], '|', board[79])
    print('----------------------------------------')
    print('\n', board[80], '|', board[81], '|', board[82], '|', board[83], '|', board[84], '|', board[85], '|',
          board[86], '|', board[87], '|', board[88], '|', board[89])
    print('----------------------------------------')
    print('\n', board[90], '|', board[91], '|', board[92], '|', board[93], '|', board[94], '|', board[95], '|',
          board[96], '|', board[97], '|', board[98], '|', board[99], '\n')


def free_moves(board):
    free_moves = []
    for i in range(board_size):
        if board[i] == steps:
            free_moves.append(i)
    return free_moves


def loss(board):
    VAR_LOSS = (tuple(range(5)), tuple(range(1, 6)), tuple(range(2, 7)), tuple(range(3, 8)), tuple(range(4, 9)),
                tuple(range(5, 10)),
                tuple(range(20, 26)), tuple(range(22, 27)), tuple(range(23, 28)), tuple(range(24, 29)),
                tuple(range(25, 30)),
                tuple(range(30, 36)), tuple(range(32, 37)), tuple(range(33, 38)), tuple(range(34, 39)),
                tuple(range(35, 40)),
                tuple(range(40, 46)), tuple(range(42, 47)), tuple(range(43, 48)), tuple(range(44, 49)),
                tuple(range(45, 50)),
                tuple(range(50, 56)), tuple(range(52, 57)), tuple(range(53, 58)), tuple(range(54, 59)),
                tuple(range(55, 60)),
                tuple(range(60, 66)), tuple(range(62, 67)), tuple(range(63, 68)), tuple(range(64, 69)),
                tuple(range(65, 70)),
                tuple(range(70, 76)), tuple(range(72, 77)), tuple(range(73, 78)), tuple(range(74, 79)),
                tuple(range(75, 80)),
                tuple(range(80, 86)), tuple(range(82, 87)), tuple(range(83, 88)), tuple(range(84, 89)),
                tuple(range(85, 90)),
                tuple(range(90, 96)), tuple(range(92, 97)), tuple(range(93, 98)), tuple(range(94, 99)),
                tuple(range(95, 100)),
                tuple(range(0, 50, 10)), tuple(range(10, 60, 10)), tuple(range(20, 70, 10)), tuple(range(30, 80, 10)),
                tuple(range(40, 90, 10)), tuple(range(50, 100, 10)),
                tuple(range(1, 50, 10)), tuple(range(11, 60, 10)), tuple(range(21, 70, 10)), tuple(range(31, 80, 10)),
                tuple(range(41, 90, 10)), tuple(range(51, 100, 10)),
                tuple(range(2, 50, 10)), tuple(range(12, 60, 10)), tuple(range(22, 70, 10)), tuple(range(32, 80, 10)),
                tuple(range(42, 90, 10)), tuple(range(52, 100, 10)),
                tuple(range(3, 50, 10)), tuple(range(13, 60, 10)), tuple(range(23, 70, 10)), tuple(range(33, 80, 10)),
                tuple(range(43, 90, 10)), tuple(range(53, 100, 10)),
                tuple(range(4, 50, 10)), tuple(range(14, 60, 10)), tuple(range(24, 70, 10)), tuple(range(34, 80, 10)),
                tuple(range(44, 90, 10)), tuple(range(54, 100, 10)),
                tuple(range(5, 50, 10)), tuple(range(15, 60, 10)), tuple(range(25, 70, 10)), tuple(range(35, 80, 10)),
                tuple(range(45, 90, 10)), tuple(range(55, 100, 10)),
                tuple(range(6, 50, 10)), tuple(range(16, 60, 10)), tuple(range(26, 70, 10)), tuple(range(36, 80, 10)),
                tuple(range(46, 90, 10)), tuple(range(56, 100, 10)),
                tuple(range(7, 50, 10)), tuple(range(17, 60, 10)), tuple(range(27, 70, 10)), tuple(range(37, 80, 10)),
                tuple(range(47, 90, 10)), tuple(range(57, 100, 10)),
                tuple(range(8, 50, 10)), tuple(range(18, 60, 10)), tuple(range(28, 70, 10)), tuple(range(38, 80, 10)),
                tuple(range(48, 90, 10)), tuple(range(58, 100, 10)),
                tuple(range(9, 50, 10)), tuple(range(19, 60, 10)), tuple(range(29, 70, 10)), tuple(range(39, 80, 10)),
                tuple(range(49, 90, 10)), tuple(range(59, 100, 10)),
                tuple(range(50, 100, 10 + 1)), tuple(range(40, 100, 10 + 1)), tuple(range(51, 100, 10 + 1)),
                tuple(range(30, 100, 10 + 1)), tuple(range(41, 100, 10 + 1)), tuple(range(52, 100, 10 + 1)),
                tuple(range(20, 100, 10 + 1)), tuple(range(31, 100, 10 + 1)), tuple(range(42, 100, 10 + 1)),
                tuple(range(53, 100, 10 + 1)), tuple(range(10, 100, 10 + 1)), tuple(range(21, 100, 10 + 1)),
                tuple(range(32, 100, 10 + 1)), tuple(range(43, 100, 10 + 1)), tuple(range(54, 100, 10 + 1)),
                tuple(range(0, 100, 10 + 1)), tuple(range(11, 100, 10 + 1)), tuple(range(22, 100, 10 + 1)),
                tuple(range(33, 100, 10 + 1)), tuple(range(44, 100, 10 + 1)), tuple(range(1, 100, 10 + 1)),
                tuple(range(12, 100, 10 + 1)), tuple(range(23, 100, 10 + 1)), tuple(range(34, 100, 10 + 1)),
                tuple(range(45, 100, 10 + 1)), tuple(range(2, 100, 10 + 1)), tuple(range(13, 100, 10 + 1)),
                tuple(range(24, 100, 10 + 1)), tuple(range(35, 100, 10 + 1)), tuple(range(3, 100, 10 + 1)),
                tuple(range(14, 100, 10 + 1)), tuple(range(25, 100, 10 + 1)), tuple(range(4, 100, 10 + 1)),
                tuple(range(15, 100, 10 + 1)), tuple(range(5, 100, 10 + 1)),
                tuple(range(59, 100, 10 - 1)), tuple(range(49, 100, 10 - 1)), tuple(range(58, 100, 10 - 1)),
                tuple(range(39, 100, 10 - 1)), tuple(range(48, 100, 10 - 1)), tuple(range(57, 100, 10 - 1)),
                tuple(range(29, 100, 10 - 1)), tuple(range(38, 100, 10 - 1)), tuple(range(47, 100, 10 - 1)),
                tuple(range(19, 100, 10 - 1)), tuple(range(28, 100, 10 - 1)), tuple(range(37, 100, 10 - 1)),
                tuple(range(46, 100, 10 - 1)), tuple(range(55, 100, 10 - 1)), tuple(range(9, 100, 10 - 1)),
                tuple(range(18, 100, 10 - 1)), tuple(range(27, 100, 10 - 1)), tuple(range(36, 100, 10 - 1)),
                tuple(range(45, 100, 10 - 1)), tuple(range(54, 100, 10 - 1)), tuple(range(8, 100, 10 - 1)),
                tuple(range(17, 100, 10 - 1)), tuple(range(26, 100, 10 - 1)), tuple(range(35, 100, 10 - 1)),
                tuple(range(44, 100, 10 - 1)), tuple(range(7, 100, 10 - 1)), tuple(range(16, 100, 10 - 1)),
                tuple(range(25, 100, 10 - 1)), tuple(range(34, 100, 10 - 1)), tuple(range(6, 100, 10 - 1)),
                tuple(range(15, 100, 10 - 1)), tuple(range(24, 100, 10 - 1)), tuple(range(5, 100, 10 - 1)),
                tuple(range(14, 100, 10 - 1)), tuple(range(4, 100, 10 - 1))
                )

    def func(var):
        for i in var:
            if board[i[0]] == board[i[1]] == board[i[2]] == board[i[3]] == board[i[4]] != steps:
                loss = board[i[0]]
                return loss
            if steps not in board:
                return NICHYA
        return None
    return func(VAR_LOSS)


def human_step(board, human):
    free = free_moves(board)
    step = None
    while step not in free:
        step = number_steps(0, board_size)
        if step not in free:
            print('Поле уже занято!!! ')
    return step


def comp_step(board, comp, human):
    board = board[:]
    print('Мой ход: ')
    for i in free_moves(board):
        i = random.randint(0, 99)
        return i
        board[i] = comp
        if winner(board) == comp:
            print(i)
            return i
        board[i] = steps
    for j in free_moves(board):
        board[j] = human
        if winner(board) == human:
            print(j)
            return j
        board[j] = steps
    for k in free_moves(doska):
        print(k)
        return k


def next_turn(queue):
    if queue == X:
        return O
    else:
        return X


def who_loss(loser, comp, human):
    if loser != NICHYA:
        print('Собрана линия ', loser)
    else:
        print(NICHYA)
    if loser == comp:
        print('Компьютер проиграл!')
    elif loser == human:
        print('Ты проиграл!')
    elif loser == NICHYA:
        print(NICHYA)


def main():
    description()
    human: str
    comp, human = who_x_0()
    queue = X
    board = new_board()
    show_board(board)
    while not loss(board):
        if queue == human:
            hod = human_step(board, human)
            board[hod] = human
        else:
            hod = comp_step(board, comp, human)
            board[hod] = comp
        show_board(board)
        queue = next_turn(queue)
    loser = loss(board)
    who_loss(loser, comp, human)


main()
