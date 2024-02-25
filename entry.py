from tkinter import *
root=Tk()

e=Entry(root , width=50, bg="crimson" , fg="green", borderwidth=10)
e.pack()

def myClick():
    myLabel=Label(root,text="You Clicked a Button  !!")
    myLabel.pack()



myButton= Button(root,text="Click Here!" , command=myClick, fg="red" , bg="yellow")#the function is executed once before clicking the button.
#fg attribute displays the button text in red color and the bg as yellow

myButton.pack()

root.mainloop()