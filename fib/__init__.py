def fib(N):
    a = 1
    b = 1

    for i in range(N):
        a, b = b, a + b

    return b
