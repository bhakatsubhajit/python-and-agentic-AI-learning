firstNum = input("Enter your first number :")
secondNum = input("Enter your second number :")

add = int(firstNum) + int(secondNum)
sub = int(firstNum) - int(secondNum)
multi = int(firstNum) * int(secondNum)
div = int(firstNum) / int(secondNum)
quo = int(firstNum) // int(secondNum) # special div operator in python that results in integer

print(" Results are : \n " + 
      " Sum : " + str(add) + "\n"
      " Difference : " + str(sub) + "\n"
      " Product : " + str(multi) + "\n"
      " Division : " + str(div) + "\n"
      " Quotient : " + str(quo) + "\n"
        )