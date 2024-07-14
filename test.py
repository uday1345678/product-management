""" n1=1234
n1=n1%10
print(n1)

n1=1234
n1=n1//10
print(n1)

n1=5
n1=2+3
print(n1)

n1=2
n2=3
add=n1+n2
print(add,"=",n1,"+",n2)
 """

""" n1=5
n2=3
r=n1>n2
print(r,"=",n1,">",n2)
 """

""" n1=5
r=n1%2
print(r)
 """
""" i=1
while(True):
    if(i==4):
        break
    print("hi")
    i=i+2
 """


""" s=0
n1=123
r=n1%10
s=s+r
n1=n1//10
r=n1%10
s=s+r
n1=n1//10
r=n1%10
s=s+r
print(s)
 

 
n1=5
n2=4
r1=n1>n2
r2=n1<n2
r3=r1 and r2
print(r3,"=",r1,"and",r2)


n1=5
n2=4
r1=n1>n2
r2=n1<n2
r3=r1 or r2
print(r3,"=",r1,"or",r2)
 """ 


""" email="admin@gmail.com"
if (email=="admin@gmail.com"):
    password=input("enter password")
    if(password=="admin"):
        print("login")
    else:
        print("not login") 
else:
    print("write email")
 """
""" s=0
for i in range(1,21,1):
    if (i%2==0):
        s=s+i
    print(s)
 """
 
""" 
i=1
while(i<=5):
    print("hello")
    i=i+1
     """
""" 
i=1
while(i>=1):
        print(i)
        i=i-1


i=1
while(i<=5):
        j=1
while(j<=5):
        print("*",end="")
        j=j+1  
        print()
        i=i+1
 """
""" 
for i in range(1,5):
    for j in range(1,5):
        print(chr(96+j),end="")
    print()

i=1
while(i<=5):
    j=1
    while(j<=5):
        print(j,end="")
        j=j+1
    i=i+1
    print() """



""" for i in range(1,5):
    n1=7
    print(n1)
    n2=9
    print(n2)
    print("hi")
 """


""" i=1
while(i<=5):
     j=1
     while(j<=5):
          print(chr(64+j),end="")
          j=j+1
    
     print()
     i=i+1
 """

""" 
for i in range(1,5):

    for j in range(1,5):
        print(chr(97+j),end="")
    
    
    print()
     """
""" data=[5,4,3,5]
if(data[3]%2==0):
    print("even")
else:
    print("odd")
 """
""" n1=5
data. append(n1)
print(data)


n2=4
data. append(n2)
print(data)


n3=10
data. append(n3)
print(data)
data.pop()
print(data)
data.pop()
print(data)
data.pop()
print(data)
data.pop()
print(data)
 """
""" 
data=[5,9,4,7,6,3]
datae=[]
datao=[]
print(len(data))
n=len(data)
for i in range(n):
    if(data[i]%2==0):
         print("even=>",data[i])
         datae.append(data[i])
    else:
         datao.append(data[i])
 """
""" 
print(datae)
print(max(datae))
print(min(datae))
print(sum(datae))
s1=sum(datae)

print(datao)
print(sum(datao))

s2=sum(datao)
print(max(datao))
print(min(datao))

if(s1>=s2):
     print(s1)
else:
     print(s2)
 """
""" 
data=[5,9,4,6,7,3]
datae=[]
datao=[]
print(len(data))
n=len(data)
if(data[0]%2==0):
     print("even")
else:
     print("odd")


for i in range(n):
     if(data[i]%2==0):
          print("even=>",data[i])
else:
     data.append
         
print(max(data))
print(min(data))
print(sum(data))

 """
""" datae=[]
datao=[]
data=[2,3,6,5,7,4]
n= len(data)
for i in range(n):
    if(data[i]%2==0):
        datae.append(data[i])
    else:
        datao.append(data[i])

print(datae)
print(datao)    

se=sum(datae)
so=sum(datao)
if(se>so):
    print(se)
else:
    print(so)
   """  













""" 
datae=[]
datao=[]
data=[5,4,7,2,8]
n=len(data)
for i in range(n):
    if(data[i]%2==0):
          datae.append(data[i])
    else:
         datao.append(data[i])

se=(sum(datae))
so=(sum(datao))
if(se>so):
     print(so)
else:
     print(se)
     
s1=max(datae)
s2=max(datao)
if(s1>s2):
     print(s1)
else:
     print(s2) """

