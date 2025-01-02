def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def non_prime_divisors(N):
    divisors = []
    for i in range(1, N + 1):
        if N % i == 0:
            divisors.append(i)
    non_prime_count = 0
    for divisor in divisors:
        if not is_prime(divisor):
            non_prime_count += 1
    return non_prime_count
N = int(input())
print(non_prime_divisors(N))
