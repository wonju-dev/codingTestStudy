n = 10
data = "1 1 9 9 2 8 8 3 3 3 7 7 7 7 4 6 5 5 0 0 0"
count = [0] * 10

for num in data.split():
    count[int(num)] += 1

for i in range(n):
    for j in range(count[i]):
        print(i)