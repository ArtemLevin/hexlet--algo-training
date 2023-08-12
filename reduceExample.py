from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def summa(a, b):
    return a + b

print(reduce(summa, numbers))