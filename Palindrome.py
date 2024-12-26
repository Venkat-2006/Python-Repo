def is_palindrome(n):
    return str(n) == str(n)[::-1]
N = int(input())
if is_palindrome(N):
    print("Palindrome")
else:
    print("Not Palindrome")
