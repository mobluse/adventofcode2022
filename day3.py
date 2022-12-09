#!/usr/bin/python
# cat day3input.txt | ./day3.py
def find(s1, s2):
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
    ch = find(a, b)
    base = ord('a')-1 if 'a'<=ch and ch<='z' else  ord('A')-27
    priority = ord(ch) - base
    print(ch + str(priority))
    sum += priority
    s = input()
print(sum)
