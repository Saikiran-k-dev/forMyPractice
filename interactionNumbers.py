import sys

def intersections(arr1, n, arr2, m) :
    #Your code goes here
    li =[]
    for ele in arr1:
        #if ele in li:
        #    break
        for ele1 in arr2:
            if ele1 == ele:
                li.append(ele)
                arr2.remove(ele1)
                #break
                print(ele,end=' ')
                break
    print()

    # return int(arr3[0]),int(arr3[1]),int(arr3[2])























#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()
    t -= 1