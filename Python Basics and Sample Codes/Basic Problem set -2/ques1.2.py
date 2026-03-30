userNum = int(input("please enter your number:"))

if userNum < 0 :
    print("Invalid input negative number")
else:
    if userNum % 2 == 0:
        print("your input is an even number")
    else:
        print("your input is odd number")
    
