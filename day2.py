#!/usr/local/bin/snek
# cat day2input.txt | ./day2.py
sum = 0
s = input()
while s != '.':
    opponent = chr(ord(s[0])+ord('X')-ord('A'))
    if opponent == 'X':
        correct = 'Y'
    elif opponent == 'Y':
        correct = 'Z'
    elif opponent == 'Z':
        correct = 'X'
    response = s[2]
    if response == 'X':
        shape = 1
    elif response == 'Y':
        shape = 2
    elif response == 'Z':
        shape = 3
    print(shape)
    if response == correct:
        score = 6
    elif response == opponent:
        score = 3
    else:
        score = 0
    print(score)
    sum += shape + score
    s = input()
print(sum)
