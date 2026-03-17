hour, minute = map(int, input().split())
time = hour * 60 + minute - 45
if time < 0:
    time += 1440
alarm_hour = time // 60
alarm_minute = time % 60
print(alarm_hour, alarm_minute)