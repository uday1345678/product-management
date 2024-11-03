import random as r
def  ranfun():
    n=r.randint(1,6)
    print(n)
    return n
count=0
p1=0
p2=0
def player1():
    print("player1",end="")
    global p1
    rr=ranfun()
    p1=p1+rr
    if rr==6:
         player1()
def player2():
    print("player2 ",end="")
    global p2
    rr=ranfun()
    p2=p2+rr
    if rr==6:
         player2()

    
while(True):
        if(count==20):
                break
        elif(count%2==0):
            input()
            player1()
        elif(count%2==1):
            input()
            player2()
      
            
        count+=1
if (p1>p2):
    print("winner is p1",p1)
else:
    print("p2 is winner",p2)

i=1
while(i<=10):
     print(i)
     i=i+1