from tkinter import *
root=Tk()
myLabel1=Label(root, text="Hello World !")
myLabel2=Label(root, text="My name is Snigdha Pandey")
myLabel3=Label(root, text="      ")

#alternate to write the same
myLabel4=Label(root, text="Python Tkinter").grid(row=0,column=2)
# the columns have relative positioning to each other, i.e.. if the adjacent column is empty and does not contain any content to be displayed,the compiler ignores the gap and occupies the next concurrent available column for the display(consider myLabel1 and myLabel2) 
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)
myLabel3.grid(row=1,column=2)

root.mainloop()