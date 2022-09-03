text = input()

while text != "#":
    count = 0
    for i in range(len(text)):
        if text[i] in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
            count += 1
    print(count)
    text = input()
