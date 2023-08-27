def solution(str_1, str_2):
    new_str_1 =''.join(str_1.split('#'))
    new_str_2 = ''.join(str_2.split('#'))
    return new_str_1 == new_str_2
print(solution('',  ''))

