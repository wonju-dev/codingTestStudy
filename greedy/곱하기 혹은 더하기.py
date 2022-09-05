from collections import deque


numbers = deque(list(map(int, list(input()))))

while len(numbers) != 1:
    one = numbers.popleft()
    two = numbers.popleft()

    if one + two > one * two:
        numbers.appendleft(one + two)
    else:
        numbers.appendleft(one * two)

print(numbers[0])