""" class Profile:
    def __init__(self,data):
        print(data)




class User:
    def __init__(self):
        self.info=[
            {"id":1,"name":"user1","age":30,"salary":4000},
            {"id":2,"name":"user2","age":32,"salary":5000},
            {"id":3,"name":"user3","age":34,"salary":6000}
        ]
    def UserAdd(self):
        u = input("enter name")
        age=int(input("enter age"))
        salary=int(input("enter salary"))
        self.info.append({"id":3,"name":u,"age":age,"salary":salary})
    def UserPrint(self):
        print(self.info)
    def UserLogin(self):
        u = input("enter name")
        for i in self.info:
            if u==i["name"]:
                print("login")
                p = Profile(i)
                break
        else: 
            print("not login")

user = User()
user.UserAdd()
user.UserPrint()
user.UserLogin()       
 """

""" class profile:
   def __init__(self,data):
      print(data)
      
   

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
       

        
class userFile:
    def userWrite(self):
        #file=open("filename","mode") # W write a append r read  mode(w,a,r)
        f= input("enter file name")
        file =open(f,"w")
        name = input("enter name")
        file.write(name)
        file.close()
    def useRead(self):
        f= input("enter file name")
        file=open(f,"r")
        for i in file:
            print(i) 
    def userAppend(self):
        f = input("file name")
        file=open(f,"a")
        name = input("enter name")
        file.write(name)

user = userFile()
user.userWrite()
user.useRead()
user.userAppend()
