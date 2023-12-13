import sys
import queue
sys.setrecursionlimit(3000)
from sys import stdin
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def maxDataNode(tree):
    
     if tree is None:
         return 0
     largestNumber=0
     q=queue.Queue()
     q.put(tree)
     while not q.empty():
         currentNode = q.get()
         if currentNode.data>largestNumber:
             largestNumber = currentNode.data
         for child in currentNode.children:
             q.put(child)
     return largestNumber
def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
tree = createLevelWiseTree(arr)
print(maxDataNode(tree))