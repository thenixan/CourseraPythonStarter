a = int(input())
i = 1
r = 0
while i <= a:
    if 0 <= i <= 9 and i // 10 == 0:
        r = r + 1
    elif 10 <= i <= 99 and i // 100 == 0 and i % 10 == i // 10:
        r = r + 1
    elif 100 <= i <= 999 and i // 1000 == 0 and i % 10 == i // 100:
        r = r + 1
    elif 1000 <= i <= 9999 and i // 10000 == 0 and i % 10 == i // 1000 and (
            i % 100) // 10 == (i % 1000) // 100:
        r = r + 1
    elif 10000 <= i <= 99999 and i // 100000 == 0 and i % 10 == i // 10000 \
            and (
            i % 100) // 10 == (i % 10000) // 1000:
        r = r + 1
    i = i + 1
print(r)
