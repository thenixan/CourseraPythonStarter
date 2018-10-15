seq_count = 0
prev = 0
max_count = 1
while True:
    i = int(input())
    if i == 0:
        break
    elif prev == i:
        seq_count = seq_count + 1
        if seq_count > max_count:
            max_count = seq_count
    else:
        seq_count = 1
        prev = i

print(max_count)
