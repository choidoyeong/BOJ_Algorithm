import sys
str1 = ','.join(sys.stdin.readline().rstrip()).split(",")
num = int(sys.stdin.readline())
str2 = []
for n in range(0, num):
    commend = sys.stdin.readline().rstrip()
    if commend == 'L':
        if(len(str1) != 0):
            str2.append(str1.pop())
    elif commend == "D":
        if(len(str2) != 0):
            str1.append(str2.pop())
    elif commend == "B":
        if(len(str1) != 0):
            str1.pop()
    else:
        inputText = commend[2]
        str1.append(inputText)
str2.reverse()
result = "".join(str1 + str2)
print(result)