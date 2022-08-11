from itertools import combinations_with_replacement

myNumbers = [1,2,3,4]

pairs = combinations_with_replacement(myNumbers, 2)

for pair in pairs:
    print(pair)
