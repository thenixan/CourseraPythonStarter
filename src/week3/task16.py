s = input()

first = s.find("h")
last = s[::-1].find("h")
last = len(s) - last

print(s[:first], s[last:], sep='')
