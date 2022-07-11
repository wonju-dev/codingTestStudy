n = int(input())

members = []

for i in range(n):
    age, name = list(input().split())
    members.append((int(age), name, i))

members = sorted(members, key=lambda x: (x[0], x[2]))

for member in members:
    print(member[0], member[1])
