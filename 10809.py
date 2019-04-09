from sys import stdin
alphabet = 'abcdefghijklmnopqrstuvwxyz'
string = stdin.readline()
for n in alphabet:
    print(string.find(n), end = ' ')