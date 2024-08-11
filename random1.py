import random as r
def  ranfun():
    n=r.randint(1,6)
    print(n)
    return n
count=0
p1=0
p2=0
def player1():
    print("player1")
    global p1
    p1=p1+ranfun()
def player2():
    print("player2")
    global p2
    p2=p2+ranfun()
while(True):
        if(count==20):
                break
        elif(count%2==0):
            player1()
        elif(count%2==1):
            player2()
        
            
        count+=1
if (p1>p2):
    print("winner is p1",p1)
else:
    print("p2 is winner",p2)
