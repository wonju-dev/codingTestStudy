from itertools import combinations

def isPrefixSubset(subset):
    for wordA in subset:
        for wordB in subset:
            if wordA != wordB and len(wordA) > len(wordB):
                    if wordA.startswith(wordB):
                        return False
    return True

n = int(input())
words = []

# init data
for _ in range(n):
    words.append(input())

subsets = []

for i in range(1, n + 1):
    combis = combinations(words, i)
    for combi in combis:
        subsets.append(combi)

size = 0
for subset in subsets:
    if isPrefixSubset(subset):
        if size < len(subset):
            size = len(subset)

print(size)