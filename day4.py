#!/usr/local/bin/snek
# cat day4input.txt | ./day4.py
def instr(start, s, ch):
    for i in range(start, len(s)):
        if s[i] == ch:
            return i
    return -1

sum = 0
s = input()
while  s != '.':
    i0 = instr(0, s, '-')
    a = int(s[0:i0])
    i0 += 1
    i1 = instr(i0, s, ',')
    b = int(s[i0:i1])
    i0 = i1 + 1
    i1 = instr(i0, s, '-')
    c = int(s[i0:i1])
    i0 = i1 + 1
    d = int(s[i0:])
    if a >= c and b <= d or c >= a and d <= b:
        print('%d-%d,%d-%d' % (a, b, c, d))
        sum += 1
    s = input()
print(sum)
