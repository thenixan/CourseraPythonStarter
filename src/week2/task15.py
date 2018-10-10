a, b, c = int(input()), int(input()), int(input())

first, second, third = a, b, c

if first > b:
    first, second, third = b, c, a

if first > c:
    first, second, third = c, a, b

if second > third:
    second, third = third, second

print(first, second, third)
