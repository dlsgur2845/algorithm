"""
유형 : 구현

1. 'I' 면 배열에 추가, 'D 1'이면 최대 값 삭제, 'D -1'이면 최소 값 삭제

통과했지만 개인적으로 이 문제 테스트 케이스가 너무 빈약한것 같음.
operations의 최대가 1,000,000이라 Insert 500,000번된 배열에 Delete 500,000번 발생하면 최악의 경우 시간초과가 발생해야함.
그래서 O(N logN) 을 생각해보려했지만 실패.

solution_list : 1차원 배열로 구현 - O(N**2)
solution_heap : max heap, min heap 두개를 동기화 - O(N**2),
  - 동기화 후 heapify를 해주지 않으면 heap 구조 파괴
  ["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"] 경우 [7, 4]가 나오지 않음.
solution_linked : 링크드 리스트에 삽입 위치 이진 탐색 O(N logN) 으로 구현하려했으나 링크드 리스트는
                  인덱스 찾는데만 O(N)라서 안될 것 같음.

"""

def solution_list(operations):
    answer = []
    
    for op in operations:
        op, n = op.split(' ')
        
        if op == 'I':
            answer.append(int(n))
        elif answer:
            if n == '1':
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))
                
    return [max(answer), min(answer)] if answer else [0, 0]



from heapq import heappush, heappop, heapify

def solution_heap(operations):
    max_heap=[]
    min_heap=[]

    for op in operations:
        op, n = op.split(' ')
        
        if op == 'I':
            heappush(max_heap, -int(n))
            heappush(min_heap, int(n))
        elif max_heap:
            if n == '1':
                n = heappop(max_heap)
                min_heap.remove(-n)
                heapify(min_heap)
            else:
                n = heappop(min_heap)
                max_heap.remove(-n)
                heapify(max_heap)

    return [-max_heap[0], min_heap[0]] if min_heap else [0, 0]
