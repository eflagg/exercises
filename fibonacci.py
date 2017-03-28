def fib_iter(n):

    if n < 2:
        return n

    prev_prev = 0
    prev = 1

    for i in range(n - 1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current

    return current


def fib_recur(n):

    if n < 2:
        return n

    return fib_recur(n - 1) + fib_recur(n - 2)