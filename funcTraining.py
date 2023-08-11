def ispositive(value):
    if value >= 0:
        return [True, value]
    else:
        return [False, 'Negative value']

def filter_map(ispositive, valueList):
    filterList = []
    for value in valueList:
        if ispositive(value)[0] == True:
            filterList.append(ispositive(value)[1])
    return filterList

print(filter_map(ispositive, [-1, 2, 3, -5, 7]))





