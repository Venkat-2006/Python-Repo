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

def nearest_prime(n):
    if n < 2:
        return 2
    lower = n
    upper = n
    while True:
        if is_prime(lower):
            return lower
        if is_prime(upper):
            return upper
        lower -= 1
        upper += 1

T = int(input())
results = []
for _ in range(T):
    N = int(input())
    results.append(nearest_prime(N))

print("\n".join(map(str, results)))