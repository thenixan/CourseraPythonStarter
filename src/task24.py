a = int(input())
b = int(input())

d = a % b
d = (d + d) // (d + 1)

not_d = (d + 1) % 2


print("NO" * d)
print("YES" * not_d)
