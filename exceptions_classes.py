from tkinter import *
from random import *
root = Tk()

def main():
    global lashes, lashnum
    clear_screen()

    lashnum = IntVar()
 
    Label(root, text="Enter the max lashes you are willing to take", bg="black", fg="red").grid(column=1, columnspan=3, row=0)
    entlashes = Entry(root, width=5, textvariable=lashnum, justify=CENTER)
    entlashes.grid(column=2, row=1)

    impactbtn = Button(root, text="Impact Play", bg="dark red", width=10, command=lambda:impact())
    impactbtn.grid(column=1, row=2)
    sensationbtn = Button(root, text="Sensation Play", bg="dark red", width=10, command=lambda:sensation())
    sensationbtn.grid(column=2, row=2)
    ropebtn = Button(root, text="Rope Play", bg="dark red", width=10, command=lambda:ropework())
    ropebtn.grid(column=3, row=2)
    oralbtn = Button(root, text="Oral Play", bg="dark red", width=10, command=lambda:oral())
    oralbtn.grid(column=2, row=3)
    closebtn = Button(root, text="Close", bg="dark red", width=10, command=lambda:close_app())
    closebtn.grid(column=2, row=4)

def clear_screen():
    widgets = root.grid_slaves()
    for w in widgets:
        w.destroy()

def close_app():
    root.destroy()

def impact():
    clear_screen()

    lashes = lashnum.get()
    items = {0:"Flogger", 1:"Cane - Thick", 2:"Cane - Thin", 3:"Hand", 4:"Paddle"}
    selection = randrange(0,4)
    item = items[selection]

    toylbl = Label(root, text=item + " has been chosen", bg="black", fg="red")
    toylbl.grid(column=1, columnspan=2, row=0)

    licks = randrange(0,lashes)
    lickslbl = Label(root, text="Sub will take " + str(licks) + " licks!", bg="black", fg="red")
    lickslbl.grid(column=1, columnspan=2, row=1)

    mainbtn = Button(root, text="Main Menu", bg="dark red", width=10, command=lambda:main())
    mainbtn.grid(column=2, row=2)  

    closebtn = Button(root, text="Close", bg="dark red", width=10, command=lambda:close_app())
    closebtn.grid(column=1, row=2)  
    return

def ropework():
    clear_screen()
    ties = {0:"hands", 1:"feet", 2:"legs", 3:"chest", 4:"groin", 5:"neck", 6:"full body"}
    multitie = randrange(0,10)
    tietype = randrange(0,6)
    multi1 = randrange(0,2)
    multi2 = randrange(3,6)

    if multitie <= 4:
        Label(root, text="Tie the subs " + ties[tietype] + ".", bg="black", fg="red").grid(column=1, columnspan=3, row=0)
    elif multitie >= 5:
        Label(root, text="Tie the subs " + ties[multi1] + " to the subs " + ties[multi2] + ".", bg="black", fg="red").grid(column=1, columnspan=3, row=0)

    tiebtn = Button(root, text="Different Tie", bg="dark red", width=10, command=lambda:ropework())
    tiebtn.grid(column=1, columnspan=2, row=9)  

    mainbtn = Button(root, text="Main Menu", bg="dark red", width=10, command=lambda:main())
    mainbtn.grid(column=2, row=10)  

    closebtn = Button(root, text="Close", bg="dark red", width=10, command=lambda:close_app())
    closebtn.grid(column=1, row=10)  

    return

def oral():
    clear_screen()

    bodyparts = {0:"hands", 1:"feet", 2:"legs", 3:"chest", 4:"groin", 5:"neck", 6:"full body"}
    part = randrange(0,6)
    domsub = randrange(0,10)
    oraltime = randrange(1,5)

    if domsub <= 4:
        Label(root, text="Have Sub preform oral on the Dom's " + bodyparts[part] + " for " + str(oraltime) + " minutes.", bg="black", fg="red").grid(column=1, columnspan=3, row=0)
    elif domsub >= 5:
            Label(root, text="Dom preforms oral on the Sub's " + bodyparts[part]  + " for " + str(oraltime) + " minutes.", bg="black", fg="red").grid(column=1, columnspan=3, row=0)

    oralbtn = Button(root, text="Different Oral", bg="dark red", width=10, command=lambda:oral())
    oralbtn.grid(column=1, columnspan=2, row=9)  

    mainbtn = Button(root, text="Main Menu", bg="dark red", width=10, command=lambda:main())
    mainbtn.grid(column=2, row=10)  

    closebtn = Button(root, text="Close", bg="dark red", width=10, command=lambda:close_app())
    closebtn.grid(column=1, row=10)  

    return

def sensation():
    clear_screen()
    sensations = {0:"cold", 1:"hot", 2:"soft", 3:"sharp", 4:"that tickles"}
    parts = {0:"hands", 1:"feet", 2:"legs", 3:"chest", 4:"groin", 5:"neck", 6:"full body"}
    bodyparts = randrange(0,6)
    sensationnum = randrange(0,4)
    sentime = randrange(1,10)
    Label(root, text="Use something " + sensations[sensationnum], bg="black", fg="red").grid(column=1, columnspan=3, row=0)
    Label(root, text="on the subs " + parts[bodyparts] + " for " + str(sentime) + " minutes.", bg="black", fg="red").grid(column=1, columnspan=3,row=1)
    
    senbtn = Button(root, text="Different sensation", bg="dark red", width=15, command=lambda:sensation())
    senbtn.grid(column=1, columnspan=2, row=9)  

    mainbtn = Button(root, text="Main Menu", bg="dark red", width=10, command=lambda:main())
    mainbtn.grid(column=2, row=10)  

    closebtn = Button(root, text="Close", bg="dark red", width=10, command=lambda:close_app())
    closebtn.grid(column=1, row=10)
    
    return

root.title("Funishment App")
root.configure(bg="black")

main()

root.mainloop()