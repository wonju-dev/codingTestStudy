string = input()

string = string.replace("XXXX", "AAAA")
string = string.replace("XX", "BB")

if string.find("X") != -1:
    print(-1)
else:
    print(string)