def selectSort(numbers):
    for i in range(len(numbers)):
        minIndex = i
        for j in range(i + 1, len(numbers)):
            if numbers[minIndex] > numbers[j]:
                minIndex = j
    
        numbers[i], numbers[minIndex] = numbers[minIndex], numbers[i]
    return numbers

print(selectSort([9,1,8,2,7,3,6,4,5,0,0]))