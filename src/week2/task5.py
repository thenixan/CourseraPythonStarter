x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = (x1 - x2) ** 2
dy = (y1 - y2) ** 2

d = dx + dy

if d <= 2:
    print("YES")
else:
    print("NO")
