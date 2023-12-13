## Read input as specified in the question.
## Print output as specified in the question.
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkCousins(root,p,q):
    if root is None:
        return None
    q=queue.Queue()
    q.put(root)
    while not(q.empty()):
        currentNode = q.get()
        q.put(currentNode.left)
        q.put(currentNode.right)
        print(currentNode.data,currentNode.left.data,currentNode.right.data)
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
p = int(input())
q = int(input())
ans = checkCousins(root,p,q)
if ans is True:
    print('true')
else:
    print('false')
