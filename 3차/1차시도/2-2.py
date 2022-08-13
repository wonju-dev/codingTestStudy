def solution(ingredient):
    if len(ingredient) < 4:
        return 0

    string = "".join(list(map(str, ingredient)))


    count = 0
    while True:
        index = string.find("1231")
        if index == -1:
            return count
        else:
            count += 1
            string = string[:index] + string[index + 4:]

# 시간초과 (88.2 / 100) / 테케 5번, 12번