import sys
import queue

class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.children = list()

def inputLevelWise(li) :
    i = 0
    data = li[i] 
    i += 1
    if data == -1 :
        return None
    root = TreeNode(data) 
    q = queue.Queue()
    q.put(root)
    while (not q.empty()) :
        frontNode = q.get()
        noOfChildren = li[i]
        i += 1
        childrenArray = li[i : i+noOfChildren]
        for childData in childrenArray :
            childNode = TreeNode(childData)
            frontNode.children.append(childNode)
            q.put(childNode)
        i = i+noOfChildren
    return root
        
def sumOfAllNodes(root):
    if root is None:
        return 0
    
    total_sum = 0
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        current_node = q.get()
        total_sum += current_node.data
        
        for child in current_node.children:
            q.put(child)
    
    return total_sum

#main
sys.setrecursionlimit(10**6)
li = [int(elem) for elem in list(input().strip().split())]
root = inputLevelWise(li)
print(sumOfAllNodes(root))