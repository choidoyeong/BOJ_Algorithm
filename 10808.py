from sys import stdin
alphabet = 'abcdefghijklmnopqrstuvwxyz'
string = list(stdin.readline())
for n in alphabet:
    print(string.count(n), end = ' ')