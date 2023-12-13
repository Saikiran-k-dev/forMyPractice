from curses.ascii import isdigit


li = (int (x) for x in input().split())
print(li)
for i in range(0,len(li)):
    print(li[i])
p=int(input("Enter Which table u need"))
n=int(input("Enter till where u need the table"))
li = [int(x) for x in range(0,n) if x%p==0 if x!=0 ]
print(li)

n=(input())
liInLi=[i for i in n]
print(liInLi)

n=int(input())
jaggedLi=[[int(x) if x.isdigit() else x for x in input().split()] for i in range(n)]
print(jaggedLi)

myChar="saikiran"
reversedMyChar=myChar[len(myChar)::-1]
print(reversedMyChar)