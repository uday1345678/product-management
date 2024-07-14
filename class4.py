""" subject1=75
subject2=80
subject3=90
sum=subject1+subject2+subject3
 """
""" print("sum=",sum) """
""" 
subject1=int(input("entersubjectmarks"))
subject2=int(input("entersubjectmarks"))
subject3=int(input("entersubjectmarks"))
sum=subject1+subject2+subject3
print("sum=",sum)
"""




""" Pname1="product1"

Pname2="product2"

Prate1=5000

Prate2=4000

total=Prate1+Prate2

print("Pname1=",Pname1)

print("Pname2=",Pname2)

print("Prate1=",Prate1)

print("Prate2=",Prate2)

print("total=",total)
 """


""" print("Name \t\t Rate")

Pname1="Product1"
Prate1=5000

print(Pname1,"\t",Prate1)

Pname2="Product2"
Prate2=4000

print(Pname2,"\t",Prate2)
print("_________________")
total=Prate1+Prate2

print("total\t",total)
print("______________")
 """


""" name="uday"

print("StudentName:",name)

class1="7th"

print("class1:",class1)

print("subject1\tsubject2")

s1=75
s2=80

print(s1,"\t\t",s2)
 """



""" m=210

if (m>200):
    print("pass")

 """
m=199

if (m>200):
    print("pass")

else:
    print("fail")


""" numb1=int(input("enter first number:"))
if numb1%2==0:
    print("even")
else:
    print("odd")
 """


""" age=int(input("enter age:"))
if age >=18:
    print("vote")
else:
    print("not eligible to vote")
 """



""" numb1=int(input("enter first number:"))
numb2=int(input("enter second number:"))
if numb1>numb2:
    print(numb1)
else:
    print(numb2)
 """



""" numb1=int(input("enter first number:"))
if numb1>20:
    print("too high")
else:
    print("thank you")
 """



""" numb1=int(input("enter first number:"))
if numb1>10 and numb1<20:
    print("thank you")
else:
    print("incorrect answer")
 """


""" colour1=input("enter colour:")
if colour1=="red":
    print("I like red too")
else:
    print("i dont like ",colour1)
 """




""" numb1=int(input("enter first number:"))
if numb1<10:
    print("too low")
elif numb1>10 and numb1<20:
    print ("correct")
else:
    print("too high")
 """


""" age=int(input("enter age:"))
if age>=18:
    print("you can vote")
elif age==17:

    print("you can learn to drive")
elif age ==16:
    print("you can buy a lottery ticket")3

else:
    print("you can go trick or treating")
 """


""" numb1=int(input("enter first number:"))
if numb1==1:
    print("thank you")
elif numb1==2:
    print("well done")
elif numb1==3:
    print("correct")
else:
    print("error message")
 """


""" n=int(input("enter your number"))
i=1
while(i<=10):
    print(i*n)
    i=i+1
 """

n=0
i=10
while(i>=1):
    print(i)
    n=n+i
    i=i-1
print(n)

""" i=1
while(i<=6):
    print("hi")
    i=i+1
 """

""" i=10
while(i<=5):
    print(i)
    i=i-1


 """



""" while(True):
    n=int(input("enter your number"))
    i=int(input("enter your number"))
    print(n*i)
 """

""" 
while(True):
    ch=int(input("enter 1 for add\nenter 2 for subtract\n enter 3 for multiply\nenter 4 for divide "))
    if(ch==1):
        n1=int(input("enter your number"))
        n2=int(input("enter your number"))
        r=n1+n2
        print(r)

    elif(ch==2):
     n1=int(input("enter your number"))
     n2=int(input("enter your number"))
     r=n1-n2
     print(r) 

    elif(ch==3):
        n1=int(input("enter your number"))
        n2=int(input("enter your number"))
        r=n1*n2
        print(r)

    elif(ch==4):
        n1=int(input("enter your number"))
        r=n1/n2
        print(r)

    else:
        break
     """






    
"""     
i=1
while(i<=10):
    if(i==5):
        break
    print(i)
    i=i+1
    
i=1
while(i<=10):
    if(i==5):
        i=i+1
        continue
    print(i)
    i=i+1
 """


""" i=1
while(i<=26):
    print(chr(64+i))
    i=i+1
    
i=26
while(i>=1):
    print(chr(96+i))
    i=i-1
 """
""" n=2
for i in range(1,11):
    print(i*n)
 """
""" for i in range(2,11):
    print(i)

for i in range(11,0,-2):
    print(i)
 """


""" 
for i in range(5):
    for i in range(5):
        print("hi",end="")
    print()

for i in range(5):
    for j in range(5):
        print(j+1,end="")
    print()

for i in range(5):
    for j in range(5):
        print(i+1,end="")
    print()
for i in range(5):
    for j in range(5):
        print(chr(i+65),end="")
    print()
for i in range(5):
    for j in range(5):
        print(chr(j+65),end="")
    print()
for i in range(5):
    for j in range(5):
        print(chr(j+97),end="")
    print()
for i in range(5):
    for j in range(5):
        print(chr(i+97),end="")
    print()
k=0
for i in range(5):
    for j in range(5):
        print(chr(k+97),end="")
        k+=1
    print()
 """






""" for i in range(4,0,-1):
    for j in range(4):
        print(chr(i+64),end="")
    print()
 """



""" name="python"
n=len(name)
print(n)

name="python"
N=str.lower(name)
print(N)
 """
""" name="pyhton"
print(name[1:])
 """
""" k=0
name="python"
for i in range(len(name)):
    if name[i]!="a"or name[i]!="e"or name[i]!="i"or name[i]!="o"or name[i]!="u": 
        print()
    else:
    print(k)
 """
""" c=0
name="python"
for i in range(len(name)):
    if name[i]=="a"or name[i]=="e"or name[i]=="i"or name[i]=="o"or name[i]=="u": 
        print()
    else:
        c+=1
print(c)
 



for i in range(5):
    for j in range(5):
        print(chr(j+97),end="")

"""


""" name="python"
n=len(name)
for i in range(n):
    name[i],name[n-1-i]=name[n-1-i],name[i]
print(name,end="")  """
""" name=[5,9,8,6]
print(name)
n=len(name)
for i in range(n2):
    name[i],name[n-1-i]=name[n-1-i],name[i]
print(name,end="")  
 """
""" name="python"
print(str.swapcase(name))
print(name)

for i in range(len(name),0,-1):
    print(name[i-1],end="")
 """

""" name="python@gmail.com"
print(str.split(name,"")) 
 """

""" data=[5,9,8,4]
print(data[1:4])
 """

""" 
data=[5,9,8,7]
for i in data:
    print(i) """

s=0
data=[5,9,8,7]
for i in data:
    print(i)
    S=S+i
print(s)
















