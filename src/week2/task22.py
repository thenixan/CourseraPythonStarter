k, m, n = int(input()), int(input()), int(input())

fits = n % k == 0

times = (n // k) * 2
if not fits:
    times = times + 1

print(times * m)
