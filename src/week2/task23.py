l1, r1, l2, r2, l3, r3 = int(input()), int(input()), int(input()), int(
    input()), int(input()), int(input())

ov12 = r2 >= l1 >= l2 or r2 >= r1 >= l2 or r1 >= l2 >= l1 or r1 >= r2 >= l1
if ov12:
    d12 = 0
elif l1 > r2:
    d12 = l1 - r2
else:
    d12 = l2 - r1

ov23 = r3 >= l2 >= l3 or r3 >= r2 >= l3 or r2 >= l3 >= l2 or r2 >= r3 >= l2
if ov23:
    d23 = 0
elif l2 > r3:
    d23 = l2 - r3
else:
    d23 = l3 - r2

ov31 = r1 >= l3 >= l1 or r1 >= r3 >= l1 or r3 >= l1 >= l3 or r3 >= r1 >= l3
if ov31:
    d31 = 0
elif l3 > r1:
    d31 = l3 - r1
else:
    d31 = l1 - r3

if (d12 == 0 and d23 == 0) or (d23 == 0 and d31 == 0) or (
        d31 == 0 and d12 == 0):
    print(0)
elif d23 <= r1 - l1:
    print(1)
elif d31 <= r2 - l2:
    print(2)
elif d12 <= r3 - l3:
    print(3)
else:
    print(-1)
