
from sys import stdin


def pairSum(arr, n, x) :
    arr1=[]
    for i in range(len(arr)):
        arr1.append(arr[i])
    countingNumberOfTimes = 0
    for i in arr:
        arr1.remove(i)
        for j in arr1:
            if i+j==x:
                countingNumberOfTimes+=1
    return countingNumberOfTimes

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))

    t -= 1