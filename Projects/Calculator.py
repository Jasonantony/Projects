from tkinter import *
from PIL import *
import math


root= Tk()
root.title('Calculator')

def calc(number):
    current = inp.get()
    inp.delete(0,END)
    inp.insert(0,str(current)+str(number))

def add():
    first=inp.get()
    inp.delete(0,END)
    global f_num
    global math
    math="addition"
    f_num=int(first)

def sub():
    first=inp.get()
    inp.delete(0,END)
    global f_num
    global math
    math="sub"
    f_num=int(first)
def mul():
    first=inp.get()
    inp.delete(0,END)
    global f_num
    global math
    math="mul"
    f_num=int(first)

def div():
    first=inp.get()
    inp.delete(0,END)
    global f_num
    global math
    math="div"
    f_num=int(first)

def clear():
    inp.delete(0,END)

def equals():
    second_num=inp.get()
    inp.delete(0,END)

    if math == "addition":
        inp.insert(0,f_num+int(second_num))

    elif math == "sub":
        inp.insert(0,f_num - int(second_num))

    elif math == "mul":
        inp.insert(0,f_num * int(second_num))
    
    elif math == "div":
        inp.insert(0,f_num / int(second_num))

inp=Entry(root,width=40)
inp.grid(row=0, column=0,columnspan=4,padx=35)

button_1 = Button(root,text="1" ,command=lambda: calc(1),padx=35,pady=35,bg='powderblue')
button_2 = Button(root,text="2" ,command=lambda: calc(2),padx=35,pady=35,bg='powderblue')
button_3 = Button(root,text="3" ,command=lambda: calc(3),padx=35,pady=35,bg='powderblue')
button_4 = Button(root,text="4", command=lambda: calc(4),padx=35,pady=35,bg='powderblue')

button_5 = Button(root,text="5" ,command=lambda: calc(5),padx=35,pady=35,bg='powderblue')
button_6 = Button(root,text="6" ,command=lambda: calc(6),padx=35,pady=35,bg='powderblue')
button_7 = Button(root,text="7" ,command=lambda: calc(7),padx=35,pady=35,bg='powderblue')
button_8 = Button(root,text="8" ,command=lambda: calc(8),padx=35,pady=35,bg='powderblue')

button_9 = Button(root,text="9" ,command=lambda: calc(9),padx=35,pady=35,bg='powderblue')
button_0 = Button(root,text="0" ,command=lambda: calc(0),padx=35,pady=35,bg='powderblue')

button_equal=Button(root,text="=",command=equals,padx=35,pady=80,bg='slategrey')
button_add=Button(root,text="+",command=add,padx=33,pady=35,bg='slategrey')
button_sub=Button(root,text="-",command=sub,padx=35,pady=35,bg='slategrey')
button_div=Button(root,text="/",command=div,padx=35,pady=35,bg='slategrey')
button_mul=Button(root,text="*",command=mul,padx=35,pady=35,bg='slategrey')
button_clear=Button(root,text="Clear",command=clear,padx=155,pady=35,bg='slategrey')


button_clear.grid(row=5,column=0,columnspan=4)
button_div.grid(row=4,column=2)
button_mul.grid(row=4,column=1)
button_sub.grid(row=4,column=0)
button_add.grid(row=3,column=2)
button_equal.grid(row=3,column=3,rowspan=2)
button_0.grid(row=3,column=1)
button_1.grid(row=3,column=0)
button_2.grid(row=2,column=3)
button_3.grid(row=2,column=2)
button_4.grid(row=2,column=1)
button_5.grid(row=2,column=0)
button_6.grid(row=1,column=3)
button_7.grid(row=1,column=2)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=0)


root.mainloop()