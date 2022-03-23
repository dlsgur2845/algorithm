"""
유형 : 중복 순열

***쿼리로 생성된 모든 단어들을 product연산 하려 했지만 5번 케이스에서 시간초과 발생.
따라서, 한 번 등장한 쿼리와 한 번 이상 등장한 쿼리를 따로 계산.

1. banned_id로 user_id를 찾는건 사실 단어 길이가 길지 않기 때문에 for loop 2번으로 찾을 수 있지만,
   Trie tree를 한번 구현해봄. tree의 삽입, 탐색 시간은 O(L). (L: 쿼리문의 길이)
2. 각 쿼리로 구할 수 있는 단어들을 한 번만 등장한 쿼리와 한 번 이상 등장한 쿼리로 나눠 저장한다.
  2-1. 한 번 등장한 쿼리의 단어들은 case 배열.
  2-2. 한 번 이상 등장한 쿼리의 단어들은 case_dup 배열에 저장.
3. case를 product 후 중복 제거.
  3-1. 이후 case의 모든 원소들 중 길이가 len(case)와 같은 경우만 answer에 1씩 추가
4. case_dup은 모든 원소에 대한 nCr을 answer에 곱해준다. (n: 쿼리로 구한 단어 수, r: 쿼리 등장 횟수)
"""

from collections import defaultdict
from itertools import product

class Node:
    def __init__(self,):
        self.next=defaultdict(list)
        self.words=list()

class Trie:
    def __init__(self,):
        self.first=Node()
        
    def add(self, s):
        return self._add(s, self.first, 0)
    def _add(self, s, node, depth):
        if depth >= len(s):
            node.words.append(s)
            return
        for c in [s[depth], '*']:
            if not c in node.next:
                node.next[c] = Node()
            self._add(s, node.next[c], depth+1)
    
    def find(self, s):
        return self._find(s, self.first, 0)
    def _find(self, s, node, depth):
        if depth >= len(s):
            return node.words
        return self._find(s, node.next[s[depth]], depth+1)

def solution(user_id, banned_id):
    answer = 0
    tree = Trie()
    total=len(banned_id)
    query_cnt = defaultdict(int)
    result=defaultdict(set)
    dupList=[0]
    
    def comb(n, r):
        return fact[n] // fact[n-r] // fact[r]
    
    fact = [1]*9
    for i in range(1, 9):
        fact[i] = fact[i-1]*i

    for user in user_id:
        tree.add(user)

    for user in banned_id:
        query_cnt[user] += 1
        for ban in tree.find(user):
            result[user].add(ban)
    
    case=[]
    case_dup=defaultdict(list)
    for k in result:
        if query_cnt[k] == 1:
            case.append(list(result[k]))
        else:
            total -= query_cnt[k]
            case_dup[k] += list(result[k])
    
    tmp=set()
    for p in product(*case):
        tmp.add(tuple(sorted(set(p))))
    for t in tmp:
        if len(t) == total:
            answer+=1
    
    for k in case_dup:
        answer *= comb(len(case_dup[k]), query_cnt[k])
    
    return answer
