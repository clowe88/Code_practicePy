from tkinter import *
from random import randint

def chore(number):
    
    global pepnames
    text = number
    daily = Tk()
    Label(daily, text="This is Today's Chores List").grid(row=0, column=0)
    y=1
    
    for i in chorelist[text]:
        Label(daily, text=i + ': ' + chorelist[text][i]).grid(row=y, column=0)
        y += 1
        
    
def exit():
    root.destroy()
    
def calcreate():     
       
    global chorelist 
    global buttons
    global button 
    buttons = {}
    chorelist = {}  
    chores = ["Laundry", "Dishes", "Floors", "Bathroom", "Cat Boxes", "Dog Walking"]
    days = 0
    month = calvar.get()
    d = 1
    
    if month == "Apr" or month == "Jun" or month == "Sep" or month == "Nov":
        days = 31
    elif month == "Feb":
        days = 29
    elif month == "Jan" or month == "Mar" or month == "May" or month == "Jul" or month == "Aug" or month == "Oct" or month == "Dec":
         days = 32
    else: 
        errortk = Tk()
        Label(errortk, text="Please Select a Month.").grid(row=0, column=0)
        Button(errortk, text="OK", command=lambda:errortk.destroy()).grid(row=1, column=0)
        
    widgets = root.grid_slaves()
    for w in widgets:
        w.destroy()
    
    x = 0
    y = 0
    btn=1
    while d < days:
        chorelist[d] = {}
        if y == 7:
            y = 0
            x +=1
        Button(root, text=str(d), command=lambda d=d: chore(d), width=4).grid(columnspan=1, row=x, column=y)
        i = 0
        chores = ["Laundry", "Dishes", "Floors", "Bathroom", "Cat Boxes", "Dog Walking"]
        while i <= (len(pepnames)-1):            
            c = len(chores)-1
            l = randint(0, c)
            chorelist[d][pepnames[i]] = chores[l]
            chores.pop(l)
            print (chores)
            i += 1
        y += 1
        d += 1
        Button(root, text="Main Menu", command=lambda:mainmenu()).grid(columnspan = 3, row=5, column=2)
      
            
def mainmenu():
    root.destry()
    main()
    
    
def addname():
    global a
    x = pepvar.get()
    pepnames[a] = x
    a += 1    
    print (pepnames)
    
def main():
    global root 
    global pepvar
    global calvar
    global calmonths
    global pepnames
    global a  
    a=0
    
    
    
    root = Tk()
    root.title("Chores Calendar")

    pepvar = StringVar(root)
    pepvar.set("Name")
    calvar = StringVar(root)
    calvar.set("Months")
    calmonths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    pepnames = {}
    

    Label(root, text="Select Current Month: ").grid(columnspan=2, row=0, column=0)
    OptionMenu(root, calvar,*calmonths).grid(columnspan=2,row=1, column=0)

    Label(root, text="Enter peoples names: ").grid(columnspan=2,row=2, column=0)
    Entry(root, textvariable=pepvar, width=15).grid(row=3, column=0)
    Button(root, text="Add Name", command=lambda:addname()).grid(row=3, column=1)

    Button(root, text="Create Calendar", command=lambda:calcreate()).grid(columnspan=2,row=4, column=0)
    Button(root, text="Close", command=lambda:exit()).grid(columnspan=2,row=5, column=0)

    root.mainloop()

main()