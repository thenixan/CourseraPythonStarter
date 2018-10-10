daylength = 60 * 24

in_minutes = int(input())
day_minutes = in_minutes % daylength

print(day_minutes // 60, day_minutes % 60)
