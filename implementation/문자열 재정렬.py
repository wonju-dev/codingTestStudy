string = input()

alphas = []
total = 0
for i in range(len(string)):
    if string[i].isalpha():
        alphas.append(string[i])
    else:
        total += int(string[i])

alphas.sort()

print("".join(alphas) + str(total))