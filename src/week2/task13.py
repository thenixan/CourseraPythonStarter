a = int(input())
b = int(input())
c = int(input())

max, side1, side2 = a, b, c

if b > max:
    max, side1, side2 = b, c, a

if c > max:
    max, side1, side2 = c, a, b

if side1 < side2:
    side1, side2 = side2, side1

a2 = max ** 2
b2 = side1 ** 2
c2 = side2 ** 2

if (a + b <= c) or (b + c <= a) or (c + a <= b):
    print("impossible")
elif a2 == b2 + c2:
    print("rectangular")
elif a2 > b2 + c2:
    print("obtuse")
else:
    print("acute")
