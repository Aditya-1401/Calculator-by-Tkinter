from tkinter import *
aj = Tk()
aj.title("Calculator")
aj.geometry("744x900")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="ERROR"
                screen.update()


        scvalue.set(value)
        screen.update() 
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


scvalue = StringVar()
scvalue.set("")
screen = Entry(aj,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=5,ipady=5,padx=5)

f=Frame(aj,bg="grey")

b = Button(f,text="9",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="8",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="7",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(aj,bg="grey")
b = Button(f,text="6",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="5",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="4",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(aj,bg="grey")
b = Button(f,text="3",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="2",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="1",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(aj,bg="grey")
b = Button(f,text="0",padx=27,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text=".",padx=32,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="C",padx=27,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(aj,bg="grey")
b = Button(f,text="+",padx=28,pady=15,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="-",padx=30,pady=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click) 

b = Button(f,text="*",padx=30,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(aj,bg="grey")
b = Button(f,text="%",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="/",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="=",padx=28,pady=18,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

aj.mainloop()
