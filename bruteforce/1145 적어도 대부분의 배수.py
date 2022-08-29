numbers = list(map(int, input().split()))

now = min(numbers)
while True:    
    count = 0
    for number in numbers:
        if now % number == 0:
            count += 1

    if count >= 3:
        print(now)
        break

    now += 1