a = int(input())
b = int(input())
c = int(input())

hasodd = (a % 2 == 0 or b % 2 == 0 or c % 2 == 0)
haseven = (a % 2 == 1 or b % 2 == 1 or c % 2 == 1)

if hasodd and haseven:
    print("YES")
else:
    print("NO")
