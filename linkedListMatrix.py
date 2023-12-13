class linkedList:
    def __init__(self,data):
        self.data =data
        self.next = None
        self.down = None
n = int(input())
li = [int(x) for x in input().split()]
head = None
rowTail = None
columnTail = None
mainHead = None
for i in range(len(li)):
    if head == None:
        
        newNode = linkedList(li[i])
        mainHead = newNode
        head = newNode
        print(newNode.data,end="->")
    else:
        newNode = linkedList(li[i])
        head.next = newNode
        head = head.next
        print(newNode.data,end="->")
    if i%3==0:
        break
