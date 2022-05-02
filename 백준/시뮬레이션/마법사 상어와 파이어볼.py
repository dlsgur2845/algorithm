import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda:sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
fireList = []
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireList.append([r-1, c-1, m, s, d])

mr, mc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    tmpList=[]
    for r, c, m, s, d in fireList:
        _r = (r + mr[d]*s) % N
        _c = (c + mc[d]*s) % N

        tmpList.append([_r, _c, m, s, d])
    fireList = sorted(tmpList)

    tmpList=[]
    while fireList:
        cnt=1
        fire = fireList.pop()
        sameDir = True
        while fireList and fire[:2]==fireList[-1][:2]:
            tmp = fireList.pop()
            fire[2] += tmp[2] # m
            fire[3] += tmp[3] # s
            if fire[4]%2 != tmp[4]%2:
                sameDir=False
            cnt+=1
        if cnt<=1:
            tmpList.append(fire)
            continue

        fire[2] //= 5
        fire[3] //= cnt

        if fire[2]>0:
            nextDir = [0, 2, 4, 6] if sameDir else [1, 3, 5, 7]
            for i in range(4):
                tmpList.append(fire[:4]+[nextDir[i]])
    fireList = tmpList

print(sum([m for _,_,m,_,_ in fireList]))