n = int(input())
x = float(input())

res = 0
i = 0
while i < n:
    a = float(input())
    res = (res + a) * x
    i = i + 1

a = float(input())
res = res + a

print(res)
