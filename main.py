"""
the following algorithms are only for checking if its even
"""


def ordinary(num: int):
    return num % 2 == 0


def check_last_num(num: int):
    return str(num)[-1] in ["2", "4", "6", "8", "0"]


def minus_2(num: int):
    num = abs(num)
    while num != 1 and num != 0:
        num -= 2

    return not bool(num)


def minus_2_10(num: int):
    num = abs(num)
    while num != 1 and num != 0:
        for i in [10, 8, 6, 4, 2]:
            if num >= i:
                num -= i
                break

    return not bool(num)


def minus_2_100(num: int):
    num = abs(num)
    while num != 1 and num != 0:
        for i in [100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52,
                  50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]:
            if num >= i:
                num -= i
                break

    return not bool(num)


def range_num(num: int):
    num = abs(num)
    current_bool = True
    for _ in range(num):
        current_bool = not current_bool
    return current_bool


def too_understandable(num: int):
    # credit to Bamboooz#8423
    if num/2 == int(num/2):
        return True
    else:
        return False


if __name__ == '__main__':
    func = too_understandable
    error = 0
    errors = []
    for number in range(100):
        case = func(number) == ordinary(number)
        if not case:
            error += 1
            errors.append(number)
        else:
            print(case)

    print()
    print(bool(error))
    if error:
        print(errors)
