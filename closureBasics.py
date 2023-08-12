def outer(x):
    def inner(n):
        return x+n
    return inner

sum_with_three = outer(3)
result_sum = sum_with_three(5)
print(f'{result_sum = }')
