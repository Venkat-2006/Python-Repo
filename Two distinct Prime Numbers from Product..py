def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_pair(N):
    if N <= 1:
        return -1  # No possible product of two primes

    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0 and is_prime(i):
            other = N // i
            if other != i and is_prime(other):
                return f"{i} {other}"

    return -1

# Input reading
N = int(input())

# Finding the prime pair
result = find_prime_pair(N)

# Output the result
print(result)
