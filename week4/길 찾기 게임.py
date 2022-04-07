"""
유형 : 이진트리, DFS

*python이 아닌 다른 언어라면 런타임 에러를 걱정하지 않아도 되지만 파이썬의 경우
 재귀 1000까지 기본으로 가능하기 때문에 sys의 setrecursionlimit으로 최대 재귀를 늘려줘야한다.
 - 문제에서 트리 깊이가 1000이하인 경우만 입력으로 주어진다해서 편향 트리의 경우 문제 없을 줄 알았는데 런타임에러...
 - 실제 코딩테스트 시험에서 시스템 함수 호출을 해도되는지는 의문...
 
1. y가 높은 값부터 인덱스 번호를 매기며 이진트리에 추가
2. 전위 순회의 경우 현재, left, right 순서대로 탐색
3. 후위 순회의 경우 left, right, 현재 순서대로 탐색
"""

import sys
limit_number = 1006
sys.setrecursionlimit(limit_number)

class Node():
    def __init__(self, x=None):
        self.x=x
        self.left=None
        self.right=None
        
class Tree():
    def __init__(self,):
        self.root=None
        self.pre=[]
        self.post=[]
        
    def add(self, x):
        self._add(self.root, x)
    def _add(self, node, x):
        if node==None:
            self.root=Node(x)
        else:
            if x[0] < node.x[0]:
                if node.left:
                    self._add(node.left, x)
                else:
                    node.left=Node(x)
            else:
                if node.right:
                    self._add(node.right, x)
                else:
                    node.right=Node(x)
                    
    def preorder(self,):
        self._pre(self.root)
    def _pre(self, node):
        if node: self.pre.append(node.x[1])
        if node.left: self._pre(node.left)
        if node.right: self._pre(node.right)
        
    def postorder(self,):
        self._post(self.root)
    def _post(self, node):
        if node.left: self._post(node.left)
        if node.right: self._post(node.right)
        if node: self.post.append(node.x[1])
        

from collections import defaultdict
def solution(nodeinfo):
    d = defaultdict(list)
    
    for i, (x, y) in enumerate(nodeinfo):
        d[y].append((x, i+1))
        d[y].sort()
        
    d = sorted(d.items(), reverse=True)
    tree=Tree()
    for y, nodeList in d:
        for node in nodeList:
            tree.add(node)
    tree.preorder()
    tree.postorder()
    return [tree.pre, tree.post]
