n = int(input())
houses = list(map(int, input().split()))
houses.sort()
print(houses[len(houses) // 2 - 1])
