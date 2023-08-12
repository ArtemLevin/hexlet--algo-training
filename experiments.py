# def greet(name, surname):
#     return f'Hello, {name} {surname}!'
#
# def partial_aplly(someFunc, argForSomeFunc):
#     def getAnotherArg(anotherArg):
#         return someFunc(argForSomeFunc, anotherArg)
#     return getAnotherArg
#
# f = partial_aplly(greet, 'Dorian')
# print(f('Grey'))


# def partial_apply(function, arg1):
#     def inner(arg2):
#         return function(arg1, arg2)
#     return inner

def func(arg1, arg2):
    return f'{arg1 = }, {arg2 =}'
def flip(func):
    def inner(arg1, arg2):
        return func(arg2, arg1)
    return inner

c = flip(func)
print(c(1, 2))