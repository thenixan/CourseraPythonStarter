n = int(input())

k = 0
res = 1
while True:
    if res >= n:
        break
    else:
        k = k + 1
        res = res * 2

print(k)
