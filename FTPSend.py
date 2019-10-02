from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os
import ftplib

root = Tk()

def main():
    global ipaddress, username, password
    ipaddress = StringVar()
    username = StringVar()
    password = StringVar()

    Label(root, text="Enter IP Address:").pack()
    Entry(root, textvariable=ipaddress).pack()
    Label(root, text="").pack()
    Label(root, text="Enter Username:").pack()
    Entry(root, textvariable=username).pack()
    Label(root, text="Enter Password:").pack()
    Entry(root, textvariable=password, show="*").pack()
    Label(root, text="").pack()
    Label(root, text="Browse to configuration file:").pack()
    Button(root, text="Browse...", command=lambda:browse()).pack()
    Button(root, text="Go!", command=lambda:sendfiles()).pack()
    Button(root, text="Close", command=lambda:closeprogram()).pack()

    
def browse():
    e = Entry(root)
    e.destroy()
    filename = askopenfilename(initialdir="C:\%USERPROFILE%", filetypes =(("Text File", "*.txt"),("All Files","*.*")), title = "Choose a file.")
    e = Entry(root)
    e.insert(0,filename)
    e.configure(state=DISABLED, width=len(filename))
    e.pack()
    return filename
    
def closeprogram():
    root.destroy()

def sendfiles():
    ip = ipaddress.get()
    user = username.get()
    passwd = password.get()
    session = ftplib.FTP(ip, user, passwd)
    file = open(filename, 'rb')
    session.storbinary('STOR Config.txt', file)
    file.close()
    session.quit()



    

main()

root.mainloop()