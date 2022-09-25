def solution(today, terms, privacies):
    # print()
    answer = []

    todaies = list(map(int, today.split(".")))
    todayMonthForm = 12 * todaies[0] + todaies[1]

    # print(todaies, todayMonthForm)

    termMap = {}
    for term in terms:
        name, period = term.split()
        period = int(period)
        termMap[name] = period

    # print(termMap)

    for i in range(len(privacies)):
        date, term = privacies[i].split()
        toMonthForm = ""
        dates = list(map(int, date.split(".")))
        toMonthForm = 12 * dates[0] + dates[1]

        # print(dates, toMonthForm, term)

        if toMonthForm + termMap[term] < todayMonthForm:
            answer.append(i+1)
        elif toMonthForm + termMap[term] == todayMonthForm:
            if todaies[2] >= dates[2]:
                answer.append(i+1)
    # print(answer)
    return answer

# solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
# solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])