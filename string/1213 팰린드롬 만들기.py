from math import ceil

def getHighestPriorityAlphabet(alphabetMap, index):
    return sorted(alphabetMap.items(), key= lambda x : x[0])[index]

string = input()
alphabetMap = {}
for i in range(len(string)):
    if string[i] in alphabetMap:
        alphabetMap[string[i]] += 1
    else:
        alphabetMap[string[i]] = 1

answer = "_" * len(string)

for i in range(ceil(len(string) / 2)):
    key, value = getHighestPriorityAlphabet(alphabetMap, 0)
    if value < 2 and len(alphabetMap.items()) > 1:
        key, value = getHighestPriorityAlphabet(alphabetMap, 1)

    if value >= 2:
        oppositeIndex = len(string) - 1 - i
        answer = answer[:i] + key + answer[i + 1 : oppositeIndex] + key + answer[oppositeIndex + 1:]
    else:
        answer = answer[:i] + key + answer[i + 1 :]
    
    if value == 2:
        del alphabetMap[key]
    else:
        alphabetMap[key] -= 2

if answer.count("_") != 0:
    print("I'm Sorry Hansoo")
else:
    print(answer)