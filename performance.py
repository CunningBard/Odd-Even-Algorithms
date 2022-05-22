import main
import time


def timed(is_even_func, numbers: int = 1000, iterate: int = 1000):
    times = 0
    the_time = 0

    for _ in range(iterate):
        current_time = time.time()
        func = is_even_func
        error = 0
        errors = []
        for number in range(numbers):
            case = func(number) == main.ordinary(number)
            if not case:
                error += 1
                errors.append(number)
                print(case)

        if error:
            print(errors)

        times += 1
        the_time += time.time() - current_time

    return the_time / times


print(timed(main.minus_2_10))

"""ls = []
for i in range(2, 101):
    if main.check_last_num(i):
        ls.append(i)


ls.sort()
ls.reverse()
print(ls)"""