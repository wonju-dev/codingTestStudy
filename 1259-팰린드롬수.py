while True:
    num = input()
    if num == "0":
        break
        
    head = 0
    tail = len(num) - 1

    while head <= tail:
        if num[head] != num[tail]:
            print("no")
            break
        else:
            head += 1
            tail -= 1
    else:
        print("yes")
