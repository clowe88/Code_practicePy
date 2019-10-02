from tkinter import *
from pygame import *
import random

root = Tk()

global dmg 
weplist = {
                "lance":1,
                "sword":2, 
                "dagger":3,
                "axe": 4,
                "spear":5
    }

weplist2 = {
                1:"lance",
                2:"sword", 
                3:"dagger",
                4:"axe",
                5:"spear"
    }


def wep_to_dmg(weapon):

    switcher = {
                1:lance(),
                2:sword(),
                3:dagger(), 
                4:axe(),
                5:spear()
                }
    func = switcher.get(weapon, lambda:"Nothing Equipped")
    print (func)

def lance():
    global dmg
    dmg = random.randint(2,16)
    
def sword():
    global dmg
    dmg = random.randint(2,12)

def dagger():
    global dmg
    dmg = random.randint(2,10)

def axe():
    global dmg
    dmg = random.randint(2,10)

def spear():
    global dmg
    dmg = random.randint(2,16)

char1 = {"name" : "Skyggen", 
         "weapon" : "sword", 
         "armor"  : 12, 
         "attack" : 10, 
         "health" : 100,
         "level"  : 1,
         "exp"    : 0
}

char2 = {"name" : "Black Knight",
         "weapon" : "lance",
         "armor"  : 15, 
         "attack" : 10,
         "health" : 100,
         "level"  : 1,
         "exp"    : 0
}

def main():
    char1["health"] = 100
    char2["health"] = 100
    widgets = root.pack_slaves()
    for w in widgets:
        w.destroy()
    Button(root, text="Lance", command=lambda:wep1btn()).pack(side=TOP)
    Button(root, text="Sword", command=lambda:wep2btn()).pack(side=TOP)
    Button(root, text="Dagger", command=lambda:wep3btn()).pack(side=TOP)
    Button(root, text="Axe", command=lambda:wep4btn()).pack(side=TOP)
    Button(root, text="Spear", command=lambda:wep5btn()).pack(side=TOP)


    Button(root, text="Attack!", command=lambda:playeratk()).pack(side=LEFT)
    Button(root, text="Exit", command=lambda:close_program()).pack(side=LEFT)
    Button(root, text="Block!", command=lambda:playerblock()).pack(side=LEFT)


def playeratk():
    # use following to generate dmg value: wep_to_dmg(weplist[char1["weapon"]])
    #rolls for if the computer blocks and if so what damage is taken
    blkroll = random.randint(0,1)
    blkmulti = random.randint(0,1)
    char2["weapon"] = weplist2[random.randint(1,5)]

    if blkroll == 0:
        if random.randint(1,20) >= char2["armor"]:
            mixer.init()
            mixer.music.load("dnd_sounds/\/Swords_Collide.mp3")
            mixer.music.play()
            #player 1 attack
            wep_to_dmg(weplist[char1["weapon"]])
            print (str(dmg) + " Damage Done!")
            char2["health"] = char2["health"]-dmg
        else:
            print (char1["name"] + " did not roll high enough to hit!")
        if random.randint(1,20) >= char1["armor"]:
            #player 2 attack if block == 0 (no block)
            wep_to_dmg(weplist[char2["weapon"]])
            print (str(dmg) + " Damage Done!")
            char1["health"] = char1["health"]-dmg
        else:
            print (char2["name"] + " did not roll high enough to hit!")
    else:
        mixer.init()
        mixer.music.load("dnd_sounds/\/metal clang.mp3")
        mixer.music.play()
        if blkmulti == 0:
            if random.randint(1,20) >= char2["armor"]:
            #player 1 attack
                wep_to_dmg(weplist[char1["weapon"]])
                print (char2["name"] + " Blocked! " + str(dmg/2) + " Damage Done!")
                char2["health"] = char2["health"]-dmg/2
            else:
                print (char2["name"] + " did not roll high enough to hit!")
        elif random.randint(1,20) >= char2["armor"]:
            #player 1 attack
            wep_to_dmg(weplist[char1["weapon"]])
            print (char2["name"] + " Blocked! " + str(0) + " Damage Done!")
            char2["health"] = char2["health"]
        else:
            print (char2["name"] + " did not roll high enough to hit!")
           
    #win check
    if char1["health"] <= 0:
        widgets = root.pack_slaves()
        for w in widgets:
            w.destroy()
        Label(root, text=(char2["name"] + " Wins!!!")).pack(side=TOP)
        Button(root, text="Play Again?", command=lambda:main()).pack(side=LEFT)
        Button(root, text="Quit", command=lambda:close_program()).pack(side=RIGHT)
    elif char2["health"] <= 0:
        widgets = root.pack_slaves()
        for w in widgets:
            w.destroy()
        Label(root, text=(char1["name"] + " Wins!!!")).pack()
        Button(root, text="Play Again?", command=lambda:main()).pack(side=LEFT)
        Button(root, text="Quit", command=lambda:close_program()).pack(side=RIGHT)
    else: 
        #show current HP    
        print (char1["name"] + " is at " + str(char1["health"]) + " HP.")
        print (char2["name"] + " is at " + str(char2["health"]) + " HP.")
           

