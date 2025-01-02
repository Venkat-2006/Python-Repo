def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_mega_prime(n):
    if not is_prime(n):
        return False
    for digit in str(n):
        if digit not in '2357':
            return False
    return True

N = int(input())
if is_mega_prime(N):
    print("Mega Prime")
else:
    print("Not Mega Prime")