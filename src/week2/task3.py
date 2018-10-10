first = int(input())
second = int(input())
third = int(input())

if first > second:
    second = first
if second > third:
    third = second

print(third)
