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
    ipoctet1, ipoctet2, ipoctet3, ipoctet4 = ipaddress.get().split(".")
    suboctet1, suboctet2, suboctet3, suboctet4 = subnetmask.get().split(".")
    
    widgets = root.pack_slaves()
    for w in widgets:
        w.destroy()

    if int(suboctet1) != 255:
        if int(suboctet1) == 254:
            subnets = []
            network = 0
            cidr = 7
            while network < 255:
                subnets.append(network)
                network = network + 2
        elif int(suboctet1) == 252:
            subnets = []
            network = 0
            cidr = 6
            while network < 255:
                subnets.append(network)
                network = network + 4
        elif int(suboctet1) == 248:
            subnets = []
            network = 0
            cidr = 5
            while network < 255:
                subnets.append(network)
                network = network + 8
        elif int(suboctet1) == 240:
            subnets = []
            network = 0
            cidr = 4
            while network < 255:
                subnets.append(network)
                network = network + 16
        elif int(suboctet1) == 224:
            subnets = []
            network = 0
            cidr = 3
            while network < 255:
                subnets.append(network)
                network = network + 32
        elif int(suboctet1) == 192:
            subnets = []
            network = 0
            cidr = 2
            while network < 255:
                subnets.append(network)
                network = network + 64
        elif int(suboctet1) == 128:
            subnets = []
            network = 0
            cidr = 1
            while network < 255:
                subnets.append(network)
                network = network + 128
    elif int(suboctet2) != 255:
        if int(suboctet2) == 254:
            subnets = []
            network = 0
            cidr = 15
            while network < 255:
                subnets.append(network)
                network = network + 2
        elif int(suboctet2) == 252:
            subnets = []
            network = 0
            cidr = 14
            while network < 255:
                subnets.append(network)
                network = network + 4
        elif int(suboctet2) == 248:
            subnets = []
            network = 0
            cidr = 13
            while network < 255:
                subnets.append(network)
                network = network + 8
        elif int(suboctet2) == 240:
            subnets = []
            network = 0
            cidr = 12
            while network < 255:
                subnets.append(network)
                network = network + 16
        elif int(suboctet2) == 224:
            subnets = []
            network = 0
            cidr = 11
            while network < 255:
                subnets.append(network)
                network = network + 32
        elif int(suboctet2) == 192:
            subnets = []
            network = 0
            cidr = 10
            while network < 255:
                subnets.append(network)
                network = network + 64
        elif int(suboctet2) == 128:
            subnets = []
            network = 0
            cidr = 9
            while network < 255:
                subnets.append(network)
                network = network + 128
    elif int(suboctet3) != 255:
        if int(suboctet3) == 254:
            subnets = []
            network = 0
            cidr = 23
            while network < 255:
                subnets.append(network)
                network = network + 2
        elif int(suboctet3) == 252:
            subnets = []
            network = 0
            cidr = 22
            while network < 255:
                subnets.append(network)
                network = network + 4
        elif int(suboctet3) == 248:
            subnets = []
            network = 0
            cidr = 21
            while network < 255:
                subnets.append(network)
                network = network + 8
        elif int(suboctet3) == 240:
            subnets = []
            network = 0
            cidr = 20
            while network < 255:
                subnets.append(network)
                network = network + 16
        elif int(suboctet3) == 224:
            subnets = []
            network = 0
            cidr = 19
            while network < 255:
                subnets.append(network)
                network = network + 32
        elif int(suboctet3) == 192:
            subnets = []
            network = 0
            cidr = 18
            while network < 255:
                subnets.append(network)
                network = network + 64
        elif int(suboctet3) == 128:
            subnets = []
            network = 0
            cidr = 17
            while network < 255:
                subnets.append(network)
                network = network + 128
    elif int(suboctet4) != 255:
        if int(suboctet4) == 254:
            subnets = []
            network = 0
            cidr = 31
            while network < 255:
                subnets.append(network)
                network = network + 2
        elif int(suboctet4) == 252:
            subnets = []
            network = 0
            cidr = 30
            while network < 255:
                subnets.append(network)
                network = network + 4
        elif int(suboctet4) == 248:
            subnets = []
            network = 0
            cidr = 29
            while network < 255:
                subnets.append(network)
                network = network + 8
        elif int(suboctet4) == 240:
            subnets = []
            network = 0
            cidr = 28
            while network < 255:
                subnets.append(network)
                network = network + 16
        elif int(suboctet4) == 224:
            subnets = []
            network = 0
            cidr = 27
            while network < 255:
                subnets.append(network)
                network = network + 32
        elif int(suboctet4) == 192:
            subnets = []
            network = 0
            cidr = 26
            while network < 255:
                subnets.append(network)
                network = network + 64
        elif int(suboctet4) == 128:
            subnets = []
            network = 0
            cidr = 25
            while network < 255:
                subnets.append(network)
                network = network + 128

    Label(root,text="CIDR: /" + str(cidr)).pack(side=TOP)

    if suboctet1 != 255:
        x=0
        for i in subnets:
            Label(root, text=str(subnets[x]) + ".0.0.0").pack()
            x = x+1
    elif suboctet2 != 255:
        x=0
        for i in subnets:
            Label(root, text=ipoctet1 + "." + str(subnets[x]) + ".0.0").pack()
            x = x+1
    elif suboctet3 != 255:
        x=0
        for i in subnets:
            Label(root, text=ipoctet1 + "." + ipoctet2 + "." + str(subnets[x]) + ".0").pack()
            x = x+1
    elif suboctet4 != 255:
        x=0
        for i in subnets:
            Label(root, text=ipoctet1 + "." + ipoctet2 + "." + ipoctet3 + "." + str(subnets[x])).pack()
            x = x+1

    btnclose = Button(root, text="Exit", command=lambda:close()).pack()

root.mainloop()