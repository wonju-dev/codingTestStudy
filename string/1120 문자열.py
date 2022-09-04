a, b = input().split()

minCount = 51
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1
    if minCount > count:
        minCount = count

print(minCount)