CASE = 5

index = ""
for i in range(1, CASE + 1):
    name = input()
    if "FBI" in name:
        index += str(i) + " "
    
if index == "":
    print("HE GOT AWAY!")
else:
    print(index)