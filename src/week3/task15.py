s = input()

first = s.find("f")
last = s[::-1].find("f")
if last != -1:
    last = len(s) - last - 1

if first == last and first != -1:
    print(first)
elif first != last:
    print(first, last)
