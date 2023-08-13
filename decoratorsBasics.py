from collections import OrderedDict
from functools import wraps


def wrapped(function):
    @wraps(function)
    def inner(arg):
        return function(arg)

    return inner


def greater_than_max_length(value):
    def predicate(arg):
        return arg >= value

    return predicate


def memoization(predicate):
    valueDict = OrderedDict()

    def wrapper(func):
        def inner(arg):
            nonlocaL = valueDict
            if arg in valueDict.keys():
                return valueDict[arg]
            else:
                if predicate(len(valueDict)):
                    del valueDict[list(valueDict)[0]]
                valueDict[arg] = func(arg)
                return valueDict[arg]

        return inner

    return wrapper


@wrapped
@memoization(greater_than_max_length(10))
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(100))
