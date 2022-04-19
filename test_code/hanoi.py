class Node:
    def __init__(self, name, stack):
        self.name = name
        self.stack = stack

A = Node('A', [3, 2, 1])
B = Node('B', [])
C = Node('C', [])

def hanoi(n, a, b, c):
    if n < 1:
        return
    hanoi(n - 1, a, c, b)
    print(f'{n}:{a.name}{a.stack}->{c.name}{c.stack}')
    c.stack.append(a.stack.pop())
    hanoi(n - 1, b, a, c)

hanoi(3, A, B, C)
print('\n',A.stack, B.stack, C.stack)