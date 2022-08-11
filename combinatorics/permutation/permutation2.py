myNumbers = [1,2,3,4,5]

for a in range(len(myNumbers)):
    for b in range(len(myNumbers)):
        if a != b:
            print((myNumbers[a], myNumbers[b]))

print()

for a in range(len(myNumbers)):
    for b in range(len(myNumbers)):
        for c in range(len(myNumbers)):
            if a != b and b != c and c != a:
                print((myNumbers[a], myNumbers[b], myNumbers[c]))