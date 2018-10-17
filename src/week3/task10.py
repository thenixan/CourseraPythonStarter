a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c

e = 10 ** -6

if -e < d < e:
    print(-b / (2 * a))
elif d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(x1, x2)
