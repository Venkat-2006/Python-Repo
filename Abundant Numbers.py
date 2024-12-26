def is_abundant(n):
    sum_of_factors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_factors += i
    return sum_of_factors > n

N = int(input())
print(is_abundant(N))
