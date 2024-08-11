def bank():
    amount=5000
    while(True):
        n=int(input("enter 1 for balance\nenter 2 for withdraw\nenter 3 for deposit"))
        if(n==1):
            print(amount)
        elif(n==2):
            print(amount)
            b3=int(input("enter amount"))
            amount=amount-b3
            
        elif(n==3):
            print(amount)
            b5=int(input("enter amount"))
            amount=amount+b5
        else:
            break
