class node:
    def __init__(self,data):
        self.data=data
        self.head=None

class stack:
    def __init__(self):
        self.head=None
        self.count=0
    def size(self):
        return self.count
    def isEmpty(self):
        return self.size()==0
    def push(self,data):
        newNode=node(data)
        newNode.next=self.head
        self.head=newNode
        self.count=self.count+1
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        data=self.head.data
        self.head=self.head.next
        self.count=self.count-1
        return data
    def top(self):
        if self.isEmpty():
            return "stack is empty"
        data = self.head.data
        return data
    
s=stack()
s.push(10)
print(s.top())
s.pop()
print(s.top())