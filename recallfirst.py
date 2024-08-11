""" for i in range(11):
    print(i)

for i in range(11,0,-2):
    print(i)

for i in range(0,11,2):
    print(i)

for i in range(2,22,2):
    print(i)

n=4
for i in range(1,11):
    print(i*n) 


for i in range(1,11):
    i=i+1
    print(i)


for i in range(1,11):
    print()
print("hi")


for i in range(10,0,-1):
    print()
print("hello")

for i in range(10,0,-2):
    print()
print("python")
 """

""" i=1
while(i<=26):
    print(chr(i+64))
    i=i+1

i=1
while(i<=26):
    print(chr(i+97))
    i=i+1  
 """
""" i=5
while(i<=10):
    if (i==5):
        i=i+1
        continue
    print(i)
    i=i+1
 """


while(True):
    ch=int(input("enter 1 for add\n enter 2 for subtract\n enter 3 for multiply\n enter 4 for divide"))
    if(ch==1):
        n1=int(input("enter your number"))
        n2=int(input("enter your number"))
        r=n1+n2
        print(r)
    elif(ch==2):
        n3=int(input("enter your number"))
        n4=int(input("enter your number"))
        r1=n3-n4

        print(r1)
    elif(ch==3):
        n5=int(input("enter your number"))
        n6=int(input("enter your number"))
        r2=n5*n6
        print(r2)
    elif(ch==4):
     n7=int(input("enter your number"))
     n8=int(input("enter your number"))
     r3=n7/n8
     print(r3)

    else:
        break
 
""" n=0
i=1
while(i<=10):
        n=n+i 
        i=i+1
print(n)
 """
""" s=0
i=1 
while(i<=10):
  if(i%2==0):
    s=s+1
print(s)
  
  


class User:
    def __init__(self):
      self.info=[
            {"age":5,"name":"u","salary":23000},
            {"age":6,"name":"n","salary":34000},
            {"age":7,"name":"m","salary":70000}
             ]
    def useradd(self):
        k=input("enter name")
        a=int(input("enter age"))
        l=int(input("enter salary"))
        self.info.append({"age":a,"name":k,"salary":l})
    def userprint(self):
       print(self.info)
    def userlogin(self):
        u=input("enter name")
        for i in self.info:
           if u==i["name"]:
            p=profile(i)
            print("login")
            break
        else:
           ("login denied")
    def payment(self):
        sum1=0
        for i in self.info:
            sum1+=i["salary"]
        print("total payment=>",sum1)
user = User()
user.useradd()
user.userprint()
user.payment()
user.userlogin()       
 """





