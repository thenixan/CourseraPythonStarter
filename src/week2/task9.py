n = int(input())

if 10 < n % 100 < 20 or n % 10 == 0 or n % 10 >= 5:
    print(n, "korov")
elif n % 10 == 1:
    print(n, "korova")
else:
    print(n, "korovy")
