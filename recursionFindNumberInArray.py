def checkNumber(arr, x):
    arrayLength=len(arr)
    if arrayLength==0 or arrayLength ==1:
            return True
    print(arr)
    checkNumber(arr[1:],x)
    
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
