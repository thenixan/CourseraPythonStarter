n = int(input())

i = 1
while i <= n:
    if i ** 2 <= n:
        print(i ** 2, end=' ')
        i = i + 1
    else:
        break