""" data=[5,4,3,6,7]
datae=[]
datao=[]
n=len(data)
for i in range(n):
    if(data[i]%2==0):
     datae.append(data[i])
    else:
        datao.append(data[i])
print(datae)
print(datao)
 """

""" list1=[]
n=59236
while(n!=0):
    r=n%10
    list1.append(r)
    n=n//10
print(list1)
 """ 

""" data1=["uday","uday1","uday3"]
data2=[60,63,52,32]
data3=["uday@gmail.com","uday4@gmail.com"]
print(data1)
print(data2)
print(data3)
n=(input("enter your email"))
if(n in data3):
    print("yes")
else:
    print("decline")

 """    

""" data12=[5,6,2,8,9]
print(data12)
f=int(input("enter your number"))
if(f in data12):
    print("thank you")
else:
    data12.append(f)
    print("number entered")
print(data12)
 """

""" n=0
data1=[5,9,7,2,4]
i=0
while(i<n//2):
 """     

""" data=[5,6,4,7,3]
datae=[]
datao=[]
n=len(data)
for i in range(n):
    if(data[i]%2==0):
        datae.append(data[i])
    else:
        datao.append(data[i])
print(datae)
print(datao)

so=max(data)
se=max(data)
if(se>so):
  print(se)
else:
    print(so)
 """
""" data1=[5,7,2,9,1]
f=int(input("enter your number")
if(f in data1):
    print("thank you")
else:
    data1.append(f)
    print("number added")
    print(data1)
     """

""" data2=[]
n=59340
while(n!=0):
    r=n%10
    data2.append(r)
    n=n//10
print(data2)
 """

""" data=[3,4,8,9,5]
n=len(data)
for i in rangen//2)(:
    data[i],data[n-1-i]=data[n-1-i],data[i]
print(data)
 """

""" data=[5,9,3,7]
item=7
index=2
data.insert(index,item)
print(data)

data.pop()
print(data)
data.remove(5)
print(data)
 """

""" max1=0
list1=[5,6,8,2]
for i in list1:
    if(i>max1):
        max1=i
print(max1)
 """












""" max1=0
list1=[5,9,8,3]
for i in list1:
    if(i>max1):
        max1=i
print(max1) """




""" list2=[5,3,7,6]
min1=list1[0]
for i in list2:
    if(i<min1):
        min1=i
print(min1)
 """

""" list3=[5,3,6,3,9]
print(list3)
print(" >4 and <7")
for i in list3:
    if(i>4 and i<7):
         print(i)
 """


""" while(True):
    f=int(input("enter your number"))
    g=int(input("enter your number"))
    if(f%2==0 and g%2==0):
        r=f+g
        print(r)
        break
 """    
  
""" 
data1={'id':'5','name':'uday','class':'7'}
print(data1)
print(data1['name'])
data1['age']=18
print(data1)
data1.pop('name')
print(data1)


for i in data1.values():
    print(i)

for i in data1.keys():
    print(i)
 """


""" for i in data1:
    print(i)
 """

""" key=input("enter your key")
value=input("enter your value")
data1.update({key:value})
print(data1)
 """

""" data=[
    [5,4,7,2,9],
    [6,3,8,10]
]
print(data)

for i in range(len(data)):
    for j in data[i]:
        print(j,end="")
    print()
row1=int(input("enter row"))
col1=int(input("enter col"))
print(data[row1][col1])
f=data[row1]
v=int(input("enter your number"))
f.append(v)
print(f)
c=int(input("enter your column"))
print(f[c])
n=int(input("enter your number"))
f[c]=n
print(f)

 """


""" student={
          "A":{"id":82,"name":"u"},
          "B":{"id1":35,"name1":"u1"} 
}
print(student)
for i in student:
   
    print(i,student[i])
 """


""" data=[1,1,1,1]
while(len(data)):
    print(data)
 """

""" data=(5,9,7,8)
n=data.count(9)
print(n)

dn1=data.index(9)
print(dn1)
 """
