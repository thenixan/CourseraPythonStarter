l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
l, w, h = int(input()), int(input()), int(input())

# l1 <= l and l2 <= l and h1 <= h and h2 <= h and w1 <= w and w2 <= w

v01 = (l1 + l2) <= l and h1 <= h and h2 <= h and w1 <= w and w2 <= w
v02 = l1 <= l and l2 <= l and (h1 + h2) <= h and w1 <= w and w2 <= w
v03 = l1 <= l and l2 <= l and h1 <= h and h2 <= h and (w1 + w2) <= w

l1, w1 = w1, l1
v04 = (l1 + l2) <= l and h1 <= h and h2 <= h and w1 <= w and w2 <= w
v05 = l1 <= l and l2 <= l and (h1 + h2) <= h and w1 <= w and w2 <= w
v06 = l1 <= l and l2 <= l and h1 <= h and h2 <= h and (w1 + w2) <= w
l1, w1 = w1, l1

l2, w2 = w2, l2
v07 = (l1 + l2) <= l and h1 <= h and h2 <= h and w1 <= w and w2 <= w
v08 = l1 <= l and l2 <= l and (h1 + h2) <= h and w1 <= w and w2 <= w
v09 = l1 <= l and l2 <= l and h1 <= h and h2 <= h and (w1 + w2) <= w
l2, w2 = w2, l2

l1, w1 = w1, l1
l2, w2 = w2, l2
v10 = (l1 + l2) <= l and h1 <= h and h2 <= h and w1 <= w and w2 <= w
v11 = l1 <= l and l2 <= l and (h1 + h2) <= h and w1 <= w and w2 <= w
v12 = l1 <= l and l2 <= l and h1 <= h and h2 <= h and (w1 + w2) <= w

if v01 or v02 or v03 or v04 or v05 or v06 or v07 or v08 or v09 or v10 or v11 \
        or v12:
    print("YES")
else:
    print("NO")
