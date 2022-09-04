case = int(input())

for _ in range(case):
    password = input()
    print("yes" if 6 <= len(password) <= 9 else "no")