""" data[0] =9

print(data) """
""" data1 =[2,3,4]
data1[0]=9

print(data1)
 """
""" print(data)

for i in data:
    print(i)

 """""" 
for i in range(len(data)):
    print(data[i])
     """

""" 
data={5,9,8,8}

print(data)
data.add(7)
print(data)
data.pop()
print(data)


data.remove(9)
print(data)

d=data.copy()
data.clear()

print(data) """
#print(data[0])

""" for i in data:
    print(i) """
""" 
for i in range(len(data)):
    print(data[i]) """

""" 
name="python@gmail.com"
print(str.split(name,"@")) 

#name="python"
print(str.lower(name))
print(name)
n=str.replace(name,"@","#")
n=str.find(name,"o")
print(n)
 """

""" n="python@gmail.com"
n1=str.(n,"@gmail.com")
print(n1)
 """


""" n1="python@gmail.com" """
# n2=n1.count("o")
# print(n2) 
""" print(n1)
n3=list(n1)
print(n3) """


""" for i in n3:
    print(i,end="")
    if(i=="@"):
    """         
""" n=len(n3)
for i in range(n):
    
    if(n3[i]=="p"):
        for j in range(i,n-1):
            n3[j]=n3[j+1]
        
print(n3) """
""" n3=list(input("enter string"))
r=input("enter character")

n=len(n3)
for i in range(n):
    
    if(n3[i]==r):
        for j in range(i,n-1):
            n3[j]=n3[j+1]
        
print(n3) 
 """

""" n1=input("enter gmail")
n2=(list(n1))
print(n2)
 """

""" name="python"
l=list(name)
n=len(l)
for i in range(n//2):
    l[i],l[n-i-1]=l[n-1-i],l[i]
print(l)
 """


""" def add():
    n1=5
    n2=4
    r=n1+n2
    print(r)


def subtract():
    n1=5
    n2=4
    r=n1-n2
    print(r)

add()
subtract()
 """

""" def countingprint():
    for i in range(1,11):
        print(i)
countingprint()

def printstring():
    n1=int(input("enter number"))
    print(n1)
printstring()    
 """
""" def area():
    radius=int(input("enter radius"))
    a=3.14*radius*radius
    print(a)
#area()

def multiply():
    i=1
    m=2
    while(i<=10):
        print(i*m)
        i=i+1
multiply()

def divide():
    d1=int(input("enter number"))
    d2=int(input("enter number"))
    r=d1/d2
    print(r)
divide()

def areaofrectangle():
    length=int(input("enter your number"))
    breadth=int(input("enter your number"))
    n5=length*breadth
    print(n5)
areaofrectangle()
"""

""" def areaofcircle():
    radius=int(input("enter radius"))
    n6=3.14*32*32
    print(n6)
areaofcircle()
 """

""" def diameterofcircle():
    radius=int(input("enter radius"))
    n8=radius//2
    print(n8)
diameterofcircle()
 """

""" def radiusofscircle():
    diameter=int(input("enter diameter"))
    r=diameter*2
    print(r)


def perimeterofsquare():
    side=int(input("enter side"))
    p1=4*side    
    print(p1)
perimeterofsquare()
 """

""" def perimeterofrectangle():
    length=int(input("enter length"))
    breadth=int(input("enter breadth"))
    p2=2*(length+breadth)
    print(p2)
perimeterofrectangle()
 """

""" def areaofsquare():
    side=int(input("enter side"))
    a1=side*side
    print(a1)
areaofsquare()
 """

""" def lengthofrectangle():
    breadth=int(input("enter breadth"))
    areaofrectangle=int(input("enter area"))
    l1=areaofrectangle//breadth
    print(l1)
lengthofrectangle()
 """

""" def breadthofrectangle():
    length=int(input("enter length"))
    areaofrectangle=int(input("enter area"))
    b1=areaofrectangle//length
    print(b1)
breadthofrectangle()
 """

""" def sidesofsquare():
    perimeter=int(input("enter perimeter"))
    p3=perimeter/4
    print(p3)
sidesofsquare()
 """


""" def sidesofsquare():
    areaofsquare=int(input("enter area"))
    a4=areaofsquare/areaofsquare
sidesofsquare()
 """
