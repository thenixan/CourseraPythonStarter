n = int(input())
f0 = 0
f1 = 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    i = 2
    f = 0
    while f <= n:
        f = f0 + f1
        f0 = f1
        f1 = f
        if f == n:
            print(i)
            break
        i = i + 1
    else:
        print(-1)
