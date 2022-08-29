from itertools import combinations


string = input()
pivots = combinations(range(1, len(string)), 2)
words = []
for pivot in pivots:
    front = "".join(string[:pivot[0]])[::-1]
    mid = "".join(string[pivot[0]:pivot[1]])[::-1]
    tail = "".join(string[pivot[1]:])[::-1]

    words.append(front + mid + tail)

words.sort()
print(words[0])