def playerblock():
    #rolls for if the computer blocks and if so what damage is taken
    blkroll = random.randint(0,1)
    blkmulti = random.randint(0,1)
    char2["weapon"] = weplist2[random.randint(1,5)]

    if blkroll == 0:
        mixer.init()
        mixer.music.load("dnd_sounds/\/metal clang.mp3")
        mixer.music.play()
        #player 1 blocks        
        #player 2 attack if block == 0 (no block)
        if blkmulti == 0:
            if random.randint(1,20) >= char1["armor"]:
                wep_to_dmg(weplist[char2["weapon"]])
                print (char1["name"] + " Blocked! " + str(dmg/2) + " Damage Done!")
                char1["health"] = char1["health"]-dmg/2
        else:
            if random.randint(1,20) >= char1["armor"]: 
                wep_to_dmg(weplist[char2["weapon"]])
                print (char1["name"] + " Blocked! " + str(0) + " Damage Done!")
                char1["health"] = char1["health"]
    else:
        mixer.init()
        mixer.music.load("dnd_sounds/\/swoosh 3.mp3")
        mixer.music.play()
        print (char2["name"] + " Missed!!")
    
       #win check
    if char1["health"] <= 0:
        widgets = root.pack_slaves()
        for w in widgets:
            w.destroy()
        Label(root, text=(char2["name"] + " Wins!!!")).pack(side=TOP)
        Button(root, text="Play Again?", command=lambda:main()).pack(side=LEFT)
        Button(root, text="Quit", command=lambda:close_program()).pack(side=RIGHT)
    elif char2["health"] <= 0:
        widgets = root.pack_slaves()
        for w in widgets:
            w.destroy()
        Label(root, text=(char1["name"] + " Wins!!!")).pack(side=TOP)
        Button(root, text="Play Again?", command=lambda:main()).pack(side=LEFT)
        Button(root, text="Quit", command=lambda:close_program()).pack(side=RIGHT)
    else: 
        #show current HP    
        print (char1["name"] + " is at " + str(char1["health"]) + " HP.")
        print (char2["name"] + " is at " + str(char2["health"]) + " HP.")
    
def close_program():
    root.destroy()

def wep1btn():
    char1["weapon"] = "lance"
    print (char1["name"] + " switched to " + char1["weapon"] + "! ")

def wep2btn():
    char1["weapon"] = "sword"
    print (char1["name"] + " switched to " + char1["weapon"] + "! ")

def wep3btn():
    char1["weapon"] = "dagger"
    print (char1["name"] + " switched to " + char1["weapon"] + "! ")

def wep4btn():
    char1["weapon"] = "axe"
    print (char1["name"] + " switched to " + char1["weapon"] + "! ")

def wep5btn():
    char1["weapon"] = "spear"
    print (char1["name"] + " switched to " + char1["weapon"] + "! ")
       

main()

root.mainloop()