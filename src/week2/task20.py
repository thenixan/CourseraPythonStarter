k = int(input())

l1 = k % 15

if l1 % 3 == 0 or l1 % 5 == 0:
    print("YES")
else:
    print("NO")
