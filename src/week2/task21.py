a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a == 0 and b == 0:
    print("INF")
elif b % a == 0:
    r = -b / a
    if c * r + d != 0:
        print(int(r))
    else:
        print("NO")
else:
    print("NO")
