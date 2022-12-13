#!/usr/local/bin/snek
# cat day6input.txt day6input.txt | snek ./day6.py

start = time.monotonic()
n = 4
s = input()
print(len(s))
for i in range(n-1, len(s)):
    if (
        s[i-0] != s[i-1] and
        s[i-0] != s[i-2] and
        s[i-0] != s[i-3] and
        s[i-1] != s[i-2] and
        s[i-1] != s[i-3] and
        s[i-2] != s[i-3]
                            ):
        print(i+1)
        break
input()

n = 14
s = input()
print(len(s))
for i in range(n-1, len(s)):
    if (
        s[i-0] != s[i-1] and
        s[i-0] != s[i-2] and
        s[i-0] != s[i-3] and
        s[i-0] != s[i-4] and
        s[i-0] != s[i-5] and
        s[i-0] != s[i-6] and
        s[i-0] != s[i-7] and
        s[i-0] != s[i-8] and
        s[i-0] != s[i-9] and
        s[i-0] != s[i-10] and
        s[i-0] != s[i-11] and
        s[i-0] != s[i-12] and
        s[i-0] != s[i-13] and
        s[i-1] != s[i-2] and
        s[i-1] != s[i-3] and
        s[i-1] != s[i-4] and
        s[i-1] != s[i-5] and
        s[i-1] != s[i-6] and
        s[i-1] != s[i-7] and
        s[i-1] != s[i-8] and
        s[i-1] != s[i-9] and
        s[i-1] != s[i-10] and
        s[i-1] != s[i-11] and
        s[i-1] != s[i-12] and
        s[i-1] != s[i-13] and
        s[i-2] != s[i-3] and
        s[i-2] != s[i-4] and
        s[i-2] != s[i-5] and
        s[i-2] != s[i-6] and
        s[i-2] != s[i-7] and
        s[i-2] != s[i-8] and
        s[i-2] != s[i-9] and
        s[i-2] != s[i-10] and
        s[i-2] != s[i-11] and
        s[i-2] != s[i-12] and
        s[i-2] != s[i-13] and
        s[i-3] != s[i-4] and
        s[i-3] != s[i-5] and
        s[i-3] != s[i-6] and
        s[i-3] != s[i-7] and
        s[i-3] != s[i-8] and
        s[i-3] != s[i-9] and
        s[i-3] != s[i-10] and
        s[i-3] != s[i-11] and
        s[i-3] != s[i-12] and
        s[i-3] != s[i-13] and
        s[i-4] != s[i-5] and
        s[i-4] != s[i-6] and
        s[i-4] != s[i-7] and
        s[i-4] != s[i-8] and
        s[i-4] != s[i-9] and
        s[i-4] != s[i-10] and
        s[i-4] != s[i-11] and
        s[i-4] != s[i-12] and
        s[i-4] != s[i-13] and
        s[i-5] != s[i-6] and
        s[i-5] != s[i-7] and
        s[i-5] != s[i-8] and
        s[i-5] != s[i-9] and
        s[i-5] != s[i-10] and
        s[i-5] != s[i-11] and
        s[i-5] != s[i-12] and
        s[i-5] != s[i-13] and
        s[i-6] != s[i-7] and
        s[i-6] != s[i-8] and
        s[i-6] != s[i-9] and
        s[i-6] != s[i-10] and
        s[i-6] != s[i-11] and
        s[i-6] != s[i-12] and
        s[i-6] != s[i-13] and
        s[i-7] != s[i-8] and
        s[i-7] != s[i-9] and
        s[i-7] != s[i-10] and
        s[i-7] != s[i-11] and
        s[i-7] != s[i-12] and
        s[i-7] != s[i-13] and
        s[i-8] != s[i-9] and
        s[i-8] != s[i-10] and
        s[i-8] != s[i-11] and
        s[i-8] != s[i-12] and
        s[i-8] != s[i-13] and
        s[i-9] != s[i-10] and
        s[i-9] != s[i-11] and
        s[i-9] != s[i-12] and
        s[i-9] != s[i-13] and
        s[i-10] != s[i-11] and
        s[i-10] != s[i-12] and
        s[i-10] != s[i-13] and
        s[i-11] != s[i-12] and
        s[i-11] != s[i-13] and
        s[i-12] != s[i-13]
                              ):
        print(i+1)
        break
input()
print('%f s' % time.monotonic()-start)
