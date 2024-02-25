from tkinter import *
root=Tk()

def myClick():
    myLabel=Label(root,text="You Clicked a Button 1 !!")
    myLabel.pack()
#A button in tkinter is a widget
myButton= Button(root,text="Click Here!" , command=myClick )#after clicking the button ,executes the function the times one clicks


myButton= Button(root,text="Click Here!" , command=myClick(), fg="red" , bg="yellow")#the function is executed once before clicking the button.
#fg attribute displays the button text in red color and the bg as yellow

myButton.pack()

root.mainloop()