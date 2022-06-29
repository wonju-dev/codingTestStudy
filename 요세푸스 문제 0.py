n, k = list(map(int, input().split(" ")))

people = list(range(1, n + 1))
answer = []

index = 0
counter = 1

while people.count(False) != n:

    while counter != k or not people[index]:
        if people[index]:
            counter += 1
        index = (index + 1) % n

    answer.append(people[index])
    people[index] = False
    counter = 1

print("<" + ", ".join(list(map(str, answer))) + ">")
