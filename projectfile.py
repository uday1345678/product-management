""" class UserFile:
    def Write(self):
        print("write")
        name = input("enter file name")
        file = open(name,"w")
        uname = input("enter name")
        file.write(uname)
        file.close()

    def Read(self):
        print("read")
        name = input("enter file name")
        file=open(name,"r")
        for i in file:
            print(i)
    def Append(self):
        print("Append")
        name = input("enter file name")
        file = open(name,"a")
        uname = input("enter name")
        file.write(uname)
        file.close()


objfile = UserFile()
while(True):
    n=int(input("1 for write\n2 for read\n3 for append"))
    if n==1:
        objfile.Write()
    elif n==2:
        objfile.Read()
    elif n==3:
        objfile.Append()
    else:
        break


 """
class UserFile:
    def Write(self):
        print("write")
        name = input("enter file name")
        file = open(name,"w")
        class1=input("enter class")
        section1=input("enter section")
        age=input("enter age")
        uname = input("enter name")
        file.write(uname)
        file.write(class1)
        file.write(section1)
        file.write(age)
        file.close()

    def Read(self):
        print("read")
        name = input("enter file name")
        file=open(name,"r")
        for i in file:
            print(i)
    def Append(self):
        print("Append")
        name = input("enter file name")
        file = open(name,"a")
        age =input("enter age")
        class1 =input("enter class")
        section1 =input("enter section")
        uname = input("enter name")
        file.write(uname)
        file.write(class1)
        file.write(section1)
        file.write(age)
        file.close()
        

objfile = UserFile()
while(True):
    n=int(input("1 for write\n2 for read\n3 for append"))
    if n==1:
        objfile.Write()
    elif n==2:
        objfile.Read()
    elif n==3:
        objfile.Append()
    else:
        break
