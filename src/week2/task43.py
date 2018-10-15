a = int(input())
while True:
    r = a % 10
    print(r, end='')
    if a // 10 != 0:
        a = a // 10
    else:
        break
