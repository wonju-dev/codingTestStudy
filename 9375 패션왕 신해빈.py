l = int(input())

for q in range(l):
    n = int(input())
    closet = {}

    for _ in range(n):
        _, category = map(str, input().split())

        clothes = closet.get(category)

        if clothes is None:
            closet[category] = 1
        else:
            closet[category] = closet[category] + 1

    if len(closet) == 1:
        closet['_'] = 0
    
    count = 1
    for numOfClothePerCategory in closet.values():
        count *= numOfClothePerCategory + 1
    print(count - 1)