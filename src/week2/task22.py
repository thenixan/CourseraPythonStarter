k, m, n = int(input()), int(input()), int(input())

required = m * n * 2

l = n % k

s = (n // k) * 2 * m

print(s + (l * m))
