first = int(input())
second = int(input())

d = second - first + 1
last = first - 1

if last % d == 0:
    print("YES")
else:
    print("NO")
