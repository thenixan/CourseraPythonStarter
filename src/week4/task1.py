a = int(input())
b = int(input())
c = int(input())
d = int(input())


def min4(x, y, z, f):
    r1 = min(x, y)
    r2 = min(z, f)
    return min(r1, r2)


print(min4(a, b, c, d))
