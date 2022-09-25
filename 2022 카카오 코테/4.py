def getBinaryString(number):
    string = "" 
    while number > 1:
        share = number // 2
        remainder = number % 2
        string = str(remainder) + string
        number = share

    if len(str(number) + string) % 2 == 0:
        return "0" + str(number) + string
    else:
        return str(number) + string

def check(binary):
    if len(binary) == 1:
        return True
    
    if len(binary) < 3:
        binary = binary + "0"
    
    if binary[len(binary) // 2] == "0":
        return False
    else:
        return check(binary[:len(binary) // 2]) and check(binary[len(binary) // 2 + 1:])


def solution(numbers):
    answer = []

    for number in numbers:
        binaryString = getBinaryString(number) 
        
        if check(binaryString):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
