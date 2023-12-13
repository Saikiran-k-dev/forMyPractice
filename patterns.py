# Printing * square pattern 
"""
****
****
****
****
"""
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
print('###################################################')

#printing number pattern
"""
1111
1111
1111
1111
"""
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print("1",end="")
    print()
print('###################################################')
"""
1111
2222
3333
4444
"""
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()
print('###################################################')
"""
1234
1234
1234
1234
"""
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()
print('###################################################')

"""
1234
5678
9101112
13141516
"""
n=5
p=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(p,end=",")
        p+=1
    print()
print('###################################################')

"""
4321
4321
4321
4321
"""
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n-j+1,end="")
    print()
print('###################################################')

"""
AAAA
BBBB
CCCC
DDDD
"""
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        charp = (chr(ord('A')+i-1))
        print(charp,end="")
    print()
print('###################################################')

"""
ABCD
ABCD
ABCD
ABCD
"""
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        charp = (chr(ord('A')+j-1))
        print(charp,end="")
    print()
print('###################################################')

"""
ABCD
EFGH
IJKL
MNOP
"""
n=5
p=1
for i in range(1,n+1):  
    for j in range(1,n+1):
        charp=(chr(ord('A')+p-1))
        print(charp,end="")
        p+=1
    print()
    
print('###################################################')

"""
ABCD
BCDE
CDEF
DEFG
"""
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        charp=(chr(ord('A')+i-1+j-1))
        print(charp,end="")
    print()
print('###################################################')
"""
DDDD
CCCC
BBBB
AAAA
"""
n=4
for i in range(1,n+1):
    for j in range(1,j+1):
        charp=(chr(ord('A')+n-i))
        print(charp,end="")
    print()
print('###################################################')
"""
DCBA
DCBA
DCBA
DCBA
"""
n=4
for i in range(1,n+1):
    for j in range(1,j+1):
        charp=(chr(ord('A')+n-j))
        print(charp,end="")
    print()
print('###################################################')
"""
1111
222
33
4
"""
n=4
for i in range(1,n+1):
    for j in range(1,n+1-i+1):
        print(i,end="")
    print()
print('###################################################')