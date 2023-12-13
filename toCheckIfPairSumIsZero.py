from sys import stdin

def pairSum0(l,n):
    k=l
    numberOfPairSum = 0
    for i in l:
        for j in k:
            if i+j==0:
                numberOfPairSum+=1
    print(numberOfPairSum)
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))