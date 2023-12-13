class stack:
    def __init__(self):
        self.data=[]
    def push(self,element):
        self.element=element
        self.data.append(element)
    def pop(self):
        if self.isStackEmpty():
            return ('stack is empty')
            
        return self.data.pop()
    def top(self):
        if self.isStackEmpty():
            return ('stack is empty')
        return self.data[len(self.data)-1]
    def size(self):
        return len(self.data)
    def isStackEmpty(self):
        if self.size()==0:
            return True
        return False

sai = stack()
sai.push(10)
sai.push(20)
sai.push(30)
while sai.isStackEmpty()==False:
    print(sai.pop())
print(sai.top())
print(sai.size())