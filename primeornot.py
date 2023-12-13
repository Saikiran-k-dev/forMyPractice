# def isPrime(n):
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         data.append(n)
# def toCheckPrimeInBetween(n):
#     for i in range(2,n+1):
#         isPrime(i)
# data=[]
# n=int(input())
# toCheckPrimeInBetween(n)
# print(data)

####################################################################3
"""
ncr
n!/r!*n-r!
"""

n=int(input())
r=int(input())
def findingFact(n):
    fact=1
    for  i in range(1,n+1):
        fact=fact*i
    return fact
def calculatingFact(n,r):
    n_fact=findingFact(n)
    r_fact=findingFact(r)
    n_r_fact=findingFact(n-r)
    ncr=n_fact//r_fact*n_r_fact
    return ncr

ncr=calculatingFact(n,r)
print(ncr)
