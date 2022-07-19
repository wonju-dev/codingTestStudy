a = [9,1,8,2,7,3,6,4,5,0,0]

def q(array, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    q(array, start, right - 1)
    q(array, right + 1, end)

q(a, 0, len(a) - 1)
print(a)