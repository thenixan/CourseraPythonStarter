h = int(input())
a = int(input())
b = int(input())

distance = h - b
velocity = a - b

print((distance + velocity - 1) // velocity)
