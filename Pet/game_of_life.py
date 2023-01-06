from random import randint

size = 3

field = [[0 for i in range(size)] for j in range(size)]

f0, f1 = 0, 1


def create_first_generation():
    for row in range(len(field)):
        for col in range(len(field[row])):
            born = randint(0, 1)
            if born == 1:
                field[row][col] = 1


def create_next_generation():
    for row in range(len(field)):
        for col in range(len(field[row])):
            cnt = check_neighbors(field, row, col)
            if field[row][col] == 0:
                field[row][col] = check_for_dead(cnt)
            elif field[row][col] == 1:
                field[row][col] = check_for_live(cnt)
            else:
                raise ValueError(f'Impossible value {field[row][col]}')


def check_neighbors(space, row, col):
    cnt = 0
    try:
        neighbor = space[row - 1][col - 1]
    except IndexError:
        pass
    else:
        if neighbor == 1:
            cnt += 1

    try:
        neighbor = space[row - 1][col]
    except IndexError:
        pass
    else:
        if neighbor == 1:
            cnt += 1

    try:
        neighbor = space[row - 1][col + 1]
    except IndexError:
        pass
    else:
        if neighbor == 1:
            cnt += 1

    try:
        neighbor = space[row][col - 1]
    except IndexError:
        pass
    else:
        if neighbor == 1:
            cnt += 1

    try:
        neighbor = space[row][col + 1]
    except IndexError:
        pass
    else:
        if neighbor == 1:
            cnt += 1

    try:
        neighbor = space[row + 1][col - 1]
    except IndexError:
        pass
    else:
        if neighbor == 1:
            cnt += 1

    try:
        neighbor = space[row + 1][col]
    except IndexError:
        pass
    else:
        if neighbor == 1:
            cnt += 1

    try:
        neighbor = space[row + 1][col + 1]
    except IndexError:
        pass
    else:
        if neighbor == 1:
            cnt += 1

    return cnt


def check_for_live(cnt):
    if cnt in (2, 3):
        return 1
    return 0


def check_for_dead(cnt):
    if cnt >= 3:
        return 1
    return 0


def valid_blank():
    for row in field:
        if 1 in row:
            return True
    return False


def valid_repeat(iteration):
    global f0
    global f1
    if iteration % 2 == 0:
        f0 = field.copy()
    if iteration % 2 == 1:
        f1 = field[:]
    if f0 == f1:
        return True


def main():
    create_first_generation()
    print('1:\n', *field, sep='\n')
    print(f'\n{"=" * size * 2}\n')
    iteration = 0
    while True:
        create_next_generation()
        print(f'{iteration + 2}:\n', *field, sep='\n')
        print(f'\n{"=" * size * 2}\n')
        if not valid_blank():
            print('END BLANK')
            break
        if valid_repeat(iteration):
            print('END REPEAT')
            break
        iteration += 1


if __name__ == '__main__':
    main()
