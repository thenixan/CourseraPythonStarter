a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

r1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
r2 = (a1 // b2) * (b1 // c2) * (c1 // a2)
r3 = (a1 // c2) * (b1 // a2) * (c1 // b2)
r4 = (a1 // a2) * (b1 // c2) * (c1 // b2)
r5 = (a1 // b2) * (b1 // a2) * (c1 // c2)
r6 = (a1 // c2) * (b1 // b2) * (c1 // a2)

r = r1
if r < r2:
    r = r2
if r < r3:
    r = r3
if r < r4:
    r = r4
if r < r5:
    r = r5
if r < r6:
    r = r6

print(r)
