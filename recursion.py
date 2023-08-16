def counter(func):
    myCount = 0
    def wrapper(*arg):
        nonlocal myCount
        myCount +=1
        print(f'{myCount = }')
        return func(*arg)

    return wrapper


@counter
def length(list, myCount=0):
    if list is None:
        return myCount
    else:
        return length(list[1:], myCount)

print(length([1,2,3,4,5]))
