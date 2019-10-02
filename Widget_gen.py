from tkinter import *
import random

root = Tk()
i = 0
x = 0
y = 0
while i < 15:
    if x == 5:
        x = 0
        y +=1
    Button(root, text ="button" + str(i)).grid(row=x, column=y)
    x += 1
    i += 1

root.mainloop()