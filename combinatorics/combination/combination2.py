myNumbers = [1,2,3,4,5]

for a in range(len(myNumbers)):
    for b in range(a + 1, len(myNumbers)):
        print((myNumbers[a], myNumbers[b]))

print()

for a in range(len(myNumbers)):
    for b in range(a + 1, len(myNumbers)):
        for c in range(b + 1, len(myNumbers)):
            print((myNumbers[a], myNumbers[b], myNumbers[c]))