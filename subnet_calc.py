from tkinter import *

root = Tk()
ipaddress = StringVar()
subnetmask = StringVar()

lblenterip = Label(root, text="Enter host IP address:", font="arial").pack()
entryipaddress = Entry(root, textvariable=ipaddress, width=15).pack()
lblentersubnet = Label(root, text="Enter subnet mask:", font="arial").pack()
entrysubnetmask = Entry(root, textvariable=subnetmask, width=15).pack()
btngoip = Button(root, text="GO!", command=lambda:goip()).pack()
btnclose = Button(root, text="Exit", command=lambda:close()).pack()

def close():
    root.destroy()

def goip():

    global ipaddress, subnetmask

    ip = ipaddress.get()
    subn = subnetmask.get()

    subnets, ipoctet1, ipoctet2, ipoctet3, ipoctet4, sub = subnetfinder(ip, subn)
    sub = int(sub)
    
    widgets = root.pack_slaves()
    for w in widgets:
        w.destroy()

    x = 0

    for i in subnets:
        if sub == 1:
            if int(ipoctet1) >= int(i) and int(ipoctet1) < int(subnets[x+1]):
                Label(root, text=str(str(subnets[x]) + ".0.0.0"), bg="yellow").pack()
                x += 1
            else:
                Label(root, text=str(str(subnets[x]) + ".0.0.0")).pack()
                x +=1
        elif sub == 2:
            if int(ipoctet2) >= int(i) and int(ipoctet2) < int(subnets[x+1]):
                Label(root, text=str(str(ipoctet1) + "." + str(subnets[x]) + ".0.0"), bg="yellow").pack()
                x += 1
            else:
                Label(root, text=str(str(ipoctet1) + "." + str(subnets[x]) + ".0.0")).pack()
                x +=1
        elif sub == 3:
            if int(ipoctet3) >= int(i) and int(ipoctet3) < int(subnets[x+1]):
                Label(root, text=str(str(ipoctet1) + "." + str(ipoctet2) + "." + str(subnets[x]) + ".0"), bg="yellow").pack()
                x += 1
            else:
                Label(root, text=str(str(ipoctet1) + "." + str(ipoctet2) + "." + str(subnets[x]) + ".0")).pack()
                x +=1
        elif sub == 4:
            if int(ipoctet4) >= int(i) and int(ipoctet4) < int(subnets[x+1]):
                Label(root, text=str(str(ipoctet1) + "." + str(ipoctet2) + "." + str(ipoctet3) + "." + str(subnets[x])), bg="yellow").pack()
                x += 1
            else:
                Label(root, text=str(str(ipoctet1) + "." + str(ipoctet2) + "." + str(ipoctet3) + "." + str(subnets[x]))).pack()
                x +=1
       

    btnclose = Button(root, text="Exit", command=lambda:close()).pack()

def subnetfinder(ip, subn):

    ipoctet1, ipoctet2, ipoctet3, ipoctet4 = str(ip).split(".")
    suboctet1, suboctet2, suboctet3, suboctet4 = str(subn).split(".")

    if int(suboctet1) == 255 or int(suboctet1) == 0:
        pass
    else:
        suboctet = suboctet1
        sub = 1

    if int(suboctet2) == 255 or int(suboctet2) == 0:
        pass
    else:
        suboctet = suboctet2
        sub = 2

    if int(suboctet3) == 255 or int(suboctet3) == 0:
        pass
    else:
        suboctet = suboctet3
        sub = 3

    if int(suboctet4) == 255 or int(suboctet4) == 0: 
        pass
    else:
        suboctet = suboctet4
        sub = 4

    if int(suboctet) == 254:
        subnets = []
        network = 0
        while network < 255:
            subnets.append(network)
            network = network + 2
    elif int(suboctet) == 252:
        subnets = []
        network = 0
        while network < 255:
            subnets.append(network)
            network = network + 4
    elif int(suboctet) == 248:
        subnets = []
        network = 0
        while network < 255:
            subnets.append(network)
            network = network + 8
    elif int(suboctet) == 240:
        subnets = []
        network = 0
        while network < 255:
            subnets.append(network)
            network = network + 16
    elif int(suboctet) == 224:
        subnets = []
        network = 0
        while network < 255:
            subnets.append(network)
            network = network + 32
    elif int(suboctet) == 192:
        subnets = []
        network = 0
        while network < 255:
            subnets.append(network)
            network = network + 64
    elif int(suboctet) == 128:
        subnets = []
        network = 0
        while network < 255:
            subnets.append(network)
            network = network + 128

    print (subnets)

    return (subnets, ipoctet1, ipoctet2, ipoctet3, ipoctet4, sub)

root.mainloop()