def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    names = []
    
    day1Map = {}
    
    for i in range(len(steps_one)):
        if names_one[i] not in names:
            names.append(names_one[i])
        if day1Map.get(names_one[i]) is not None:
            day1Map[names_one[i]] = max(day1Map[names_one[i]], steps_one[i])
        else:
            day1Map[names_one[i]] = steps_one[i]

    day2Map = {}
    
    for i in range(len(steps_two)):
        if names_two[i] not in names:
            names.append(names_two[i])
        if day2Map.get(names_two[i]) is not None:
            day2Map[names_two[i]] = max(day2Map[names_two[i]], steps_two[i])
        else:
            day2Map[names_two[i]] = steps_two[i]

    day3Map = {}
    
    for i in range(len(steps_three)):
        if names_three[i] not in names:
            names.append(names_three[i])
        if day3Map.get(names_three[i]) is not None:
            day3Map[names_three[i]] = max(day3Map[names_three[i]], steps_three[i])
        else:
            day3Map[names_three[i]] = steps_three[i]
    
    records = []

    for i in range(len(names)):
        total = 0
        if day1Map.get(names[i]) is not None:
            total += day1Map.get(names[i])
        if day2Map.get(names[i]) is not None:
            total += day2Map.get(names[i])
        if day3Map.get(names[i]) is not None:
            total += day3Map.get(names[i])
        records.append((names[i], total))
    
    records.sort(key=lambda x: x[1], reverse = True)
    
    answer = []
    for record in records:
        answer.append(record[0])

    print(records)
    return answer

print(solution([1,2,3, 10000], ['a','b','c','c'], [10,20,30], ['a','c','b'], [1000, 1,1], ['b','c','a']))