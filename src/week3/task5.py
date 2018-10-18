a = float(input())
e = 10 ** -6

r = int(a // 1)
k = a % 1

if -e < k - 0.5 < e:
    print(r + 1)
elif k < 0.5:
    print(r)
else:
    print(r + 1)
