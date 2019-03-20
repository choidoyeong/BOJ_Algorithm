from sys import stdin
num = int(stdin.readline())
queue = []
for n in range(0, num):
    commend = stdin.readline().rstrip()
    if(commend == 'pop'):
        if(len(queue) == 0):
            print(-1)
            continue
        print(queue.pop(0))
    elif(commend == 'size'):
        print(len(queue))
    elif(commend == 'empty'):
        if(len(queue) != 0):
            print(0)
            continue
        print(1)
    elif(commend == 'front'):
        if(len(queue) == 0):
            print(-1)
            continue
        print(queue[0])
    elif(commend == 'back'):
        if(len(queue) == 0):
            print(-1)
            continue
        print(queue[-1])
    else:
        queue.append(commend[5:])