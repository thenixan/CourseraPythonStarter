result = 0
current_max = 0
while True:
    i = int(input())
    if i == 0:
        break
    elif current_max < i:
        result = current_max
        current_max = i
    elif result < i:
        result = i

print(result)
