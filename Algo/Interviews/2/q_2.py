from random import randint


def dice5():
    return randint(1, 5)


def convert5to7():
    while True:
        roll_1 = dice5()
        roll_2 = dice5()

        num = ((roll_1) * 5) + (roll_2)

        if num > 21:
            continue

        return num % 7 + 1

convert5to7()
