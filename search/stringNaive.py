string = "'abc'dab'abc'dabe"
target = "abc"

count = 0
for i in range(len(string) - len(target)):
    if string[i:i + len(target)] == target:
        count += 1

print(count)