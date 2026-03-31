
def add(a,b):
    return a+b


c = add(8,7)

print("The sum is == ",c)

#default arguements

def multi(a,b=1):
    return a*b

result = multi(5)
updatedResult = multi(5,2)

print("result with default parameter = ", result)
print("result = ", updatedResult)
