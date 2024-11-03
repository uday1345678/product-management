""" import pandas

studentinfo=[
            {"name":"uday","age":14,"class1":9},
            {"name":"uday2","age":15,"class1":10}
            ]

p1=pandas.DataFrame(studentinfo)
print(p1)
print(p1['name'])
print(p1['age'])
print(p1['class1'])

 """
""" 
import pandas as pd

studentinfo=[
            {"name":"uday","age":14,"class1":9},
            {"name":"uday2","age":15,"class1":10}
            ]

p1=pd.DataFrame(studentinfo)
print(p1)
print(p1['name'])
print(p1['age'])
print(p1['class1']) """
""" 
import pandas as pd

name=["user1","user2","user3"]
age=[19,20,23]

p1=pd.Series([name,age],index=["name","age"])
print(p1) """
""" 
import pandas as pd

name=["user1","user2","user3"]
age=[19,20,23]
 """
""" f =pd.DataFrame([name,age])
print(f)


f1 =pd.DataFrame([name,age],index=["name","age"])

print(f1)
 """
""" f1 =pd.DataFrame([name,age],index=["name","age"],columns=["N1","N2","N3"])

print(f1)
 """

""" import numpy as np
num =[1,2,3,4,5] """
""" 
f = np.sin(num)
print(f)
f = np.cos(num)
print(f)
f = np.tan(num)
print(f) """
""" f =np.sum(num)
print(f)
 """


""" 
class Info:
    def data(self):
        
        rate=90

        return rate 
    def time(self):
        time=0
        return time
class Bank(Info):
    def __init__(self) :
        p=1000
        try:
            s=p*self.data()/self.time()
            print(s)
        except:
            print("except")
        
bank = Bank() """

""" from tkinter import *

root =Tk()
root.geometry("300x400")
name = Label(text="Enter name")
name.place(x=20,y=20)

nameinput = Entry()
nameinput.place(x=120,y=20)

lastname = Label(text="Last Name")
lastname.place(x=20,y=50)
lastnameinput=Entry()
lastnameinput.place(x=120,y=50)
email=Label(text="enter email")
pass1=Label(text="enter password")
email.place(x=20,y=120)
pass1.place(x=20,y=140)
emailinput= Entry()
pass1input=Entry()
emailinput.place(x=120,y=120)
pass1input.place(x=120,y=140)
button=Button(text="submit")
button.place(x=160,y=180)
root.mainloop() """













"""
from tkinter import *
root= Tk()
root.geometry("500x600")
firstname= Label(text="enter first name")
firstname.place(x=20,y=20)
lastname=Label(text="enter last name")
lastname.place(x=20,y=40)
firstname1=Entry()
lastname1=Entry()
firstname1.place(x=120,y=20)
lastname1.place(x=120,y=40)
button=Button()
button= Button(text="submit")
button.place(x=120,y=90)
root.mainloop()

"""

""" def areaofcircle():
    radius=12
    pie=3.14
    area=pie*radius*radius
    print(area)
areaofcircle()
 """

""" firstname=input("enter first name")
lastname=input("enter last name")
r1=lastname+ " "+firstname
print(r1)
 """


""" colourlist1=["red","green","white","black"]
print(colourlist1[0])
print(colourlist1[-1])
 """

""" 
def examdatesheet():
    date=input("enter date")
    month=input("enter month")
    year=input("enter year")
    print(date+"/"+month+"/"+year)
examdatesheet()
 """

""" def calculate(n1,n2,n3):
    if n1==n2==n3:
        r1=n1+n2+n3
        r2=r1*3
        return r2
f vowel():
    character=input("enter letter")
    if character=='a'or character=='e' or character=='i' or character=='o'or character=='u':
        print("character is a vowel")
    else:
        print("not a vowel")
vowel()    else:
        r1=n1+n2+n3
        return r1
n1=12
n2=12
n3=12
v=calculate(n1,n2,n3)
print(v)
 """
"""  """
""" def calculate(r1,r2,r3):
    if r1==r2 or r2==r3 or r1==r3:
        return 0
    else:
        r4=r1+r2+r3
        return r4
r1=1
r2=2
r3=123
v=calculate(r1,r2,r3)
print(v) """

""" list=["uday","singh"]
print(list) """

""" while(True):
    list1=[1,2,3,4]
    print(list1)
     """
""" 
list1=[1,2,3]
n=len(list1)
for i in list1:
    print(i) """
""" list1=[1,2,3,4]
n=len(list1)
i=0
s=0
while(i<n):
    if list1[i]%2==0:
        """  """
        s=s+list1[i]
        
    i=i+1
print(s)
 """
""" m=1
list1=[1,2,3,4]
for i in list1:
    if i%2==0:
        m=m*i
print(m)
n=max(list1)
print(n)
n1=min(list1)
print(n1)
n2=len(lisAt1)

 """
 
""" list1=["abc","xyzx","xya","aba","121","121","ads"]
m1=len(list1)
print(m1)
count=0
for i in list1:
        if i[0]==i[-1]:
            count+=1    

print(count)
 """

""" list1=[]
n1=len(list1)
if n1>0:
    print("list is not empty")
else:
    print("list is empty")
 """
list1=[1,4,2,3,4,5,6,3,7]
n=len(list1)
for i in range(n):
    j=i+1
    while(j<n):
        if list1[i]==list1[j]:
            list1[j]=list1[j+1]
            n=n-1
            j=j-1
        j=j+1
       
for i in range(n):
    print(list1[i])


