loop = int(input())

numbers = []
operation = []

currentNumber = 0

flag = True

for i in range(loop):
    n = int(input())

    if currentNumber < n:
        while currentNumber != n:
            currentNumber += 1
            numbers.append(currentNumber)
            operation.append("+")

    if numbers[-1] == n:
        operation.append("-")
        numbers.pop()
    else:
        print("NO")
        flag = False
        break

if flag:
    for op in operation:
        print(op)
