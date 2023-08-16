def solution(items, direction='asc'):
    items_length = len(items)

    if items_length == 0:
        return []

    index = items_length // 2
    element = items[index]

    smaller_items = [
        items[i]
        for i in range(items_length)
        if items[i] < element and i != index
    ]
    bigger_items = [
        items[i]
        for i in range(items_length)
        if items[i] >= element and i != index
    ]

    sorted_smaller_items = solution(smaller_items, direction)
    sorted_bigger_items = solution(bigger_items, direction)

    if direction == 'asc':
        return [*sorted_smaller_items, element, *sorted_bigger_items]
    return [*sorted_bigger_items, element, *sorted_smaller_items]