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
-----------------------------------------------
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
-----------------------------------------------

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
        human = O
        comp = X
    return comp, human


def number_steps(low, high):
    descrip = 'Ты ввел не то, что нужно. Попробуй снова мэн)'
    answer = None
    while answer not in range(low, high):
        try:
            answer = int(input("Делай свой ход - введи номер поля (0-99): "))
            a = list(range(0, 99))
            for i in a:
                if answer > i:
                    print(descrip)
                    break
                elif answer < i:
                    print(descrip)
                    break
            continue
        except ValueError:
            print(descrip)
            continue







    return answer


def new_board():
    brd = []
    for i in range(board_size):
        brd.append(steps)
    return brd


def show_board(brd):
    print(f''' 
----------------------------------------------
 {brd[0]} |  {brd[1]} | {brd[2]} |  {brd[3]} |  {brd[4]} |  {brd[5]} |  {brd[6]} |  {brd[7]} |  {brd[8]} |  {brd[9]}
----------------------------------------------
 {brd[10]} |  {brd[11]} | {brd[12]} |  {brd[13]} |  {brd[14]} |  {brd[15]} |  {brd[16]} |  {brd[17]} |  {brd[18]} |  {brd[19]} 
----------------------------------------------
 {brd[20]} |  {brd[21]} | {brd[22]} |  {brd[23]} |  {brd[24]} |  {brd[25]} |  {brd[26]} |  {brd[27]} |  {brd[28]} |  {brd[29]}
----------------------------------------------
 {brd[30]} |  {brd[31]} | {brd[32]} |  {brd[33]} |  {brd[34]} |  {brd[35]} |  {brd[36]} |  {brd[37]} |  {brd[38]} |  {brd[39]}
----------------------------------------------
 {brd[40]} |  {brd[41]} | {brd[42]} |  {brd[43]} |  {brd[44]} |  {brd[45]} |  {brd[46]} |  {brd[47]} |  {brd[48]} |  {brd[49]}
----------------------------------------------
 {brd[50]} |  {brd[51]} | {brd[52]} |  {brd[53]} |  {brd[54]} |  {brd[55]} |  {brd[56]} |  {brd[57]} |  {brd[58]} |  {brd[59]}
----------------------------------------------
 {brd[60]} |  {brd[61]} | {brd[62]} |  {brd[63]} |  {brd[64]} |  {brd[65]} |  {brd[66]} |  {brd[67]} |  {brd[68]} |  {brd[69]}
----------------------------------------------
 {brd[70]} |  {brd[71]} | {brd[72]} |  {brd[73]} |  {brd[74]} |  {brd[75]} |  {brd[76]} |  {brd[77]} |  {brd[78]} |  {brd[79]}
----------------------------------------------
 {brd[80]} |  {brd[81]} | {brd[82]} |  {brd[83]} |  {brd[84]} |  {brd[85]} |  {brd[86]} |  {brd[87]} |  {brd[88]} |  {brd[89]}
----------------------------------------------
 {brd[90]} |  {brd[91]} | {brd[92]} |  {brd[93]} |  {brd[94]} |  {brd[95]} |  {brd[96]} |  {brd[97]} |  {brd[98]} |  {brd[99]}
----------------------------------------------

    ''')



def free_moves(brd):
    free_moves = []
    for i in range(board_size):
        if brd[i] == steps:
            free_moves.append(i)
    return free_moves


def loss(brd):
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
            if brd[i[0]] == brd[i[1]] == brd[i[2]] == brd[i[3]] == brd[i[4]] != steps:
                loss = brd[i[0]]
                return loss
            if steps not in brd:
                return NICHYA
        return None
    return func(VAR_LOSS)


def human_step(brd, human):
    free = free_moves(brd)
    step = None
    while step not in free:
        step = number_steps(0, board_size)
        if step not in free:
            print('Поле уже занято!!! ')
    return step


def comp_step(brd, comp, human):
    brd = brd[:]
    print('Ходит железяка: ')
    for i in free_moves(brd):
        i = random.randint(0, 99)
        return i
        brd[i] = comp
        if winner(brd) == comp:
            print(i)
            return i
        brd[i] = steps
    for j in free_moves(brd):
        brd[j] = human
        if winner(brd) == human:
            print(j)
            return j
        brd[j] = steps
    for k in free_moves(brd):
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


def ques():
    answer = None
    while answer not in ('да', 'нет'):
        answer = input('Сыграть еще раз?(да/нет)').lower()
        if answer == 'да':
            main()
        else:
            continue


def main():
    try:
        description()
        human: str
        comp, human = who_x_0()
        queue = X
        brd = new_board()
        show_board(brd)
        while not loss(brd):
            if queue == human:
                step = human_step(brd, human)
                brd[step] = human
            else:
                step = comp_step(brd, comp, human)
                brd[step] = comp
            show_board(brd)
            queue = next_turn(queue)
        loser = loss(brd)
        who_loss(loser, comp, human)
        ques()
    except KeyboardInterrupt:
        print("\n\n\nBye-bye!!!")




main()
