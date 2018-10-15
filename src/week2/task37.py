prev = -1
count = 0
while True:
    i = int(input())
    if i == 0:
        break
    elif prev == -1:
        prev = i
    elif prev < i:
        count = count + 1
        prev = i
    else:
        prev = i

print(count)
