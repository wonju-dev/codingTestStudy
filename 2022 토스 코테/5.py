def solution(tasks):
    taskMap = {}
    for task in tasks:
        if taskMap.get(task) is not None:
            taskMap[task] = taskMap[task] + 1
        else:
            taskMap[task] = 1

    myValues = list(taskMap.values())
    # print(myValues)
    answer = 0
    for i in range(len(myValues)):
        while myValues[i] - 3 >= 0:
            myValues[i] -= 3
            answer += 1
        while myValues[i] - 2 >= 0:
            myValues[i] -= 2
            answer += 1
    
    if myValues.count(0) != len(myValues):
        return -1
        
    return answer

# print(solution([1,1,2,3,3,2,2]))
# print(solution([4,1,1,1,1,2,3]))
print(solution([1, 1, 1, 1]))
