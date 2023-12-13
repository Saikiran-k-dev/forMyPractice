from sys import stdin,setrecursionlimit
import queue
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans

def maxSumNode(tree):
    actualMaximumSum = 0
    NodeWithMaximumSum = None
    if tree is None:
        return None
    if len(tree.children)==0:
        return tree,tree.data
    q=queue.Queue()
    q.put(tree)
    while not(q.empty()):
        maximumSum=0
        currentNode = q.get()
        maximumSum = currentNode.sum()
        for child in currentNode.children:
            q.put(child)
        if maximumSum>actualMaximumSum:
            actualMaximumSum = maximumSum
            NodeWithMaximumSum = currentNode
    return NodeWithMaximumSum,actualMaximumSum


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
tree = createLevelWiseTree(arr)
temp, tempSum = maxSumNode(tree)
print(temp.data)