from tkinter import *

root = Tk()
root.title('Hangman Game')
root.configure(background='dark gray')
root.geometry('235x200+10+10')

def Start():
    global lblwordentry 
    global wordentry
    global startbtn
    global word
    global guess
    global guesses
    global hangman
    global letters
    global tryguess

    hangman = []
    widgets = root.pack_slaves()
    word = entword.get()
    word = word.lower()
   
    letters = [i for i in range(len(word))]
          
    for w in widgets:
        w.destroy()

    tryguess = StringVar()
    guesses = 5
    #frmword = Frame(root).pack(side=TOP)
    #frmtry = Frame(root).pack(side=RIGHT)    
    #frmbuttons = Frame(root).pack(side=BOTTOM)   
    p=20  
    for i in letters:
              
        letters[i] = Label(root, text="_").place(x=p, y=5)
        p = p + 15

    giveupbtn = Button(root, text="I Give Up", command=lambda:giveup()).place(x=20, y=100)
    restartbtn = Button(root, text="Restart", command=lambda:restart()).place(x=100, y=100)
    closebtn = Button(root, text="Close", command=lambda:exit()).place(x=175, y=100)
    trybtn = Button(root, text="Try", command=lambda:tryfunc()).place(x=110, y=60)
    tryentry = Entry(root, textvariable=tryguess, width=1).place(x=117, y=35)
    lblguess = Label(root,text="", bg='dark gray').place(x=60, y=135)
    lblleft = Label(root, text="Guesses left: " + str(guesses)).place(x=85, y=170)

    return word, closebtn, giveupbtn, restartbtn, trybtn, tryentry, tryguess, lblguess, lblleft, letters

def exit():
    root.destroy()

def giveup():
    global word
    widgets = root.place_slaves()
    for w in widgets: 
        w.destroy()
    lblword = Label(root, text="The word was: " + word).place(x=50, y=50)

def restart():
    widgets = root.place_slaves()
    for w in widgets:
        w.destroy()

    entword = StringVar()
    lblwordentry = Label(root, text="Enter the word to guess.").pack(side=TOP)
    wordentry = Entry(root,textvariable=entword,show='*').pack()
    startbtn = Button(root, text="START", command=lambda:Start()).pack(side=BOTTOM)

def tryfunc():
    global guess
    global hangman
    global letters 

    guess = tryguess.get()
    guess = guess.lower()
    current = ""

    for x in word:
        hangman.append("_")

        lettercount = 0
        for i in word:
            if i == guess:
                letters[lettercount] = Label(root, text=guess)
                hangman[lettercount] = guess
            elif letters[lettercount] != "_":
                letters[lettercount] = letters[lettercount]
                hangman[lettercount] = hangman[lettercount]
            else:
                letters[lettercount] = Label(root, text="_")
                hangman[lettercount] = "_"

        lettercount += 1

        for l in hangman:
            current = current + l

        if word == current:
            lblleft = Label(root, text="You Win!!!").place(x=85, y=170)
        else:
            guesses -+ 1

    if guesses == 0:
        lblleft = Label(root, text="You Lost :(").place(x=85, y=170)


    

entword = StringVar()
lblwordentry = Label(root, text="Enter the word to guess.").pack(side=TOP)
wordentry = Entry(root,textvariable=entword,show='*').pack()
startbtn = Button(root, text="START", command=lambda:Start()).pack(side=BOTTOM)
  


root.mainloop()