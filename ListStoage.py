import random as rr
r=""
print("------------------------")
while True:
    # input = rr.randint(1000,9999)
    """    p = open("password.txt","a")
    p.write(str(input)) """
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    
    id += rr.choice(number)
    id += rr.choice(alpha)
    p = open(id,"w")

    if input =="1251":
        print("phone open")
        break