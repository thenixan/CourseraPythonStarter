first_n = 0
second_n = 0
candidate = 0
index = 0
prev = 0
res = 0
while True:
    i = int(input())
    if i == 0:
        break
    else:
        if prev != 0 and prev < i:
            candidate = index
        elif prev != 0 and prev > i:
            first_n = second_n
            second_n = candidate
            candidate = 0
            if (
                    res == 0 or res > second_n - first_n) and second_n != 0 \
                    and first_n != 0:
                res = second_n - first_n
        index = index + 1
        prev = i

if second_n != 0 and first_n != 0:
    print(res)
else:
    print(0)
