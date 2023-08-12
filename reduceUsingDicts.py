import operator
from functools import reduce
from operator import getitem


def walk(dictionary, path):
    return reduce(getitem, path, dictionary)

print (walk({'a': {7: {'b': 42}}}, ["a", 7]))