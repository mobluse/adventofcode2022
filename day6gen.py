#!/usr/local/bin/snek

def generate(n):
    for i in range(0, n):
        for j in range(i+1, n):
            print(' '*8+'s[i-%d] != s[i-%d] and' % (i, j))
    print()

generate(4)
generate(14)
