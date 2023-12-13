
def uniqueChar(s): 
    d={}
    returnedString = ""
    for char in s:
        if char in d:
            d[char]+=1
        else:
            d[char]=1
    for key in d:
        returnedString+=key
    return returnedString





# Main 
s=input() 
print(uniqueChar(s))