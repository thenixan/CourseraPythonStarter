a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

x1, y1, z1 = a1, b1, c1
if x1 < b1:
    x1, y1, z1 = b1, c1, a1
if x1 < c1:
    x1, y1, z1 = c1, a1, b1
if y1 < z1:
    y1, z1 = z1, y1

x2, y2, z2 = a2, b2, c2
if x2 < b2:
    x2, y2, z2 = b2, c2, a2
if x2 < c2:
    x2, y2, z2 = c2, a2, b2
if y2 < z2:
    y2, z2 = z2, y2

if x1 == x2 and y1 == y2 and z1 == z1:
    print("Boxes are equal")
elif x1 <= x2 and y1 <= y2 and z1 <= z2:
    print("The first box is smaller than the second one")
elif x1 >= x2 and y1 >= y2 and z1 >= z2:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
