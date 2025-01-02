import math

def is_prime(N):
    if N <= 1:
        return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True

# Input
N = int(input())

# Output the result based on prime check
if is_prime(N):
    print("Prime")
else:
    print("Not a Prime")
