from sys import stdin
num = int(stdin.readline())
countlist = [0] * 31
countlist[2] = 3
if num >= 4:
    for n in range(4, num+1, 2):
        countlist[n] = countlist[n-2]*3 + 2
	    if n-4 >= 2:
	        for n2 in range(2, n-3, 2):
		    	countlist[n] += countlist[n2]*2
print(countlist[num])
