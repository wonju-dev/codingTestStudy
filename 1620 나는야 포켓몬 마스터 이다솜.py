n, m = map(int, input().split())

dogam = {}
dogamIndex = {}

for i in range(1, n + 1):
    pokemon = input()
    dogam[i] = pokemon
    dogamIndex[pokemon] = i


for i in range(m):
    request = input()
    if request.isnumeric():
        print(dogam[int(request)])
    else:
        print(dogamIndex[request])