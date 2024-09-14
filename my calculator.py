import tkinter
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

#setting up the window
root = tkinter.Tk()
root.geometry("700x800+150+0")
root.title("my calculator")
#root.resizable(0,0)

def click(number):
    global operator
    if operator=="0":
        operator=""
    operator+=str(number)
    data.set(operator)

def clear():
    global operator
    operator='0'
    data.set(operator)

def equal():
    global operator
    try:
        operator=str(eval(operator))
        data.set(operator)
    except:
        data.set("Invalid Entry")

def dele():
    global operator
    operator=operator[:-1]
    if operator=="":
        operator='0'
    data.set(operator)

def fact():
    global operator
    try:
        #if ceil(operator) ==
        x=int(float(operator))
        factorial=1
        if x==0:
            data.set("1")
        if x<0:
            data.set("Invalid Entry")
        if x>0:
            for i in range(1,x+1):
                factorial=factorial*i
            operator=str(factorial)
            data.set(operator)
    except:
        data.set("Invalid Entry")

data = StringVar()
operator=''

lbl=Label(
    root,
    text="Label",
    anchor=SE,
    font = ("Verdana", 20),
    textvariable = data,
    background = "#000000",
    fg = "#ffffff"
)
lbl.pack(expand = True, fill = "both")

data.set("0")

btnrow0 = Frame(root,width=100,height=15, relief=SUNKEN,bg="#000000")
btnrow0.pack(expand =True, fill="both")

btnrow1 = Frame(root,bg="#000000")
btnrow1.pack(expand =True, fill="both")

btnrow2 = Frame(root,bg="#000000")
btnrow2.pack(expand =True, fill="both")

btnrow3 = Frame(root,bg="#000000")
btnrow3.pack(expand =True, fill="both")

btnrow4 = Frame(root,bg="#000000")
btnrow4.pack(expand =True, fill="both")

#zeroth button row
btn1 = Button(
    btnrow0,
    text = "!",
    font = ("Verdana", 15),
    fg = "light blue",
    border = 0,
    bg="#28282B",
    command = fact,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow0,
    text = "%",
    font = ("Verdana", 15),
    fg = "light blue",
    border = 0,
    bg="#28282B",
    command = lambda:click('%')
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow0,
    text = "Pow",
    font = ("Verdana", 15),
    fg = "light blue",
    border = 0,
    bg="#28282B",
    command = lambda:click("**")
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow0,
    text = "del.",
    font = ("Verdana", 15),
    fg = "light blue",
    border = 0,
    bg="#28282B",
    command =dele
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow0,
    text = "=",
    font = ("Verdana", 15),
    fg = "light blue",
    border = 0,
    bg="#28282B",
    command = equal
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

#first row btn
btn1 = Button(
    btnrow1,
    text = "7",
    font = ("Verdana", 25),
    fg = "#ffffff",
    border = 2,
    bg="#28282B",
    command = lambda:click(7)
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "8",
    font = ("Verdana", 25),
    fg = "#ffffff",
    border = 2,
    bg="#28282B",
    command = lambda:click(8)
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "9",
    font = ("Verdana", 25),
    fg = "#ffffff",
    border = 2,
    bg="#28282B",
    command = lambda:click(9)
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow1,
    text = "X",
    font = ("Verdana", 25),
    fg = "light blue",
    border = 2,
    bg="#28282B",
    command = lambda:click("*")
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

#second row btn
btn1 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 25),
    fg = "#ffffff",
    border = 2,
    bg="#28282B",
    command = lambda:click(4)
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 25),
    fg = "#ffffff",
    border = 2,
    bg="#28282B",
    command = lambda:click(5)
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 25),
    fg = "#ffffff",
    border = 2,
    bg="#28282B",
    command = lambda:click(6)
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow2,
    text = "/",
    font = ("Verdana", 30),
    fg = "light blue",
    border = 2,
    bg="#28282B",
    command = lambda:click("/")
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

#third btn row
btn1 = Button(
    btnrow3,
    text = "1",
    font = ("Verdana", 25),
    fg = "#ffffff",
    border = 2,
    bg="#28282B",
    command = lambda:click(1)
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow3,
    text = "2",
    font = ("Verdana", 25),
    fg = "#ffffff",
    border = 2,
    bg="#28282B",
    command = lambda:click(2)
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow3,
    text = "3",
    font = ("Verdana", 25),
    fg = "#ffffff",
    border = 2,
    bg="#28282B",
    command = lambda:click(3)
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow3,
    text = "+",
    font = ("Verdana", 24),
    fg = "light blue",
    border = 2,
    bg="#28282B",
    command = lambda:click("+")
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

#forth button row
btn1 = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 25),
    fg = "#ffffff",
    border = 2,
    bg="orange",
    command = clear
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 25),
    fg = "#ffffff",
    border = 2,
    bg="#28282B",
    command = lambda:click(0)
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow4,
    text = ".",
    font = ("Verdana", 30),
    fg = "light blue",
    border = 2,
    bg="#28282B",
    command = lambda:click(".")
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow4,
    text = "-",
    font = ("Verdana", 31),
    fg = "light blue",
    border = 2,
    bg="#28282B",
    command = lambda:click("-")
)
btn4.pack(side = LEFT, expand = True, fill = "both",)



root.mainloop()
