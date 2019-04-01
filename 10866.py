from sys import stdin
num = int(stdin.readline())
deque = []
for n in range(0, num):
    commend = stdin.readline().split()
    if(commend[0] == 'push_front'):
        deque.insert(0, commend[1])
    elif(commend[0] == 'push_back'):
        deque.append(commend[1])
    elif(commend[0] == 'pop_front' and len(deque) != 0):
        print(deque.pop(0))
    elif(commend[0] == 'pop_back' and len(deque) != 0):
        print(deque.pop())
    elif(commend[0] == 'size'):
        print(len(deque))
    elif(commend[0] == 'empty'):
        if(len(deque)):
            print(0)
        else:
            print(1)
    elif(commend[0] == 'front' and len(deque) != 0):
        print(deque[0])
    elif(commend[0] == 'back' and len(deque) != 0):
        print(deque[len(deque)-1])
    else:
        print(-1)