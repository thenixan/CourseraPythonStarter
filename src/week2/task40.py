n = int(input())
f0 = 0
f1 = 1
if n == 0:
    print(f0)
elif n == 1:
    print(f1)
else:
    i = 2
    f = 0
    while i <= n:
        f = f0 + f1
        f0 = f1
        f1 = f
        i = i + 1
    print(f)
