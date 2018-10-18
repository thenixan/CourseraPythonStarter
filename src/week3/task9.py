res = 0.0
s = 0.0
index = 0

res_x = 0.0
res_d = 0.0

while True:
    i = int(input())
    if i == 0:
        break
    else:
        s = s + i
        res_x = res_x + i ** 2
        res_d = res_d + i
        index = index + 1

s = s / index

res = res_x - 2 * s * res_d + index * (s ** 2)

print((res / (index - 1)) ** 0.5)
