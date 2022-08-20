from pydoc import plain


def solution(survey, choices):
    surveyMap = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0
    }
    scoreMap = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3
    }

    for i in range(len(survey)):
        minus = survey[i][0]
        plus = survey[i][1]

        if choices[i] <= 3:
            surveyMap[minus] += scoreMap[choices[i]]
        elif choices[i] >= 4:
            surveyMap[plus] += scoreMap[choices[i]]

    answer = ''
    pairs = [
        ("R", "T"),
        ("C", "F"),
        ("J", "M"),
        ("A", "N")
    ]
    for pair in pairs:
        if surveyMap[pair[0]] > surveyMap[pair[1]]:
            answer += pair[0]
        elif surveyMap[pair[0]] < surveyMap[pair[1]]:
            answer += pair[1]
        else:
            answer += pair[0]
    return answer