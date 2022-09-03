case = int(input())

pattern = []

for _ in range(case):
    if len(pattern) != 0:
        name = list(input())
        for i in range(len(name)):
            if pattern[i] != name[i]:
                pattern[i] = "?"
    else:
        pattern = list(input())

print("".join(pattern))