result = 0
current_max = 0
while True:
    i = int(input())
    if i == 0:
        break
    elif current_max < i:
        current_max = i
        result = 1
    elif current_max == i:
        result = result + 1

print(result)
