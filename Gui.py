from tkinter import *
root= Tk()
inp1=0
inp2=0
r=0
def show(value):
    print(value)
    if(value=="+"):
        global inp1
        inp1=input1.get()
        input1.delete(0,END)
    elif value=="x":
        global inp1
        inp1=input1.get()
        input1.delete(0,END)
        

    elif value=="=":
        global inp2
        inp2=input1.get()
        input1.delete(0,END)
        global r
        r= int(inp1) + int(inp2)
        input1.insert(END,r)
    else:

        input1.insert(END,value)
root.geometry("500x600")
input= Label(text="Title")
input.place(x=120,y=20/.jytrewA)
input1=Entry()
input1.place(x=120,y=40)
button1= Button(text="1",command=lambda:show("1"))
button1.place(x=120,y=90)
button2= Button(text="2", command=lambda:show("2"))
button2.place(x=140,y=90)
button3= Button(text="3", command=lambda:show("3"))
button3.place(x=160,y=90)
add= Button(text="+", command=lambda:show("+"))
add.place(x=180,y=90)


button4= Button(text="4", command=lambda:show("4"))
button4.place(x=120,y=110)
button5= Button(text="5", command=lambda:show("5"))
button5.place(x=140,y=110)
button6= Button(text="6", command=lambda:show("6"))
button6.place(x=160,y=110)
minu= Button(text="-", command=lambda:show("-"))
minu.place(x=180,y=110)

button7= Button(text="7", command=lambda:show("7"))
button7.place(x=120,y=130)
button8= Button(text="8", command=lambda:show("8"))
button8.place(x=140,y=130)
button9= Button(text="9", command=lambda:show("9"))
button9.place(x=160,y=130)
multiply= Button(text="x", command=lambda:show("x"))
multiply.place(x=180,y=130)
button0= Button(text="0", command=lambda:show("0"))
button0.place(x=120,y=150)
dot= Button(text=".", command=lambda:show("."))
dot.place(x=140,y=150)
equal= Button(text="=", command=lambda:show("="))
equal.place(x=160,y=150)
divide= Button(text="/", command=lambda:show("/"))
divide.place(x=180,y=150)




root.mainloop()
