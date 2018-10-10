x = int(input())
y = int(input())
n = int(input())


if x * y > n and (n % x == 0 or n % y == 0):
    print("YES")
else:
    print("NO")
