import random as r
def randfun():
    n= r.randint(1,6)
    print(n)

    return n
p1=0
p2=0
count=0
def player1():
    print("player 1")
    v= randfun()
    global p1
    p1+=v
    
    if v==6:
        player1()

def player2():
    print("player 2")
    v= randfun()
    global p2
    p2+=v
    if v==6:
        player2()


while True:
    if count==20:
        break
    elif count%2==0:
        input()
        player1()
    elif count%2==1:
        input()
        player2()
    
    count+=1


if(p1>p2):
    print("p1",p1)
else:
    print("p2",p2)