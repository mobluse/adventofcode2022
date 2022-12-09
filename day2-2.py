#!/usr/bin/python
# cat day2input.txt | ./day2-2.py
sum = 0
s = input()
while True:
    opponent = chr(ord(s[0])+ord('X')-ord('A'))
    if opponent == 'X':
        correct = 'Y'
        wrong = 'Z'
    elif opponent == 'Y':
        correct = 'Z'
        wrong = 'X'
    elif opponent == 'Z':
        correct = 'X'
        wrong = 'Y'
    outcome = s[2]
    if outcome == 'X':
        response = wrong
    elif outcome == 'Y':
        response = opponent
    elif outcome == 'Z':
        response = correct
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
    if s == '.':
        break
print(sum)
