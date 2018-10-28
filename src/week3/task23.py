s = input()

first = s.find("h") + 1
last = s[::-1].find("h")
last = len(s) - last - 1

m = s[first:last].replace('h', 'H')

print(s[:first], m, s[last:], sep='')
