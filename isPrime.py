import math


def isPrimeBool(number):
    count = 0
    for i in range(1, round(math.sqrt(number))+2):
        if number%i == 0: count += 1
    if count == 2: return True
    else: return False


def say_prime_or_not(number):
    if isPrimeBool(number): return "yes"
    else: return "no"

print(say_prime_or_not(13))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def say_prime_or_not(num):
    answer = 'yes' if is_prime(num) else 'no'
    print(answer)