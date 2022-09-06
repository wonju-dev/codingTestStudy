def isPalindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

def getPartialPalindrom(string):
    for i in range(len(string) - 1):
        partial = string[i:]
        if isPalindrome(partial):
            return partial
    
    return None

string = input()

if isPalindrome(string):
    print(len(string))
else:
    partial = getPartialPalindrom(string)
    
    if partial != None:
        print(len(string) + len(string) - len(partial))
    else:
        if len(string) % 2 == 0:
            print(2 * len(string) - 1)
        else:
            print(len(string) + len(string) - 1)