number = input()

front = 0
back = 0
for i in range(len(number) // 2):
    front += int(number[i])
    back += int(number[i + len(number) // 2])

if front == back:
    print("LUCKY")
else:
    print("READY")

    