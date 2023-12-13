class mapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class map:
    def __init__(self):
        self.bucketSize = 10
        self.buckets=[None for i in range(self.bucketSize)]
        self.count = 0
    
    def size(self):
        return self.count
    def getBucketIndex(self,hc):
        return(abs(hc)%(self.bucketSize))
    def remove(self,key):
        hc = hash (key) #Getting hashcode
        index= self.getBucketIndex(hc) #Finding index corresponding to hc
        head = self.buckets[index] #Finding head pointer
        prev= None
        while head is not None:
            if head.key == key:#If found
                if prev is None: #Removing
                    self.buckets[index] = head.next
                else:
                    prev.next= head.next
                self.count-=1
                return head.value
            prev =head
            head =head.next
        return None
    def getValue(self,key):
        hc  = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        print(head)
        while head is not None:
            if head.key == key:
                return head.value 
            head = head.next
        return None
    def insert(self,key,value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        head = self.buckets[index]
        newNode = mapNode(key,value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count+=1
m = map()
m.insert('parikh',2)
m.insert('sai','hello')
m.remove('sai')
# print(m.size())
print(m.getValue('parikh'))