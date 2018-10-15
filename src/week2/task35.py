count = 0
avg = 0
while True:
    i = int(input())
    if i == 0:
        break
    else:
        avg = (avg * count + i) / (count + 1)
        count = count + 1

print(avg)
