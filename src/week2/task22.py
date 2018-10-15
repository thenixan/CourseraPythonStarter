k, m, n = int(input()), int(input()), int(input())

not_fits = n % k

times = n // k
if not_fits == 0:
    diff = 0
elif k // 2 >= not_fits:
    diff = 1
else:
    diff = 2
times = times * 2 + diff

print(times * m)
