from tkinter import *

root = Tk()
root.title("To Do List")

def itemadd():
    lb.insert(END,todo.get())
    additem.delete(0,END)



Label(root, text="Enter To Do List Item: ", width=20).grid(column=1, row=0, columnspan=2)

todo = StringVar()
additem = Entry(root, textvariable=todo, width=20)
additem.grid(column=1, row=1, columnspan=2)
additem.bind("<Return>", (lambda event:itemadd()))

scroll = Scrollbar(root, orient=VERTICAL)
lb = Listbox(root, width=30, height=15, selectmode=BROWSE, yscrollcommand=scroll.set)
lb.grid(column=1, row=4, columnspan=2)
scroll.grid(column=0, row=4, rowspan=1)
scroll.config(command=lb.yview)

btnadd = Button(root, text="Add List Item",command=lambda: itemadd(), width=15)
btnadd.grid(column=1, row=3, columnspan=2)


btnremove = Button(root, text="Remove List Item", width=15, command=lambda lb=lb: lb.delete(ANCHOR)).grid(column=1, row=5, columnspan=2)
btnremoveall = Button(root, text="Remove All", width=10, command=lambda lb=lb: lb.delete(0,END)).grid(column=1, row=6, columnspan=2)

btnclose = Button(root, text="Close", command=lambda:root.destroy(), width=5).grid(column=1, row=7, columnspan=2)



root.mainloop()

