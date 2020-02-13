# calculate nth febonacchi no.


def calculate_fib_no(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return calculate_fib_no(n-1) + calculate_fib_no(n-2)


assert(calculate_fib_no(10)) == 55
