a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a == 0:
    print("INF")
elif b % a == 0:
    r = -b / a
    if c % d == 0 and r == -d / c:
        print("NO")
    else:
        print(int(r))
else:
    print("NO")
