from sys import stdin

def isBalanced(expression):
    data=[]
    for i in range(len(expression)):
        try:
            if expression[i]=='(':
                data.append('(')
            if expression[i]==')':
                data.remove('(')
        except ValueError:
            data.append(expression[i])

    if len(data)==0:
        return True
    else:
        return False
expression = stdin.readline().strip()
# print(expression)
if isBalanced(expression):
    print('true')
else:
    print('fslse')
