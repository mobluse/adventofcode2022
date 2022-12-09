#!/usr/bin/python
# cat day3input.txt | ./day3-2.py
def find(s1, s2, s3):
    for ch in s1:
        if ch in s2 and ch in s3:
            return ch
    return '?'

sum = 0
a = input()
while  a != '.':
    b = input()
    c = input()
    print(a)
    print(b)
    print(c)
    ch = find(a, b, c)
    base = ord('a')-1 if 'a'<=ch and ch<='z' else ord('A')-27
    priority = ord(ch) - base
    print(ch + str(priority))
    sum += priority
    a = input()
print(sum)
