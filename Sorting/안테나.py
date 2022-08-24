n = int(input())
houses = list(map(int, input().split()))

smallest = int(1e9)
location = 0

for targetHouse in houses:
    summation = 0
    for compareHouse in houses:
        summation += abs(compareHouse - targetHouse)

    if smallest > summation:
        smallest = summation
        location = targetHouse

print(location)