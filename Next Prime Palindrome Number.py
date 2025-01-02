def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_prime_palindrome(N):
    N += 1
    while True:
        if is_prime(N) and is_palindrome(N):
            return N
        N += 1

N = int(input())
print(next_prime_palindrome(N))
