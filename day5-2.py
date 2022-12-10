#!/usr/local/bin/snek
# cat day5input.txt | snek ./day5-2.py

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
    i = find(s, 'e', 0) + 2
    n = int(s[i:find(s, ' ', i)])
    i = find(s, 'm', i) + 2
    f = int(s[i:find(s, ' ', i)])
    i = find(s, 'o', i) + 2
    t = int(s[i:])
    print('%i,%i,%i' % (n, f, t))
    f -= 1
    m[t-1] += m[f][-n:]
    m[f] = m[f][:-n]
    print(m)
    s = input()
r = ''
for s in m:
    r += s[-1]
print(r)
