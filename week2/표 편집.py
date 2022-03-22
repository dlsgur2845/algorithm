"""
유형 : index 접근 가능한 가능한 linked list

*** 여태껏 풀었던 문제중에 가장 어려웠음, (정답 코드 참조함)
*** U, D의 최대 이동이 100만 cmd가 20만이라 순차 접근하면 안될줄 알았지만, 제한사항에 cmd의 모든 x 합은 100만 이하...

1. linked list 개념이 들어가지만 인덱스로 한 번에 접근 가능한 구조여야한다.
2. 삭제된 파일을 관리하는 stack이 필요함.
3. 'U', 'D'는 linked list의 인덱스 이동 연산과 같음
4. 'C'의 경우
  4-1. 'C'의 경우 데이터를 실제로 pop 하는게 아닌 양 옆의 링크를 끊어준다.
  4-2. stack에 현재 값을 넣고 현재 데이터가 왼쪽 끝인지, 오른쪽 끝인지, 그외인지에 따라 링크를 다르게 끊어줌.
  4-3. 현재 값의 우측 노드가 배열 밖이라면 즉, 현재 노드가 list에서 남아있는 마지막인지 확인
    4-3-1. 마지막이라면,        k = 현재 값의 왼쪽 노드
    4-3-2. 마지막이 아니라면,   k = 현재 값의 오른쪽 노드
5. 'Z'의 경우
  5-1. stack의 top에 있는 값을 꺼내어 원래 위치가 왼쪽 끝인지, 오른쪽 끝인지, 그 외인지에 따라 링크를 다르게 연결.
"""

def solution(n, k, cmd):
    arr = {i:[i-1, i+1] for i in range(n)}
    alive = ['O']*n
    stack = []
    
    for c in cmd:
        c = c.split()
        
        if c[0] == 'U':
            for _ in range(int(c[1])):
                k = arr[k][0]
        elif c[0] == 'D':
            for _ in range(int(c[1])):
                k = arr[k][1]
        elif c[0] == 'C':
            left, right = arr[k]
            alive[k]='X'
            stack.append(k)
            
            if left == -1:
                arr[right][0] = left
            elif right == n:
                arr[left][1] = right
            else:
                arr[right][0] = left
                arr[left][1] = right
            
            if right == n:
                k = left
            else:
                k = right
                
        elif c[0] == 'Z':
            cur = stack.pop()
            alive[cur]='O'
            left, right = arr[cur]
            
            if left == -1:
                arr[right][0] = cur
            elif right == n:
                arr[left][1] = cur
            else:
                arr[right][0] = cur
                arr[left][1] = cur
        
    return ''.join(alive)
