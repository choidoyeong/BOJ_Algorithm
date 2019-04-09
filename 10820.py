from sys import stdin
strings = stdin.readlines()
for string in strings:
    big = 0
    small = 0
    num = 0
    space = 0
    for n in string:
        if n == '\n':
            continue
        elif n == ' ':
            space += 1
        elif n.isdigit():
            num += 1
        elif n == n.lower():
            small += 1
        elif n == n.upper():
            big += 1
    print(small, big, num, space)