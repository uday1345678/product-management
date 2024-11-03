""" a1=int(input("enter number"))
b1=int(input("enter number"))
c1=int(input("enter number"))
if a1>b1 and a1>c1:
    print(a1)
elif b1>c1:
    print(b1)
else:
    print(c1)
    

 """





""" 
a1=input("enter number or alphabet")

if a1>='A' and a1<='Z' or a1>='a' and a1<='z':
    print("alphabet")

elif ord(a1)>=48 and ord(a1)<=57:
    print("number") 

else:
    print("special character ")
 """

""" i1=2
i=1
while(i<=10):
     print(i*i1)
     i=i+1
     """""" 
sum=0
i=1
while(i<=10):
    if(i%2!=0):
    
        sum+=i
    i=i+1
print(sum)
 """


""" i=1
while(i<=26):
    print(chr(i+64))
    i=i+1
  """   
""" i=1
while(i<=26):
    print(chr(i+96))
    i=i+1
 """

""" subject1marks=int(input("enter marks"))
subject2marks=int(input("enter marks"))
subject3marks=int(input("enter marks"))
subject4marks=int(input("enter marks"))
subject5marks=int(input("enter marks"))
f1=subject1marks+subject2marks+subject3marks+subject4marks+subject5marks
if f1>=400:
    print("grade a")
elif f1>=300:
    print("grade b") 
else:
    print("grade c")
 """

list1=[12,15,18,20]
m1=list1[0]
for i in list1:
    if m1<i:
        m1=i
print(m1)


