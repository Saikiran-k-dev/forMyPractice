from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def reverseStack(inputStack, extraStack) :
	lengthOfStack=len(inputStack)
	for i in range(lengthOfStack):
		if len(inputStack)==1:
			break
		extraStack.append(inputStack.pop())
	for i in range(lengthOfStack-1):
		if len(extraStack)==0:
			break
		inputStack.insert(0,extraStack.pop())
	print(inputStack,emptyStack)
    
'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")