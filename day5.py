#!/usr/local/bin/snek
# cat day5input.txt | snek ./day5.py

def find(s, ch, start):
    for i in range(start, len(s)):
        if s[i] == ch:
            return i
    return -1

b = 9
m = []
for i in range(b):
    m += ['']
s = input()
while s[1] != '1':
    for i in range(b):
        if s[4*i+1] != ' ':
            m[i] = s[4*i+1] + m[i]
    s = input()
print(m)

while s != None and s != '':
    s = input()
s = input()
while s != '.':
    print(s)
    i = find(s, 'e', 0)
    n = int(s[i+2:find(s, ' ', i+2)])
    i = find(s, 'm', i)
    f = int(s[i+2:find(s, ' ', i+2)])
    i = find(s, 'o', i)
    t = int(s[i+2:])
    print('%i,%i,%i' % (n, f, t))
    for i in range(n):
        m[t-1] += m[f-1][-1:]
        m[f-1] = m[f-1][:-1]
    print(m)
    s = input()
r = ''
for s in m:
    r += s[-1]
print(r)
