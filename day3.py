#!/usr/local/bin/snek
# cat day3input.txt | snek ./day3.py
def common(s1, s2):
    for ch in s1:
        if ch in s2:
            return ch
    return '?'

sum = 0
s = input()
while  s != '.':
    a = s[:len(s)//2]
    b = s[len(s)//2:]
    print(a + ' ' + b)
    ch = common(a, b)
    base = (ord('A')-27, ord('a')-1)['a' <= ch <= 'z']
    priority = ord(ch) - base
    print(ch + str(priority))
    sum += priority
    s = input()
print(sum)
