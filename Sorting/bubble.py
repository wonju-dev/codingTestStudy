def bubbleSort(numbers):
    numOfCompare = 0
    numOfSwap = 0 
    
    for i in range(1, len(numbers)):
        for j in range(len(numbers) - i):
            numOfCompare += 1
            if numbers[j] > numbers[j + 1]:
                numOfSwap += 1
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    
    print(numOfCompare, numOfSwap)

def improvedBubbleSort1(numbers):
    numOfCompare = 0
    numOfSwap = 0 
    swaped = False
    
    for i in range(1, len(numbers)):
        for j in range(len(numbers) - i):
            numOfCompare += 1
            if numbers[j] > numbers[j + 1]:
                swaped = True
                numOfSwap += 1
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        
        if not swaped:
            break

    print(numOfCompare, numOfSwap)


def improvedBubbleSort2(numbers):
    return

case = int(input())

for _ in range(case):
    numbers = list(map(int, input().split()))

    bubbleSort(list(numbers))
    improvedBubbleSort1(list(numbers))
    improvedBubbleSort2(list(numbers))
