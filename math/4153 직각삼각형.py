numbers = list(map(int , input().split()))

while numbers.count(0) != 3:
    numbers.sort(reverse=True)
    print("right") if numbers[0] ** 2 == numbers[1] ** 2 + numbers[2] ** 2 else print("wrong")
    
    numbers = list(map(int , input().split()))