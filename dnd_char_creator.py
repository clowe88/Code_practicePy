import random
from tkinter import *

root = Tk()
root.title("D&D Character Creator")
root.configure(bg='dark blue')

 
# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 10, padx = 10)
mainframe.configure(bg='light blue')

# Create a Tkinter variable
tkvar1 = StringVar(root)
tkvar2 = StringVar(root)
tkvar1.set("DragonBorn")
tkvar2.set("Ranger")

races = ["DragonBorn", "Orc", "Tiefling", "Elf", "Half-Elf", "Dwarf", "Gnome", "Half-Orcs", "Human", "Hafling"]
classes = ["Ranger", "Bard", "Warlock", "Barbarian", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Rogue", "Sorcerer", "Wizard"]

dnd_logo = PhotoImage('dnd.jpg')
dnd_label = Label(mainframe, image=dnd_logo).pack()

name = Entry(mainframe)
Label(mainframe,bg='royal blue',fg='white', text="Enter character name").pack()
name.pack()

popup_race = OptionMenu(mainframe, tkvar1, *races)
popup_race.configure(bg='forest green')
Label(mainframe,bg='royal blue',fg='white', text="Choose a Race").pack()
popup_race.pack()  

popup_class = OptionMenu(mainframe, tkvar2, *classes)
popup_class.configure(bg='forest green')
Label(mainframe,bg='royal blue',fg='white', text="Choose a Class").pack()
popup_class.pack()


def create_file(char_name, race, char_class, char_alignment, strength, dexterity, constitution, intelligence, wisdom, charisma, money, str_mod, dex_mod, const_mod, intel_mod, wis_mod, char_mod):
    print ("Character Name: " + char_name, file=open("dnd_char.txt", "a"))
    print ("Your Race is: " + race, file=open("dnd_char.txt", "a"))
    print ("Your Class is: " + char_class, file=open("dnd_char.txt", "a"))
    print ("Your Alignment is: " + char_alignment, file=open("dnd_char.txt", "a"))
    print ("Strength: " + str(strength) + "  Mod: " + str_mod, file=open("dnd_char.txt", "a"))
    print ("Dexterity: " + str(dexterity) + "  Mod: " + dex_mod, file=open("dnd_char.txt", "a"))
    print ("Constitution: " + str(constitution) + "  Mod: " + const_mod, file=open("dnd_char.txt", "a"))
    print ("Intelligence: " + str(intelligence) + "  Mod: " + intel_mod, file=open("dnd_char.txt", "a"))
    print ("Wisdom: " + str(wisdom) + "  Mod: " + wis_mod, file=open("dnd_char.txt", "a"))
    print ("Charisma: " + str(charisma) + "  Mod: " + char_mod, file=open("dnd_char.txt", "a"))
    print ("You start with " + str(money) + "gp.", file=open("dnd_char.txt", "a"))
    print ("", file=open("dnd_char.txt", "a"))
    print ("", file=open("dnd_char.txt", "a"))

def alignment():
    alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chatoic Evil"]
    a = random.randint(0,8)
    char_alignment = alignments[a]
    return char_alignment

#rolls for the ability stats
def ability_gen():
    ability1 = []
    ability2 = []
    ability3 = []
    ability4 = []
    ability5 = []
    ability6 = []
    x = 0 
    while x < 4:
        ability1.append(random.randint(1,6))
        ability2.append(random.randint(1,6))
        ability3.append(random.randint(1,6))
        ability4.append(random.randint(1,6))
        ability5.append(random.randint(1,6))
        ability6.append(random.randint(1,6))
        x += 1
    
    ability1.sort()
    ability2.sort()
    ability3.sort()
    ability4.sort()
    ability5.sort()
    ability6.sort()
    
    ability1.pop(0)
    ability2.pop(0)
    ability3.pop(0)
    ability4.pop(0)
    ability5.pop(0)
    ability6.pop(0)
    
    abl1 = ability1[0] + ability1[1] + ability1[2]
    abl2 = ability2[0] + ability2[1] + ability2[2]
    abl3 = ability3[0] + ability3[1] + ability3[2]
    abl4 = ability4[0] + ability4[1] + ability4[2]
    abl5 = ability5[0] + ability5[1] + ability5[2]
    abl6 = ability6[0] + ability6[1] + ability6[2]

    abilities = [abl1, abl2, abl3, abl4, abl5, abl6]
    return abilities

#assigning dice rolls to ablities
def ability_set(abilities):
    strength = abilities[0]
    dex = abilities[1]
    const = abilities[2]
    intel = abilities[3]
    wis = abilities[4]
    charisma = abilities[5]

    return strength, dex, const, intel, wis, charisma

def race_adj(race, strength, dexterity, constitution, intelligence, wisdom, charisma):
#Stat Adjustments based on class and Race
    attrib = [strength, constitution, intelligence, dexterity, wisdom]
    att1 = random.randint(0, 2)
    att2 = random.randint(3, len(attrib)-1)
    #Dragonborn - +2 Str, +1 charisma
    if race == races[0]:
        strength += 2
        charisma += 1
    #Orc - +2 Str, +1 Const, -2 Intel
    elif race == races[1]:
        strength += 2
        constitution +=1
        intelligence -= 2
    #Tiefling - +2 Charisma, +1 Intel
    elif race == races[2]:
        charisma += 2
        intelligence += 1
    #Elf - +2 Dex
    elif race == races[3]:
        dexterity += 2
    #Half-Elf - +2 Charisma, +1 to 2 others
    elif race == races[4]:
        charisma += 2
        rand1 = attrib[att1] 
        rand2 = attrib[att2]
        rand1 += 1
        rand2 += 1 
        if strength == rand1 or strength == rand2:
            strength += 1
                    
        if dexterity == rand1 or dexterity == rand2:
            dexterity += 1
                    
        if constitution == rand1 or constitution == rand2:
            constitution += 1
                    
        if intelligence == rand1 or intelligence == rand2:
            intelligence += 1
                   
        if wisdom == rand1 or wisdom == rand2:
            wisdom += 1                    
    #Dwarf - +2 Const
    elif race == races[5]:
        constitution += 2
    #Gnome - +2 Intel
    elif race == races[6]:
        intelligence += 2
    #Half-orc - +2 Str, +1 Const
    elif race == races[7]:
        strength += 2
        constitution += 1
    #Human - +1 to all
    elif race == races[8]:
        strength += 1
        dexterity += 1
        constitution += 1
        intelligence += 1
        wisdom += 1
        charisma += 1
    #Halfling - +2 Dex
    elif race == races[9]:
        dexterity += 2
    
    return strength, dexterity, constitution, intelligence, wisdom, charisma

#Creating Ability modifiers
def ability_mod(strength, dexterity, constitution, intelligence, wisdom, charisma):
    #Strength
    if strength == 1:
        str_mod = "-5"
    elif strength == 2 or strength == 3:
        str_mod = "-4"
    elif strength == 4 or strength == 5:
        str_mod = "-3"
    elif strength == 6 or strength == 7:
        str_mod = "-2"
    elif strength == 8 or strength == 9:
        str_mod = "-1"
    elif strength == 10 or strength == 11:
        str_mod = "0"
    elif strength == 12 or strength == 13:
        str_mod = "1"
    elif strength == 14 or strength == 15:
        str_mod = "2"
    elif strength == 16 or strength == 17:
        str_mod = "3"
    elif strength == 18 or strength == 19:
        str_mod = "4"
    elif strength == 20 or strength == 21:
        str_mod = "5"
    elif strength == 22 or strength == 23:
        str_mod = "6"
    elif strength == 24 or strength == 25:
        str_mod = "7"
    elif strength == 26 or strength == 27:
        str_mod = "8"
    elif strength == 28 or strength == 29:
        str_mod = "9"
    elif strength == 30:
        str_mod = "10"
    #Dexterity
    if dexterity == 1:
        dex_mod = "-5"
    elif dexterity == 2 or dexterity == 3:
        dex_mod = "-4"
    elif dexterity == 4 or dexterity == 5:
        dex_mod = "-3"
    elif dexterity == 6 or dexterity == 7:
        dex_mod = "-2"
    elif dexterity == 8 or dexterity == 9:
        dex_mod = "-1"
    elif dexterity == 10 or dexterity == 11:
        dex_mod = "0"
    elif dexterity == 12 or dexterity == 13:
        dex_mod = "1"
    elif dexterity == 14 or dexterity == 15:
        dex_mod = "2"
    elif dexterity == 16 or dexterity == 17:
        dex_mod = "3"
    elif dexterity == 18 or dexterity == 19:
        dex_mod = "4"
    elif dexterity == 20 or dexterity == 21:
        dex_mod = "5"
    elif dexterity == 22 or dexterity == 23:
        dex_mod = "6"
    elif dexterity == 24 or dexterity == 25:
        dex_mod = "7"
    elif dexterity == 26 or dexterity == 27:
        dex_mod = "8"
    elif dexterity == 28 or dexterity == 29:
        dex_mod = "9"
    elif dexterity == 30:
        dex_mod = "10"
     #Constitution
    if constitution == 1:
        const_mod = "-5"
    elif constitution == 2 or constitution == 3:
        const_mod = "-4"
    elif constitution == 4 or constitution == 5:
        const_mod = "-3"
    elif constitution == 6 or constitution == 7:
        const_mod = "-2"
    elif constitution == 8 or constitution == 9:
        const_mod = "-1"
    elif constitution == 10 or constitution == 11:
        const_mod = "0"
    elif constitution == 12 or constitution == 13:
        const_mod = "1"
    elif constitution == 14 or constitution == 15:
        const_mod = "2"
    elif constitution == 16 or constitution == 17:
        const_mod = "3"
    elif constitution == 18 or constitution == 19:
        const_mod = "4"
    elif constitution == 20 or constitution == 21:
        const_mod = "5"
    elif constitution == 22 or constitution == 23:
        const_mod = "6"
    elif constitution == 24 or constitution == 25:
        const_mod = "7"
    elif constitution == 26 or constitution == 27:
        const_mod = "8"
    elif constitution == 28 or constitution == 29:
        const_mod = "9"
    elif constitution == 30:
        const_mod = "10"
    #Intelligence
    if intelligence == 1:
        intel_mod = "-5"
    elif intelligence == 2 or intelligence == 3:
        intel_mod = "-4"
    elif intelligence == 4 or intelligence == 5:
        intel_mod = "-3"
    elif intelligence == 6 or intelligence == 7:
        intel_mod = "-2"
    elif intelligence == 8 or intelligence == 9:
        intel_mod = "-1"
    elif intelligence == 10 or intelligence == 11:
        intel_mod = "0"
    elif intelligence == 12 or intelligence == 13:
        intel_mod = "1"
    elif intelligence == 14 or intelligence == 15:
        intel_mod = "2"
    elif intelligence == 16 or intelligence == 17:
        intel_mod = "3"
    elif intelligence == 18 or intelligence == 19:
        intel_mod = "4"
    elif intelligence == 20 or intelligence == 21:
        intel_mod = "5"
    elif intelligence == 22 or intelligence == 23:
        intel_mod = "6"
    elif intelligence == 24 or intelligence == 25:
        intel_mod = "7"
    elif intelligence == 26 or intelligence == 27:
        intel_mod = "8"
    elif intelligence == 28 or intelligence == 29:
        intel_mod = "9"
    elif intelligence == 30:
        intel_mod = "10"
    #Wisdom
    if wisdom == 1:
        wis_mod = "-5"
    elif wisdom == 2 or wisdom == 3:
        wis_mod = "-4"
    elif wisdom == 4 or wisdom == 5:
        wis_mod = "-3"
    elif wisdom == 6 or wisdom == 7:
        wis_mod = "-2"
    elif wisdom == 8 or wisdom == 9:
        wis_mod = "-1"
    elif wisdom == 10 or wisdom == 11:
        wis_mod = "0"
    elif wisdom == 12 or wisdom == 13:
        wis_mod = "1"
    elif wisdom == 14 or wisdom == 15:
        wis_mod = "2"
    elif wisdom == 16 or wisdom == 17:
        wis_mod = "3"
    elif wisdom == 18 or wisdom == 19:
        wis_mod = "4"
    elif wisdom == 20 or wisdom == 21:
        wis_mod = "5"
    elif wisdom == 22 or wisdom == 23:
        wis_mod = "6"
    elif wisdom == 24 or wisdom == 25:
        wis_mod = "7"
    elif wisdom == 26 or wisdom == 27:
        wis_mod = "8"
    elif wisdom == 28 or wisdom == 29:
        wis_mod = "9"
    elif wisdom == 30:
        wis_mod = "10"
    #Charisma
    if charisma == 1:
        char_mod = "-5"
    elif charisma == 2 or charisma == 3:
        char_mod = "-4"
    elif charisma == 4 or charisma == 5:
        char_mod = "-3"
    elif charisma == 6 or charisma == 7:
        char_mod = "-2"
    elif charisma == 8 or charisma == 9:
        char_mod = "-1"
    elif charisma == 10 or charisma == 11:
        char_mod = "0"
    elif charisma == 12 or charisma == 13:
        char_mod = "1"
    elif charisma == 14 or charisma == 15:
        char_mod = "2"
    elif charisma == 16 or charisma == 17:
        char_mod = "3"
    elif charisma == 18 or charisma == 19:
        char_mod = "4"
    elif charisma == 20 or charisma == 21:
        char_mod = "5"
    elif charisma == 22 or charisma == 23:
        char_mod = "6"
    elif charisma == 24 or charisma == 25:
        char_mod = "7"
    elif charisma == 26 or charisma == 27:
        char_mod = "8"
    elif charisma == 28 or charisma == 29:
        char_mod = "9"
    elif charisma == 30:
        char_mod = "10" 

    return str_mod, dex_mod, const_mod, intel_mod, wis_mod, char_mod   

def wealth(char_class):
    money = 0
    rolls  = 0
    if char_class == "Cleric" or char_class == "Fighter" or char_class == "Ranger" or char_class == "Paladin"or char_class == "Barbarian":
        while rolls <= 5: 
            money += random.randint(0,4)
            rolls += 1
            
    if char_class == "Rogue" or char_class == "Wizard" or char_class == "Bard" or char_class == "Warlock" or char_class == "Monk" or char_class == "Sorcerer":
        while rolls <= 4: 
            money += random.randint(0,4)
            rolls += 1

    money = money * 10
    return money

def main():
    char_name = name.get()
    race = tkvar1.get()
    char_class = tkvar2.get()
    
    strength, dexterity, constitution, intelligence, wisdom, charisma = ability_set(ability_gen())

    ########char_name = char_name.capitalize()

    strength, dexterity, constitution, intelligence, wisdom, charisma = race_adj(race, strength, dexterity, constitution, intelligence, wisdom, charisma)

    str_mod, dex_mod, const_mod, intel_mod, wis_mod, char_mod = ability_mod(strength, dexterity, constitution, intelligence, wisdom, charisma)

    money = wealth(char_class)
    char_alignment = alignment()

    create_file(char_name, race, char_class, char_alignment, strength, dexterity, constitution, intelligence, wisdom, charisma, money, str_mod, dex_mod, const_mod, intel_mod, wis_mod, char_mod)

    #final character
    
    Label(mainframe,bg='orange',text="Character Name: " + char_name, justify=LEFT).pack()
    Label(mainframe,bg='orange',text="Your Race is: " + race).pack()
    Label(mainframe,bg='orange',text="Your Class is: " + char_class).pack()
    Label(mainframe,bg='orange',text="Your Alignment is: " + char_alignment).pack()
    Label(mainframe,bg='orange',text="Strength: " + str(strength) + "  Mod: " + str_mod).pack()
    Label(mainframe,bg='orange',text="Dexterity: " + str(dexterity) + "  Mod: " + dex_mod).pack()
    Label(mainframe,bg='orange',text="Constitution: " + str(constitution) + "  Mod: " + const_mod).pack()
    Label(mainframe,bg='orange',text="Intelligence: " + str(intelligence) + "  Mod: " + intel_mod).pack()
    Label(mainframe,bg='orange',text="Wisdom: " + str(wisdom) + "  Mod: " + wis_mod).pack()
    Label(mainframe,bg='orange',text="Charisma: " + str(charisma) + "  Mod: " + char_mod).pack()
    Label(mainframe,bg='orange',text="You start with " + str(money) + "gp.").pack()

    ############print ("You start with " + str(money) + "gp.")

start = Button(mainframe,bg='dark green', fg='white', text="Create", command=lambda:main())
start.pack()
def close_program():
    root.destroy()

close = Button(root, bg='dark red', fg='white',text='Exit', command=lambda:close_program())
close.pack()

root.mainloop()

#########    choice = input("Would you like to create another character? (y/n): ")
