def counter(func):
    count = 0
    def wrapper(arg):
        nonlocal count
        count +=1
        print(f'{count = }')
        return func(arg)

    return wrapper

@counter
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(7))