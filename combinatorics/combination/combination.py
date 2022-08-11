from itertools import combinations

myNumbers = [1,2,3,4]

pairs = combinations(myNumbers, 2)

for pair in pairs:
    print(pair)