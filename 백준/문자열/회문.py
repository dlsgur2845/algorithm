import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda:sys.stdin.readline().rstrip()

def chance2(x):
    l, r = 0, len(x)-1
    while l<r:
        if x[l]==x[r]:
            l+=1
            r-=1
        else:
            return False
    return True

def palin(x):
    l, r= 0, len(x)-1
    while l<r:
        if x[l]==x[r]:
            l+=1
            r-=1
        else:
            if any([chance2(x[l+1:r+1]), chance2(x[l:r])]):
                return 1
            else:
                return 2
    return 0

for _ in range(int(input())):
    s = input()
    print(palin(s))