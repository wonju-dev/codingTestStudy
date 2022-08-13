from itertools import permutations

numbers = [1,2,3,4,5]

for pair in permutations(numbers, 2):
    print(pair)