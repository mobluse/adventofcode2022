#!/usr/bin/python
# cat day4input.txt | ./day4.py
def index(s, start, ch):
    for i in range(start, len(s)):
        if s[i] == ch:
            return i

sum = 0
s = input()
while  s != '.':
    i0 = index(s, 0, '-')
    a = int(s[0:i0])
    i0 += 1
    i1 = index(s, i0, ',')
    b = int(s[i0:i1])
    i0 = i1 + 1
    i1 = index(s, i0, '-')
    c = int(s[i0:i1])
    i0 = i1 + 1
    d = int(s[i0:])
    if (a >= c and b <= d) or (c >= a and d <= b) or not(b < c or d < a):
        print('%d-%d,%d-%d' % (a, b, c, d))
        sum += 1
    s = input()
print(sum)
