""" data={id:5}
name=["uday"]
password=[54521]
data.update({"name1":name})
print(data)

data.update({"password1":password})
print(data)
 """
""" n3=18
if (n3==18):
    print("true")
else:
    print("false")
  """   

""" def add(n1,n2):
    r=n1+n2
    print(r)
add(5,4)
 """

""" def loop(start,end):
    for i in range(start,end):
        print(i)

def table(s,e,t):
    for i in range(s,e):
        print(i*t)
table(1,11,2)

def table():
    s=1
    e=11
    t=2
    for i in range(s,e):
        print(i*t)
table()


def max():
    n1=3
    n2=4
    if (n1>n2):
        print(n1)
    else:
        print(n2)
max()

def max(n1,n2):
    if(n1>n2):
        print(n1)
    else:
        print(n2)
max(5,4)

def sumofloop():
    sum=0
    for i in range(1,11):
        sum+=i
        print(sum)
sumofloop()

def sumofloop(s,e):
    sum=0
    for i in range(s,e):
        sum=sum+i
        print(sum)
sumofloop(1,11)
 """
""" def sumofevennumbers():
    n1=1
    sum=0
    while(n1<11):
        if (n1%2==0):
            sum=sum+n1
        n1+=1
    print(sum)
sumofevennumbers()

list=[1,2,3,4,5]
def printlist(list):
    for i in range(len(list)):
        print(list[i],end="\t")
printlist(list)
 """
        
""" dictionary={"id":4,"age":12}
def printdictionary(dictionary):
    for i in dictionary.values():
        print(i)
printdictionary(dictionary)

dictionary1={}
def addkeysandvalues(dictionary1):
    dictionary2={"id":4,"age":14}
    dictionary1.update(dictionary2)
    print(dictionary1)
addkeysandvalues(dictionary1)
 """


""" def add(): with return (default)
    n1=5
    n2=4
    r=n1+n2
    return r
k=add()
print(k)
 """

""" def add(n1,n2): with return (argument)
    r=n1+n2
    return r
k=add(9,8)
print(k)
 """

""" def add():
    n1=2
    n2=4
    r=n1+n2
    print(r)
add()

def subtract(n1,n2):
    r=n1-n2
    print(r)
subtract(9,2)
 """

""" def multiply():
    n1=2
    n2=4
    r=n1*n2
    return r
k=multiply()
print(k)
 """

""" def divide(n1,n2):
    r=n1/n2
    return r
m=divide(10,5)
print(m)
 """

""" def factorial():
    f=1
    n=6
    while(n>=1):
        f=f*n
        n=n-1
    print(f)
factorial()
   """  

""" def factorial():
    n1=1
    n2=7
    while(n2>=1):
        n1=n1*n2
        n2=n2-1
    return n1
k=factorial()
print(k)
 """

def factorial(n1,n2):
    while(n2>=1):
        n1=n1*n2
        n2=n2-1
    return n1
k=factorial(1,9)
print(k)

""" def student():
    dictionary={"id":23,"name":123}
    information(dictionary)
def information(dictionary):
    print(dictionary)
student()
 """
def bank():
    amount=2900
    print(amount)
    while (True):
        n=int(input("enter 1 for balance\nenter 2 for deposit\nenter 3 for withdraw\n"))
        if(n==1):
            print(amount)
        elif(n==2):
            
            b2 =int(input("enter amount"))
           
            
            amount=amount+b2
            
            print(amount)
        elif(n==3):

            c3=int(input("enter amount"))
            if c3<=amount:
                amount=amount-c3
            else:

                print("insufficient balance")
        else:
            break
def user():
    data=["uday@gmail.com","uday20@gmail.com"]
    f1=input("enter gmail")
    if (f1 in data):
        print("login")
        bank()
    else:
        ("login failed")
user()
 

""" def bank():
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
bank()
 """
""" def shoppingcard():
    productname=[]
    productrate=[]

    while(True):
        n=int(input("enter 1 for shopping"))
        if(n==1):
            p=input("enter product name")
            r=int(input("enter product rate"))
            productname.append(p)
            productrate.append(r)
        else:
            break
    print(productname)
    print(productrate)
    print("total amount",sum(productrate))
    amount=int(input("enter payment"))
    if(amount==sum(productrate)):
        print("payment successful")
    else:
        print("payment failed")
shoppingcard()
 """

""" def creditcard():
    amount=7000
    while(True):
        n=int(input("enter 1 for balance/nenter 2 for withdraw/nenter 3 for deposit"))
        if(n==1):
            print(amount)
        elif(n==2):
            w1=int(input("enter amount"))
            r=amount-w1
            print(r)
        elif(n==3):
            d1=int(input("enter amount"))
            r1=amount+d1
            print(r1)
        else:
            break

list=[]
def login():
    n=input("enter name")
    if (n in list):
        print("login successful")
        while(True):
            c=int(input("logout press 1"))
            if c==1:
                break
            creditcard()
    else:
        print("login unsuccessful")
    
def register():
    n1=input("enter name")
    list.append(n1)
    login()
register()
 """
userdata=[]
class user:
    def login(self):
        name=input("enter name")
        if (name in userdata):
            print("login")
        else:
            print("login unsuccessful")
    def register(self):
        email=input("enter email")
        userdata.append(email)
        print(userdata)
        self.login()
        
object=user()
object.register()


