
userNum = int(input("Please enter your number atleast 2 digit : "))

'''sum = 0
b = 0
while userNum>0:
    b = userNum % 10
    sum = (sum*10) + b
    userNum = userNum//10'''

result = int(str(userNum)[::-1])

print("The reverse is : ", result)