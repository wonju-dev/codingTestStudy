def solution(s):
    biggest = -1
    for i in range(len(s)-2):
        if s[i] == s[i+1] == s[i+2]:
            substring = int(s[i:i+3])
            if substring > biggest:
                biggest = substring

    return biggest
