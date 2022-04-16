import sys
sys.stdin = open('../input.txt', 'r')

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N = int(input())
tree = defaultdict(list)

for _ in range(N):
    A, B, C = input().split()
    tree[A] = [B,C]

inorderList=[]
preorderList=[]
postorderList=[]

def inorder(cur):
    global inorderList
    if cur=='.':
        return
    inorderList.append(cur)
    inorder(tree[cur][0])
    inorder(tree[cur][1])

def preorder(cur):
    global preorderList
    if cur=='.':
        return
    preorder(tree[cur][0])
    preorderList.append(cur)
    preorder(tree[cur][1])

def postorder(cur):
    global postorderList
    if cur=='.':
        return
    postorder(tree[cur][0])
    postorder(tree[cur][1])
    postorderList.append(cur)

inorder('A')
preorder('A')
postorder('A')

print(''.join(inorderList))
print(''.join(preorderList))
print(''.join(postorderList))