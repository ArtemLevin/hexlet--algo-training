def solution(a, b):
    if a == b:
        return print(f'gcd = {a}')
    else:
        if a > b:
            return solution(a - b, b)
        elif a < b:
            return solution(a, b - a)


solution(80, 50)
