xp = int(input())
yp = int(input())
xt = int(input())
yt = int(input())

initial_odd = (xp + yp) % 2 == 0

x = xt - xp
y = yt - yp

if (x - y) <= 0 and (y - x) >= 0 and yp <= yt and ((xp + yp) % 2) == (
        (xt + yt) % 2):
    print("YES")
else:
    print("NO")
