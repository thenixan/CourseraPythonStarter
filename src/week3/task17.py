s = input()

first = s.find("h") + 1
last = s[::-1].find("h")
last = len(s) - last - 1

print(s[:first], s[first:last], s[first:last], s[last:], sep='')
