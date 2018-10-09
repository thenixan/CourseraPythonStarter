seconds_in_a_day = 24 * 60 * 60

seconds = int(input())

seconds_for_a_clock = seconds % seconds_in_a_day

hours = seconds_for_a_clock // 60 // 60

seconds_for_a_clock = seconds_for_a_clock - (hours * 60 * 60)

minute = seconds_for_a_clock // 60

minute1 = minute // 10
minute2 = minute % 10

second = seconds_for_a_clock % 60

second1 = second // 10
second2 = second % 10

print(hours, ':', minute1, minute2, ':', second1, second2, sep='')
