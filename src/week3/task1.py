x = float(input())
y = float(input())
z = float(input())

p = (x + y + z) / 2

s = (p * (p - x) * (p - y) * (p - z)) ** 0.5

print("{0:.5f}".format(s))
