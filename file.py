class userfile:
    def write(self):
        print("write")
        name=input("enter file name")
        file=open(name,"w")
        name1=input("enter name")
        age=input("enter age")
        class1=input("enter class")
        file.write(name1)
        file.write(age)
        file.write(class1)
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
        file.write(uname)
        file.write(age2)
        file.write(class1)
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


a=int(input("enter number"))
if(a<0):
    print("negative")
else:
    print("positive")