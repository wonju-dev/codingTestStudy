n = int(input())

numbers = []
for i in range(n):
    numbers.append(int(input()))

# 산술평균
print(round(sum(numbers) / len(numbers)))

numbers = sorted(numbers)

# 중앙값
print(numbers[int(len(numbers) / 2)])

# 최빈값
numberMap = {}
for nums in numbers:
    if nums in numberMap:
        numberMap[nums] += 1
    else:
        numberMap[nums] = 1

# key (숫자) : value(빈도)로 구성된 dic 생성 / 정렬기준 : 최빈값(x[1]), 숫자(x[0])
dic = sorted(list(numberMap.items()), key=lambda x: (x[1], x[0]))
# 최빈값이 가장 높은 숫자들만 필터링
filtered = list(filter(lambda x: x[1] == dic[-1][1], dic))
# 필터 결과가 1개 
if len(filtered) == 1:
    print(filtered[0][0])
# 필터 결과가 2개 이상
else:
    print(filtered[1][0])

# 범위
print(numbers[-1] - numbers[0])
