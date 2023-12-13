import sys
import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def leafNodeCount(tree):
    if tree is None:
        return None
    if len(tree.children)==0:
        return 1
    leafNodeCounter=0
    q=queue.Queue()
    q.put(tree)
    while not(q.empty()):
        currentNode = q.get()
        if len(currentNode.children)==0:
            leafNodeCounter+=1
        for child in currentNode.children:
            q.put(child)
    return leafNodeCounter

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
sys.setrecursionlimit(10**6)
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(leafNodeCount(tree))