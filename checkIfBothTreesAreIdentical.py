from sys import stdin,setrecursionlimit
import queue
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(tree1, tree2):
    if tree1 is None or tree2 is None:
        return False
    q=queue.Queue()
    q2=queue.Queue()
    q.put(tree1)
    q2.put(tree2)
    while not(q.empty()) or not(q2.empty()):
        currentNode,currenNode2 = q.get(),q2.get()
        
        if currentNode.data!=currenNode2.data:
            return False
        for child in currentNode.children:
            q.put(child)
        for child in currenNode2.children:
            q2.put(child)
    return True  

    pass





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
arr1 = list(int(x) for x in stdin.readline().strip().split())
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in stdin.readline().strip().split())
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')