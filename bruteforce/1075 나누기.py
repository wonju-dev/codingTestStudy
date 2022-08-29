n = input()
f = int(input())

front = n[:-2]
for i in range(10):
    if int(front + '0' + str(i)) % f == 0:
        print('0' + str(i))
        break
else:
    for i in range(10, 100):
        if int(front + str(i)) % f == 0:
            print(str(i))
            break