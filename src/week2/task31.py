max = 0

finished = False
while not finished:
    n = int(input())
    if n == 0:
        finished = True
    elif max < n:
        max = n

print(max)
