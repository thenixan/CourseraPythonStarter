seq_count = 1
prev = 0
max_count = 1
sign = 0
while True:
    i = int(input())
    if i == 0:
        break
    elif (sign == -1 and prev > i) or (sign == 1 and prev < i):
        prev = i
        seq_count = seq_count + 1
        if seq_count > max_count:
            max_count = seq_count
    else:
        if prev == i or prev == 0:
            seq_count = 0
            sign = 0
        elif prev > i:
            if sign == 1:
                seq_count = 1
            sign = -1
        else:
            if sign == -1:
                seq_count = 1
            sign = 1
        prev = i
        seq_count = seq_count + 1
        if seq_count > max_count:
            max_count = seq_count

print(max_count)
