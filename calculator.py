from tkinter import *
root=Tk()
root.title("Simple Calculator")

e=Entry(root,width=35,border=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def b_click(number):
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))


def b_clear():
    e.delete(0,END)

def b_add():
    first_number=e.get()
    global f_num
    global math 
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)
    

def b_sub():
    first_number=e.get()
    global f_num
    global math 
    math="subtraction"
    f_num=int(first_number)
    e.delete(0,END)

def b_mul():
    first_number=e.get()
    global f_num
    global math 
    math="multiplication"
    f_num=int(first_number)
    e.delete(0,END)

def b_div():
    first_number=e.get()
    global f_num
    global math 
    math="division"
    f_num=int(first_number)
    e.delete(0,END)


def b_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(second_number))

    if math=="subtraction":
        e.insert(0,f_num - int(second_number))

    if math=="multiplication":
        e.insert(0,f_num * int(second_number))
    
    if math=="division":
        e.insert(0,f_num / int(second_number))

b1=Button(root,text="1",padx=40,pady=20,command=lambda : b_click(1)).grid(row=3,column=0)
b2=Button(root,text="2",padx=40,pady=20,command=lambda : b_click(2)).grid(row=3,column=1)
b3=Button(root,text="3",padx=40,pady=20,command=lambda : b_click(3)).grid(row=3,column=2)

b4=Button(root,text="4",padx=40,pady=20,command=lambda : b_click(4)).grid(row=2,column=0)
b5=Button(root,text="5",padx=40,pady=20,command=lambda : b_click(5)).grid(row=2,column=1)
b6=Button(root,text="6",padx=40,pady=20,command=lambda : b_click(6)).grid(row=2,column=2)

b7=Button(root,text="7",padx=40,pady=20,command=lambda : b_click(7)).grid(row=1,column=0)
b8=Button(root,text="8",padx=40,pady=20,command=lambda : b_click(8)).grid(row=1,column=1)
b9=Button(root,text="9",padx=40,pady=20,command= lambda : b_click(9)).grid(row=1,column=2)

b0=Button(root,text="0",padx=40,pady=20,command=lambda :  b_click(0)).grid(row=4,column=0)
bAdd=Button(root,text="+",padx=39,pady=20,command= b_add).grid(row=5,column=0)
bEqual=Button(root,text="=",padx=90,pady=20,command= b_equal).grid(row=5,column=1,columnspan=2)
bClear=Button(root,text="Clear",padx=79,pady=20,command=lambda : b_clear()).grid(row=4,column=1,columnspan=2)



bSub=Button(root,text="-",padx=41,pady=20,command= b_sub).grid(row=6,column=0)
bMul=Button(root,text="*",padx=40,pady=20,command= b_mul).grid(row=6,column=1)
bDiv=Button(root,text="/",padx=41,pady=20,command= b_div).grid(row=6,column=2)

root.mainloop()