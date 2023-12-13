numberOfInputs=int(input())
list = [x for x in input().split()]
def maximumFrequencyNumbera(list):
    d={}
    li=[]
    maximumFrequency=0
    for x in list:
        d[x]=d.get(x,0)+1
    for h in d:
        if d[h]>maximumFrequency:
            maximumFrequency=d[h]     
    for value in d:
        if d[value]==maximumFrequency:
            li.append(int(value))
    return li,d

maximumFrequency,dict= maximumFrequencyNumbera(list)
print(max(maximumFrequency))