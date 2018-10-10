a = int(input())
b = int(input())

a1 = a % b
a2 = a - a1
a3 = (a2 + a2) // (a2 + 1)

b1 = b % a
b2 = b - b1
b3 = (b2 + b2) // (b2 + 1)

print(((a * a3) + (b * b3)) // (a3 + b3))
