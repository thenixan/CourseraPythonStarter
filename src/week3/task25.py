s = input()

i = 0
r = ''
while i < len(s):
    if i % 3 != 0:
        r = r + s[i]
    i = i + 1

print(r)
