import queue

class binaryTree:
    def __init__(self,data):
        self.data = data
        self.left =  None
        self.right = None

def binaryTreeFun():
    rootData = int(input("Enter the root data:"))
    q=queue.Queue()
    if rootData == -1:
        return None
    root = binaryTree(rootData)
    q.put(root)
    while not(q.empty()):
        currentNode = q.get()
        leftNodeData = int(input(f"Enter the left child of {currentNode.data}:"))
        if leftNodeData != -1:
            leftNode = binaryTree(leftNodeData)
            currentNode.left = leftNode
            q.put(leftNode)
        rightNodeData = int(input(f"Enter the right child of {currentNode.data}:"))
        if rightNodeData != -1:
            rightNode = binaryTree(rightNodeData)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

def printBinaryTreeLevelWise(root):
    if root == None:
        return -1
    q=queue.Queue()
    q.put(root)
    while not(q.empty()):
        currentNode = q.get()
        print(currentNode.data,end=":")
        if currentNode.left is not None:
            print(f"L:{currentNode.left.data}",end=",")
            q.put(currentNode.left)
        if currentNode.right is not None:
            print(f"R:{currentNode.right.data}",end="")
            q.put(currentNode.right)
        print()
root = binaryTreeFun()
call = printBinaryTreeLevelWise(root)