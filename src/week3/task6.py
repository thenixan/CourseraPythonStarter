p = int(input())
r = int(input())
k = int(input())

e = 10 ** -6

percents = 1.0 + float(p) * 0.01
price = float(r) + float(k) * 0.01

result = price * percents

r = result // 1
k = (result % 1) * 100
if k % 1 < 1 and -e < 1 - k % 1 < e:
    k = int(k) + 1
else:
    k = int(k)

print("{0:.0f}".format(r), "{0:.0f}".format(k))
