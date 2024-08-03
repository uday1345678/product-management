class userfile:
    def write(self):
        print("write")
        name =input("enter file name")
        file = open(name,"w")
        age=input("enter age")
        class1=input("enter class")
        section1=input("enter section")
        uname=input("enter name")
        file.write(age)
        file.write(section1)
        file.write(uname)
        file.write(class1)
        file.close()
    def read(self):
        print("read")
        name=input("enter file name")
        file=open(name,"r")
        for i in file:
            print(i)
    def Append(self):
        print("Append")
        name =input("enter file name")
        file = open(name,"a")
        age=input("enter age")
        class1=input("enter class")
        section1=input("enter section")
        uname=input("enter name")
        file.write(age)
        file.write(section1)
        file.write(uname)
        file.write(class1)
        file.close()

objfile=userfile()

while(True):
    ch=int(input("enter 1 for write/n enter 2 for read /n enter 3 for Append"))
    if ch==1:
        objfile.write()
    elif ch==2:
        objfile.read()
    elif ch==3:
        objfile.Append()
    else:
        break

