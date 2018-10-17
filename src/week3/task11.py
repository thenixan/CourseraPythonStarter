a = float(input())
b = float(input())
c = float(input())

e = 10 ** -6

if -e < a < e and -e < b < e and -e < c < e:
    print(3)
elif -e < a < e and -e < b < e:
    print(0)
elif -e < a < e:
    print(1, -c / b)
else:

    d = b ** 2 - 4 * a * c

    if -e < d < e:
        print(1, -b / (2 * a))
    elif d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        print(2, x1, x2)
    else:
        print(0)
