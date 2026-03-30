luckyNum = int(input("Enter your lucky number: "))

match luckyNum:
       case 1:
              printf("you won a mobile")
       case 3:
              printf("you won 300$")
       case 5:
              print("you won a certification voucher")
       case _ :
              print("Better luck next time")



