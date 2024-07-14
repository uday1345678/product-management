userdata=[]
class creditcard:
    def creditcard(self):
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


class user:
    def login(self):
        name=input("enter name")
        if (name in userdata):
            print("login successful")
            object=creditcard()
            object.creditcard()
        else:
            print("login failed")
    def register(self):
        email=input("enter email")
        userdata.append(email)
        print(userdata)
        self.login()
object=user()


class teacher:
    def teacher(self):
        print("teacher")
        
class student:
    def student(self):
        print("student")


class studentmngmnt:
    def studentmngmnt(self):
        while(True):
            print("studentmngmnt")
            n2=int(input("enter 1 for teacher/nenter2 for student/n enter 3 for studentmngmnt"))
            if (n2==1):
                t=teacher()
                t.teacher()
            elif(n2==2):    
                s=student()
                s.student()
        
        
object=studentmngmnt()
object.studentmngmnt()



