import sys
sys.stdin = open('../input.txt', 'r')

import sys
sys.setrecursionlimit(10**5)

def postorder(arr):
    length = len(arr)
    if length<=1:
        return arr
    for i in range(1, length):
        if arr[i]>arr[0]:
            return postorder(arr[1:i]) + postorder(arr[i:]) + [arr[0]]
    return postorder(arr[1:])+[arr[0]]

pre = []
while True:
    try:
        x = int(sys.stdin.readline().rstrip())
        pre.append(x)
    except:
        break
for n in postorder(pre):
    print(n)