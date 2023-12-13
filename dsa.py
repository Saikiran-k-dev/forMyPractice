# Factorial of a number
from asyncore import loop
from pickle import TRUE
import string
print('enter to check the  factorial of the number',end=" ")
n = int(input())
fact = 1
for i in range(1, n+1):
    fact = fact * i  
    i += 1
print(f"factorial of the number {n} is {fact}")

#print all the even numbers
n=10
even=[]
for i in range(1,n+1):
    if i%2 == 0:
        even.append(i)
    i+=1
print(f"even numbers are {even}")

#check if number is prime or not
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def print_primes(n):
    primes = []
    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
    print("Prime numbers up to", n, "are:")
    print(primes)
print_primes(100)

# simple intrest 
p=100
t=2
r=12
si = (p*t*r)//100
print(f" Value of simple intrest is {si}")

# farnhite to celcius
f=100
c=(f-32)*5//9
print(f" celcius value is {c}")

# calculating simple intrest using user input 
p=input()
t=int(input()) #changing the datatype while taking input
r=input()
si = (int(p)*t*int(r))//100
print(f" Value of simple intrest is {si}")


# ______________________________________________________________________________________________
# Conditions and loops 
a = True
if not(a):
    print("i am inside if")
else:
    print("i am in else")
b = True
if b:
    print('i am inside if')
else:
    print('i am in else')

# To check if the given input is odd or even
print('Enter the value to check if the number is odd or even : ', end=" ")
a = int(input())
if a%2==0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

# Logical operators (and or and not)
a=5
b=5
c=5
if a==b and b==c:
    print("they are all same")
else:
    print('one of them is wrong')
if a==b or b!=c:
    print('it is true')
else:
    print('it is false')
if not(a!=b):
    print('this will print')
else:
    print('this wont print')

# now well join elif statement in the code 
a=12
b=25
c=25
if a==b and a>c:
    print(f"both a and b are greater")
elif a>b and a>c:
    print('a is greater')
elif a>b and a==c:
    print('both a and c are greater')
elif b>a and b>c:
    print('b is greater')
elif b==c and b>a:
    print('both c and b are greater')
else:
    print('c is greater')

# To check of the list of given numbers prime or not
print("enter the numbers range to check whether its prime or not")
n = int(input())
i = 2
data = []
while i<=n:
    flag = False
    div=2
    while div<i:
        if(i%div==0):
            flag = True
        div = div+1
    if not(flag):
        data.append(i)
    i = i+1
print(data)

# Caluculator Program using while loop

while True:
    n = int(input())
    if n == 1:
        val1 = int(input())
        val2 = int(input())
        print(val1+val2)
    if n == 2:
        val1 = int(input())
        val2 = int(input())
        print(val1-val2)
    if n == 3:
        val1 = int(input())
        val2 = int(input())
        print(val1*val2)
    if n == 4:
        val1 = int(input())
        val2 = int(input())
        print(val1//val2)
    if n == 5:
        val1 = int(input())
        val2 = int(input())
        print(val1%val2)
    if n == 6 or n>=8:
        break
    if n == 7:
        print('invalid operation')

# Reversing the number 
num = int(input())
reversed = 0
while num>0:
    digit = num%10
    reversed = (reversed*10)+digit
    num = num//10

print(reversed)

# To check if thee given number is palindrome or not NOTE FUNCTION ONLY RETURNS  TRUE OR FALSE VALUES 
num = int(input())
def isPalindrome():
    print(num)
    original_num = num
    reverse_num = 0

    while num > 0:
        digit = num % 10
        reverse_num = (reverse_num * 10) + digit
        num = num // 10
    return original_num == reverse_num
if isPalindrome():
    print('The given number is a palindrome')
else:
    print('The given number is not a palindrome')

# Add all even numbers and odd numbers in the given string 
num = int(input())
even = 0
odd = 0
def addevenodd():
    global num,even,odd
    while num > 0:
        digit = num%10
        if digit%2==0:
            even+=digit
        else:
            odd+=digit
        num = num//10
    print(even,odd)
addevenodd()

# To check the fibonacci series 
n = int(input())
fibonacci = 0
a, b = 1, 1

if n == 1 or n == 2:
    fibonacci = 1
else:
    count = 3
    while count <= n:
        fibonacci = a + b
        a, b = b, fibonacci
        count += 1

print(fibonacci)

# Caluculating ncr 
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
