n = int(input())

n1 = n // 1000
n2 = (n - n1) // 100
n3 = (n - n1 - n2 * 100) // 10
n4 = (n - n1 - n2 * 100 - n3 * 10)

print((n1 * 10 + n2) - (n4 * 10 + n3) + 1)
