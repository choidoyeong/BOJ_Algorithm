from sys import stdin
num = stdin.readline().rstrip()
num = num.split()
a = []
a2 = []
index = int(num[1])-1
for n in range(0, int(num[0])):
    a.append(n+1)
for n in range(0, int(num[0])):
    a2.append(str(a.pop(index)))
    if(len(a) == 0 ): continue
    index = (index + int(num[1])-1) % len(a)
enswer = "<"+", ".join(a2)+">"
print(enswer)
