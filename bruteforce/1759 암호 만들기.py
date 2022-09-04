from itertools import combinations


l, c = map(int, input().split())
alphabets = list(map(str, input().split()))

# 모음
vowels = []
for alphabet in alphabets:
    if alphabet in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(alphabet)
# 자음
consonants = list(set(alphabets) - set(vowels))
passwords = []

if len(vowels) > 0:
    for i in range(1, len(vowels) + 1):
        numOfVowels = i
        numOfConsonants = l - i

        vo = list(combinations(vowels, numOfVowels))
        co = list(combinations(consonants, numOfConsonants))

        for v in list(vo):
            for c in list(co):
                if len(c) >= 2 and len(v) >= 1:
                    al = sorted(list(set(v).union(set(c))))
                    passwords.append("".join(al))
    passwords.sort()
    for password in passwords:
        print(password)