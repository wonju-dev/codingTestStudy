a, b = input().split()

# a's min
aMin = []
for i in range(len(a)):
    if a[i] == '6':
        aMin.append('5')
    else:
        aMin.append(a[i])

# a's max
aMax = []
for i in range(len(a)):
    if a[i] == '5':
        aMax.append('6')
    else:
        aMax.append(a[i])

# a's min
bMin = []
for i in range(len(b)):
    if b[i] == '6':
        bMin.append('5')
    else:
        bMin.append(b[i])

# a's max
bMax = []
for i in range(len(b)):
    if b[i] == '5':
        bMax.append('6')
    else:
        bMax.append(b[i])

print(int("".join(aMin)) + int("".join(bMin)), end=" ")
print(int("".join(aMax)) + int("".join(bMax)))