""" class userfile:
    def write1(self):
        print("write")
        name=input("enter file name")
        file=(name,"w")
        uname1=input("enter name")
        age=input("enter age")
        class1=input("enter class")
        file.write(uname1)
        file.write(age)
        file.write(class1)
        file.close()
    def read(self):
        print("read")
        name=input("enter file name")
        file=(name,"r")
        for i in range:
            print(i)
        file.close()
    def append(self):
        print("Append")
        name=input("enter file name")
        file=(name,"a")
        uname=input("enter name")
        age=input("enter age")
        class1=input("enter class")
        file.write(uname)
        file.write(age)
        file.write(class1)
        file.close()
object=userfile()

while(True):
    ch=int(input("enter 1 for write/nenter 2 for read/n enter 3 for append"))
    if ch==1:
            object.write1()
    elif ch==2:
        object.read()
    elif ch==3:
        object.append()
    else:
        break
 """




import pandas as ps
school={"id":[1,2,3],"subjectname":["science","Maths","computer"],"examdate":["1.8.24","28.9.24","30.8.24"],"marks":[19,20,18]}
f1=ps.DataFrame(school)
f2=sum(school["marks"])
print(f1)
print(f2)



