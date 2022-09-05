def isPalindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

def getPartialPalindromStartIndex(string):
    for i in range(len(string) - 1):
        partial = string[i:]
        if isPalindrome(partial):
            if len(partial) % 2 == 1:
                return (i + (len(partial) // 2) + 1, True)
            else:
                return (i + (len(partial) // 2) - 1, False)
    return (-1, True) 

string = input()

if isPalindrome(string):
    print(len(string))
else:
    startIndex, isOdd = getPartialPalindromStartIndex(string)
    
    if startIndex == -1:
        startIndex = len(string) - 1

    if not isOdd:
        string = string[:startIndex + 1] + '_' + string[startIndex + 1:]
        startIndex += 1

    diff = 1

    while not isPalindrome(string):
        if startIndex + diff == len(string):
            string += string[startIndex - diff]
        else:
            diff += 1

    underbarIndex = string.find("_")
    if underbarIndex != -1:
        string = string[:underbarIndex] + string[underbarIndex + 1:]

    print(len(string))