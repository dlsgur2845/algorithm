import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()

A = set([chr(ord('a')+i) for i in range(26)])
B = set(['a', 'e', 'i', 'o', 'u'])
A -= B

while True:
    s = input()
    if s=='end':
        break

    acceptable=True
    if len(set(s)-A) == 0:
        acceptable=False
    else:
        if len(s)>=3:
            for a, b, c in zip(s, s[1:], s[2:]):
                if (a in A and b in A and c in A) or (a in B and b in B and c in B):
                    acceptable=False
                    break
            else:
                if len(s)>=2:
                    for a, b in zip(s, s[1:]):
                        if a==b and a not in ['e', 'o']:
                            acceptable=False
                            break
    print((f'<{s}> is ') + ('acceptable.' if acceptable else 'not acceptable.'))