n = int(input())
rawData = input()
chairs = []

nextPass = False
for i in range(len(rawData)):
    if nextPass == True:
        nextPass = False
        continue
    if rawData[i] == "S":
        chairs.append("*")
        chairs.append("S")
    elif rawData[i] == "L":
        chairs.append("*")
        chairs.append("L")
        chairs.append("L")
        nextPass = True
chairs.append("*")

for i in range(len(chairs)):
    if chairs[i] == "*":
        continue

    if chairs[i] == "S":
        if chairs[i - 1] == "*":
            chairs[i - 1] = "O"
        elif chairs[i + 1] == "*":
            chairs[i + 1] = "O"
    elif chairs[i] == "L":
        if chairs[i + 1] == "L":
            if chairs[i - 1] == "*":
                chairs[i - 1] = "O"
        elif chairs[i - 1] == "L":
            if chairs[i + 1] == "*":
                chairs[i + 1] = "O"
print(chairs.count("O"))