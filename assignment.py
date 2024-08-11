""" import pandas as p

studentinfo={"id":[1,2,3,4,5],
            "name":["user1","user2","user3","user4","user5"],
            "age":[14,12,13,15,16],
            "marks":[56,78,98,38,26],
            "result":["pass","pass","pass","fail","fail"]
            }

f1=p.DataFrame(studentinfo)
print(f1)
 """
""" class userfile:
    def write(self):
        print("write")
        name=input("enter file name")
        file=open(name,"w")
        name1=input("enter name")
        age1=input("enter age")
        class1=input("enter marks")
        marks1=input("enter marks")
        marks2=input("enter marks")
        marks3=input("enter marks")
        marks4=input("enter marks")
        marks5=input("enter marks")
        file.write(name1)
        file.write(age1)
        file.write(class1)
        file.write(marks1)
        file.write(marks2)
        file.write(marks3)
        file.write(marks4)
        file.write(marks5)
        file.close()
    def read(self):
        print("read")
        name=input("enter name")
        file=open(name,"r")
        for i in file:
            print(i)
        file.close()
    def append(Self):
        print("append")
        name=input("enter name")
        file=open(name,"a")
        uname=input("enter name")
        class1=input("enter class")
        age2=input("enter age")
        marks6=int(input("enter number"))
        marks7=int(input("enter number"))
        marks8=int(input("enter number"))
        marks9=int(input("enter number"))
        marks10=int(input("enter number"))
        file.write(uname)
        file.write(age2)
        file.write(class1)
        file.write(marks6)
        file.write(marks7)
        file.write(marks8)
        file.write(marks9)
        file.write(marks10)
        file.close()
object=userfile()

while(True):
    ch=int(input("enter 1 for write/nenter 2 for read/enter 3 for append"))
    if(ch==1):
        object.write()
    elif(ch==2):
        object.read()
    elif(ch==3):
        object.append()
    else:
        break
 """
import bank as b
useremail=["user1@gmail.com","user2@gmail.com"]
userpass=[123,456]
emaillogin=input("enter email")
emailpass=int(input("enter pass"))
for i in range(len(useremail)):
    if(emaillogin == useremail[i]):
        print("enter pass")
        if(emailpass == userpass[i]):
            print("login successful")
            b.bank()
    else:
        print("error 404")

