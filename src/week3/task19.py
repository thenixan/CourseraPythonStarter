s = input()

sep = s.find(' ')
print(s[1 + sep:], s[:sep])
