a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

epsilon = 10 ** -6

koef = 0

if (a < -epsilon or epsilon < a) and (b < -epsilon or epsilon < b) and (
        e < -epsilon or epsilon < e):
    p1 = c / a
    p2 = d / b
    p3 = f / e
    koef = 1
elif (c < -epsilon or epsilon < c) and (d < -epsilon or epsilon < d) and (
        f < -epsilon or epsilon < f):
    p1 = a / c
    p2 = b / d
    p3 = e / f
    koef = 1
else:
    koef = 0

if koef == 1:
    if -epsilon < p1 - p2 < epsilon and -epsilon < p2 - p3 < epsilon:
        print(5)
    elif -epsilon < p1 - p2 < epsilon and (
            p2 - p3 < -epsilon or epsilon < p2 - p3):
        print(0)
    else:
        x = (d * e - f * b) / (d * a - b * c)
        y = (f * a - e * c) / (d * a - b * c)
        print(2, x, y)
else:
    if -epsilon < a < epsilon and -epsilon < b < epsilon and -epsilon < c < \
            epsilon and -epsilon < d < epsilon:
        print(5)
    elif -epsilon < b < epsilon and -epsilon < d < epsilon:
        if a < -epsilon or epsilon < a:
            print(3, e / a)
        elif c < -epsilon or epsilon < c:
            print(3, f / c)
        else:
            print(0)
    elif -epsilon < a < epsilon and -epsilon < c < epsilon:
        if b < -epsilon or epsilon < b:
            print(4, e / b)
        elif d < -epsilon or epsilon < d:
            print(4, f / d)
        else:
            print(0)
    elif -epsilon < d * a - b * c < epsilon:
        print(1, -a / b, e / b)
    elif -epsilon < d * a - b * c < epsilon:
        print(0)
    else:
        x = (d * e - f * b) / (d * a - b * c)
        y = (f * a - e * c) / (d * a - b * c)
        print(2, x, y)
