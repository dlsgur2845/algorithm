from collections import Counter, defaultdict
from heapq import heappush, heappop

class Node():
    def __init__(self, freq:int, char:chr=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanTree():
    def __init__(self, text:str):
        self.text = text
        self.root = self.HuffmanCoding()
        self.code = defaultdict(str)

        self.getCode(self.root, '')

    def HuffmanCoding(self):
        counter = Counter(self.text)
        heap = []
        for key, cnt in counter.items():
            heappush(heap, Node(cnt, key))

        while len(heap)>1:
            right = heappop(heap)
            left = heappop(heap)
            newNode = Node(right.freq+left.freq, left=left, right=right)
            heappush(heap, newNode)

        return heappop(heap)

    def getCode(self, node, code):
        if not node:
            return
        else:
            if node.char:
                self.code[node.char] = code[:]
            self.getCode(node.left, code+'0')
            self.getCode(node.right, code+'1')

def getText(n=10):
    import random
    return ''.join([chr(ord('A')+random.randint(0, 25)) for _ in range(n)])

text = getText(100)
text += 'AAAAAAAAAABBCCD'
tree = HuffmanTree(text)
text_hf = ''.join([tree.code[key] for key in text])
text_hf = ''.join([chr(int(text_hf[i:i+7], 2)) for i in range(0, len(text_hf), 7)])

print(text)
print(text_hf)