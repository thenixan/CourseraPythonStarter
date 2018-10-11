k = int(input())

if k < 30 and (k < 3 or k == 4 or k == 7):
    print("NO")
elif ((k % 30) + 5) % 3 == 0 or ((k % 30) + 10) % 3 == 0 or (
        (k % 30) + 15) % 3 == 0 or ((k % 30) + 25) % 3 == 0:
    print("YES")
else:
    print("NO")
