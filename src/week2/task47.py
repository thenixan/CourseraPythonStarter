first_n = 0
second_n = 0
candidate = 0
index = 0
prev = 0
res = 0
direction = 0
while True:
    i = int(input())
    if i == 0:
        break
    else:
        if prev == 0:
            prev = i
        else:
            if prev < i:
                direction = 1
            elif prev == i:
                direction = 0
            elif prev > i and direction > 0:
                first_n = second_n
                second_n = index
                if first_n != 0 and second_n != 0 and (
                        res == 0 or res > second_n - first_n):
                    res = second_n - first_n
                direction = -1
            elif prev > i and direction <= 0:
                direction = -1
            prev = i
        index = index + 1

if second_n != 0 and first_n != 0:
    print(res)
else:
    print(0)
