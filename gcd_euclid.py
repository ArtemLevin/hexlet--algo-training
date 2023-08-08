def solution(a, b):
    if a == b:
        return print(f'gcd = {a}')
    else:
        if a > b:
            return solution(a - b, b)
        elif a < b:
            return solution(a, b - a)


solution(80, 50)

def solution_2(a, b):
    return solution(b, a%b) if a%b else abs(b)

print(f'gcd = {solution_2(80, 5)}')
