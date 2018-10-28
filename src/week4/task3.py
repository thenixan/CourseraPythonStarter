x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


s1 = distance(x1, y1, x2, y2)
s2 = distance(x2, y2, x3, y3)
s3 = distance(x3, y3, x1, y1)

print("{0:.6f}".format(s1 + s2 + s3))
