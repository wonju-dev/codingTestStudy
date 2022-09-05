n = int(input())

students = []

for _ in range(n):
    name, kor, eng, math = input().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)

    students.append((name, kor, eng, math))

students.sort(key= lambda x : (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])