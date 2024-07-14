class productmanagement:
    def __init__(self):
        print("productmanagement")
        self.product=["shirt","watch"]
        self.productrate=[2900,3000000]
        self.productquanity=[1,2]
    def productlisiting(self):
        p=input("enter product name")
        p1=int(input("enter quantity"))
        product=[]
        quantity=[]
        if(p in self.product):
            product.append(p)
            quantity.append(p1)
        print(product,quantity)
     



class user:
    def __init__(self):
        userlist=["uday@gmail.com","uday234@gmai.com"]
        user2=input("enter email")
        if(user2 in userlist):
            print("login")
            object=productmanagement()
            object.productlisiting()

        else:
            print("login denied")
object=user()