n = int(input())
numbers = list(map(int, input().split()))
students = []

for i in range(1, n + 1):
    n = numbers[i - 1]
    if n == 0:
        students.append(i)
    else:
        temp = []
        for _ in range(n):
            temp.append(students.pop())
        students.append(i)
        for _ in range(n):
            students.append(temp.pop())

for s in students:
    print(s, end=" ")