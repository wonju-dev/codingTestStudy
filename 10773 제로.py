l = int(input())
numbers =[]
for _ in range(l):
    n = int(input())
    if n == 0:
        numbers.pop()
    else:
        numbers.append(n)
        
print(sum(numbers))
    