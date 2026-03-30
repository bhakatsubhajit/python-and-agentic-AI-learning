
num = int(input("Enter your 3 digit number= "))

match num:
    case 200:
        print("You won an amazon voucher!!!")
    case 300 :   
        print("You won an treat voucher!!!") 
    case 500:
        print("You won Rs-500!!!")    
    case _:
        print("better luck next time")