hour, minute = list(map(int, input().split()))

isMinuteChanged = False

if minute - 45 < 0:
    minute = 60 - (45 - minute)
    isMinuteChanged = True
else:
    minute -= 45

if isMinuteChanged:
    if hour - 1 < 0:
        hour = 23
    else:
        hour -= 1

print(hour, minute)
