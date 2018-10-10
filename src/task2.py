line1 = "   _~_    "
line2 = "  (o o)   "
line3 = " /  V  \\  "
line4 = "/(  _  )\\ "
line5 = "  ^^ ^^   "

count = int(input())

if 0 < count <= 9:
    print(line1 * count)
    print(line2 * count)
    print(line3 * count)
    print(line4 * count)
    print(line5 * count)
