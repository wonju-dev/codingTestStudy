n = int(input())

for _ in range(n):
    n, p = map(int, input().split())
    
    count = 0 
    now = 0

    while (now < n):
        if now + 2 == p:
            now +=1
        else:
            now +=2
        count += 1

    print(count)