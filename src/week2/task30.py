x = int(input())
y = int(input())

count = 1
while x < y:
    count = count + 1
    x = x + x * 0.1

print(count)
