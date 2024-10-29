def s(num):
    sum_div = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_div += i
    return sum_div
n = int(input())
m = int(input())
sum_n=s(n)
sum_m=s(m)
if sum_n == m and sum_m == n:
    print("Amicable")
else:
    print("Not Amicable")