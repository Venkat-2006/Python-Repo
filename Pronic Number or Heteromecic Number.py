def p(n):
    x=int(n**0.5)
    return x*(x+1)==n
i=int(input())
if p(i):
    print("YES")
else:
    print("NO")