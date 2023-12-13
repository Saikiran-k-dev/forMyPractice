from sys import stdin,setrecursionlimit
import queue
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(tree, n):
    if tree is None:
        return None
    q=queue.Queue()
    q.put(tree)
    while not(q.empty()):
        currentNode = q.get()
        if currentNode.data>n:
            return currentNode
        for child in currentNode.children:
            q.put(child)
    





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
arr = list(int(x) for x in stdin.readline().strip().split())
n = int(input())
tree = createLevelWiseTree(arr)
if nextLargest(tree, n):
    print(nextLargest(tree, n).data)