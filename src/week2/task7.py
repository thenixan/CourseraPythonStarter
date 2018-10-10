x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

d = dx + dy

if d % 2 == 0:
    print("YES")
else:
    print("NO")
