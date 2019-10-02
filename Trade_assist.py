from tkinter import *
import os

root = Tk()

def main():
    global pricenum, discountnum, markupnum
    pricenum = IntVar()
    discountnum = IntVar()
    markupnum = IntVar()

    clear_screen()

    root.title("Test Area")
    root.configure(background="light blue")
        
    instruc1 = Label(root, bg="light blue",text="Enter Product Price:")
    instruc2 = Label(root, bg="light blue",text="Enter Current Discout:")
    instruc3 = Label(root, bg="light blue",text="Enter Current Markup:")

    prodprice = Entry(root, textvariable=pricenum)
    proddiscount = Entry(root, textvariable=discountnum)
    prodmarkup = Entry(root, textvariable=markupnum)

    prodprice.delete(0)
    proddiscount.delete(0)
    prodmarkup.delete(0)

    calc = Button(root, text="Calculate Profit",  command=lambda:calcprofit())
    exitbtn = Button(root, text="Exit", command=lambda:close_program())

    instruc1.pack()
    prodprice.pack()
    instruc2.pack()
    proddiscount.pack()
    instruc3.pack()
    prodmarkup.pack()
    calc.pack()
    exitbtn.pack()
    return

def close_program():
    root.destroy()

def clear_screen():
    widgets = root.pack_slaves()
    for w in widgets:
        w.destroy()

def calcprofit():
    price = pricenum.get()
    discount = discountnum.get()
    markup = markupnum.get()

    clear_screen()

    priceincrease = discount + markup
    profit = price * priceincrease / 100

    spentlbl = Label(root, bg="light blue", text="You Spent: " + str(price))
    profitmargin = Label(root,bg="light blue", text="Your profit is: " + str(profit))
    totalprofit = Label(root, bg="light blue", text="Your sell price will be " + str(price+profit))

    spentlbl.pack()
    profitmargin.pack()
    totalprofit.pack()
    
    mainmenu = Button(root, text="Main Screen",  command=lambda:main())
    exitbtn = Button(root, text="Exit", command=lambda:close_program())
    mainmenu.pack()
    exitbtn.pack()
    
    return profit   

    


main()

root.mainloop()