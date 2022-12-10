#!/usr/local/bin/snek
# cat day1input.txt | snek ./day1.py
high1 = -1000
high2 = -2000
high3 = -3000
sum = 0
s = input()
while True:
    if s == None or s == '' or s == '.':
        if sum > high1:
            high3 = high2
            high2 = high1
            high1 = sum
        sum = 0
    else:
        sum += int(s)
    if s == '.':
        break
    s = input()
print(high1)
print(high1+high2+high3)
