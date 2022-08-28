n = int(input())

def getMaxIndexes(votes):
    indexes = [0]
    for i in range(len(votes)):
        if i != 0:
            if votes[i] > votes[indexes[0]]:
                indexes = [i]
            elif votes[i] == votes[indexes[0]]:
                indexes.append(i)
    
    return indexes

votes = []
for _ in range(n):
    votes.append(int(input()))

count = 0
while getMaxIndexes(votes)[0] != 0 or len(getMaxIndexes(votes)) != 1:
    maxIndexes = getMaxIndexes(votes)
    if len(maxIndexes) > 1:
        votes[maxIndexes[-1]] -= 1
        votes[0] += 1
        count += 1
    else:
        votes[maxIndexes[0]] -= 1
        votes[0] += 1
        count += 1

print(count)