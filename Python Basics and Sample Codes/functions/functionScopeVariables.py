p = 20 # p is a global variable.
def sum(a,b):
    result = a+b
    print(p)
    return result
# a and b are local variables, they are only accessible within the function 'sum'.

print(sum(5,10))
# print(result) # This will raise an error because 'result' is a local variable and cannot be accessed outside the function.

# how to make update the value of a global variable inside a function?

def updatepVal():
    global p 
    p= 2
    return p
print(updatepVal())