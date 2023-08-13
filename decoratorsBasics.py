def memoization(func):
    valueDict = {}
    def wrapper(arg):
        nonlocaL = valueDict
        if arg in valueDict.keys():
            return valueDict[arg]
        else:
            valueDict[arg] = func(arg)
            return valueDict[arg]
    return wrapper

@memoization
def fib(n):
    if n == 1 or n == 2: return 1
    else: return fib(n-1) + fib(n-2)


print(fib(50))


