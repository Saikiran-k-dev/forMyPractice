import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    if len(lst)==0:
        return
    middle = lst[len(lst)//2]
    print(middle)
    middleLeft = lst[0:len(lst)//2]
    print(middleLeft)
    middleLeftNode = middleLeft[len(middleLeft)//2]
    print(middleLeftNode)
    middleRight = lst[len(lst)//2+1:len(lst)]
    print(middleRight)
    middleRightNode = middleRight[len(middleRight)//2]
    print(middleRightNode)
    root = BinaryTreeNode(middle)
    root.left = BinaryTreeNode(middleLeftNode)
    root.right = BinaryTreeNode(middleRightNode)
    constructBST(middleLeft)
    constructBST(middleRight)
    pass
    

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root=constructBST(lst)
preOrder(root)