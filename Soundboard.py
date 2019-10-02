from tkinter import *
from pygame import *
from random import *
import glob

root = Tk()
root.title("Soundboards")

def close():
    root.destroy()

def randomsound():
    sounds = []
    sounds = glob.glob("random_sounds\*.mp3")
    num = randrange(0,len(sounds)-1)
    mixer.init()
    mixer.music.load(sounds[num])
    mixer.music.play()
    
def lebowski():

    def aggression():
        mixer.init()
        mixer.music.load("lebowski/\/aggression.mp3")
        mixer.music.play()

    def closethefile():
        mixer.init()
        mixer.music.load("lebowski/\/close the file.mp3")
        mixer.music.play()

    def diosmoman():
        mixer.init()
        mixer.music.load("lebowski/\/dios mo man.mp3")
        mixer.music.play()

    def dude():
        mixer.init()
        mixer.music.load("lebowski/\/dude.mp3")
        mixer.music.play()

    def stranger():
        mixer.init()
        mixer.music.load("lebowski/\/fuck a stranger in the ass.mp3")
        mixer.music.play()

    def fuckeditup():
        mixer.init()
        mixer.music.load("lebowski/\/fucked it up.mp3")
        mixer.music.play()

    def fascist():
        mixer.init()
        mixer.music.load("lebowski/\/fucking fascist.mp3")
        mixer.music.play()

    def ringer():
        mixer.init()
        mixer.music.load("lebowski/\/give me the ringer.mp3")
        mixer.music.play()

    def goddamnit():
        mixer.init()
        mixer.music.load("lebowski/\/god damn it.mp3")
        mixer.music.play()

    def sweetprince():
        mixer.init()
        mixer.music.load("lebowski/\/good night sweet prince.mp3")
        mixer.music.play()

    def mandowndude():
        mixer.init()
        mixer.music.load("lebowski/\/got a man down dude.mp3")
        mixer.music.play()

    def howyoudoing():
        mixer.init()
        mixer.music.load("lebowski/\/how you doing there.mp3")
        mixer.music.play()

    def walrus():
        mixer.init()
        mixer.music.load("lebowski/\/i am the walrus.mp3")
        mixer.music.play()

    def yourstyle():
        mixer.init()
        mixer.music.load("lebowski/\/i like your style.mp3")
        mixer.music.play()

    def suck():
        mixer.init()
        mixer.music.load("lebowski/\/ill suck your cock.mp3")
        mixer.music.play()

    def fuckswithjesus():
        mixer.init()
        mixer.music.load("lebowski/\/nobody fucks with jesus.mp3")
        mixer.music.play()

    def phoneisringing():
        mixer.init()
        mixer.music.load("lebowski/\/phone is ringing dude.mp3")
        mixer.music.play()

    def roomformore():
        mixer.init()
        mixer.music.load("lebowski/\/room for one more.mp3")
        mixer.music.play()

    def donny():
        mixer.init()
        mixer.music.load("lebowski/\/shut the fuck up donny.mp3")
        mixer.music.play()

    def strike():
        mixer.init()
        mixer.music.load("lebowski/\/strike.mp3")
        mixer.music.play()

    def easydude():
        mixer.init()
        mixer.music.load("lebowski/\/take easy dude.mp3")
        mixer.music.play()

    def crashed():
        mixer.init()
        mixer.music.load("lebowski/\/the god damn plane has crashed.mp3")
        mixer.music.play()

    def whoareyou():
        mixer.init()
        mixer.music.load("lebowski/\/who the fuck are you.mp3")
        mixer.music.play()

    widgets = root.grid_slaves()

    for w in widgets:
        w.destroy()

    root.title("The Big Lebowski Soundboard")

    Button(root, text="Aggression", width=15, command=lambda:aggression()).grid(row=1)
    Button(root, text="Close the File", width=15, command=lambda:closethefile()).grid(column=1, row=1)
    Button(root, text="Dios Mo Man", width=15, command=lambda:diosmoman()).grid(column=2, row=1)
    Button(root, text="Dude", width=15, command=lambda:dude()).grid(column=3, row=1)
    Button(root, text="Fuck a Stranger", width=15, command=lambda:stranger()).grid(column=4, row=1)
    Button(root, text="Fucked it up", width=15, command=lambda:fuckeditup()).grid(row=2)
    Button(root, text="Fucking Facist", width=15, command=lambda:facist()).grid(column=1, row=2)
    Button(root, text="Ringer", width=15, command=lambda:ringer()).grid(column=2, row=2)
    Button(root, text="Damn It", width=15, command=lambda:goddamnit()).grid(column=3, row=2)
    Button(root, text="Sweet Prince", width=15, command=lambda:sweetprince()).grid(column=4, row=2)
    Button(root, text="Man Down", width=15, command=lambda:mandowndude()).grid(row=3)
    Button(root, text="How you doing", width=15, command=lambda:howyoudoing()).grid(column=1, row=3)
    Button(root, text="Walrus", width=15, command=lambda:walrus()).grid(column=2, row=3)
    Button(root, text="Suck your cock", width=15, command=lambda:suck()).grid(column=3, row=3)
    Button(root, text="Nobody Fucks Jesus", width=15, command=lambda:fuckswithjesus()).grid(column=4, row=3)
    Button(root, text="Phone is ringing", width=15, command=lambda:phoneisringing()).grid(row=4)
    Button(root, text="Room for more", width=15, command=lambda:roomformore()).grid(column=1, row=4)
    Button(root, text="Shut the Fuck up", width=15, command=lambda:donny()).grid(column=2, row=4)
    Button(root, text="Strike", width=15, command=lambda:strike()).grid(column=3, row=4)
    Button(root, text="Take it Easy", width=15, command=lambda:easydude()).grid(column=4, row=4)
    Button(root, text="Plane has crashed", width=15, command=lambda:crashed()).grid(column=1, row=5)
    Button(root, text="Who are you", width=15, command=lambda:whoareyou()).grid(column=3, row=5)

    Button(root, text="Soundboards", command=lambda:main()).grid(column=2, row=8)

    Button(root, text="Close", command=lambda:close()).grid(column=2, row=10)

def boondocksaints():
    widgets = root.grid_slaves()

    for w in widgets:
        w.destroy()

    root.title("Boondock Saints Soundboard")

    def seveneleven():
        mixer.init()
        mixer.music.load("boondocksaints/\/711.mp3")
        mixer.music.play()

    def angelsprayer():
        mixer.init()
        mixer.music.load("boondocksaints/\/Angels Prayer.mp3")
        mixer.music.play()

    def television():
        mixer.init()
        mixer.music.load("boondocksaints/\/bad television.mp3")
        mixer.music.play()

    def betterluck():
        mixer.init()
        mixer.music.load("boondocksaints/\/better luck with beer.mp3")
        mixer.music.play()

    def bitchdetail():
        mixer.init()
        mixer.music.load("boondocksaints/\/bitch detail.mp3")
        mixer.music.play()

    def theme():
        mixer.init()
        mixer.music.load("boondocksaints/\/boondock saints theme.mp3")
        mixer.music.play()

    def proverbbook():
        mixer.init()
        mixer.music.load("boondocksaints/\/buy you a proverb book.mp3")
        mixer.music.play()

    def courtspeech():
        mixer.init()
        mixer.music.load("boondocksaints/\/court speech.mp3")
        mixer.music.play()

    def evilman():
        mixer.init()
        mixer.music.load("boondocksaints/\/evil man... dead man.mp3")
        mixer.music.play()

    def faimlyprayer():
        mixer.init()
        mixer.music.load("boondocksaints/\/family prayer court scene.mp3")
        mixer.music.play()

    def flipside():
        mixer.init()
        mixer.music.load("boondocksaints/\/flipside.mp3")
        mixer.music.play()

    def fuck():
        mixer.init()
        mixer.music.load("boondocksaints/\/fuck.mp3")
        mixer.music.play()

    def fuckinghappened():
        mixer.init()
        mixer.music.load("boondocksaints/\/i cant believe that just fucking happened.mp3")
        mixer.music.play()

    def killedcat():
        mixer.init()
        mixer.music.load("boondocksaints/\/i killed your cat.mp3")
        mixer.music.play()

    def fuckingfunny():
        mixer.init()
        mixer.music.load("boondocksaints/\/im so fuckin funny ron jeremy.mp3")
        mixer.music.play()

    def goodmen():
        mixer.init()
        mixer.music.load("boondocksaints/\/indifference of good men.mp3")
        mixer.music.play()

    def brotherprayer():
        mixer.init()
        mixer.music.load("boondocksaints/\/saints prayer brothers.mp3")
        mixer.music.play()

    def gaybar():
        mixer.init()
        mixer.music.load("boondocksaints/\/smecker at the gay bar.mp3")
        mixer.music.play()

    def gaylover():
        mixer.init()
        mixer.music.load("boondocksaints/\/smecker smacks his gay lover.mp3")
        mixer.music.play()

    def caffelatte():
        mixer.init()
        mixer.music.load("boondocksaints/\/smecker wants a caffe latte.mp3")
        mixer.music.play()

    def symbology():
        mixer.init()
        mixer.music.load("boondocksaints/\/symbology.mp3")
        mixer.music.play()

    def fagman():
        mixer.init()
        mixer.music.load("boondocksaints/\/the fag man.mp3")
        mixer.music.play()

    def mushmouth():
        mixer.init()
        mixer.music.load("boondocksaints/\/u look like mushmouth from fat albert.mp3")
        mixer.music.play()

    def asskissing():
        mixer.init()
        mixer.music.load("boondocksaints/\/well start the asskissing with you.mp3")
        mixer.music.play()

    Button(root, text="7-11", width=15, command=lambda:seveneleven()).grid(row=1)
    Button(root, text="Angels Prayer", width=15, command=lambda:angelsprayer()).grid(column=1, row=1)
    Button(root, text="Bad TV", width=15, command=lambda:television()).grid(column=2, row=1)
    Button(root, text="Luck with Beer", width=15, command=lambda:betterluck()).grid(column=3, row=1)
    Button(root, text="Bitch Detail", width=15, command=lambda:bitchdetail()).grid(column=4, row=1)
    Button(root, text="Theme", width=15, command=lambda:theme()).grid(column=0, row=2)
    Button(root, text="Proverb Book", width=15, command=lambda:proverbbook()).grid(column=1, row=1)
    Button(root, text="Court Speech", width=15, command=lambda:courtspeech()).grid(column=2, row=1)
    Button(root, text="Evil Man", width=15, command=lambda:evilman()).grid(column=3, row=1)
    Button(root, text="Court Scene", width=15, command=lambda:faimlyprayer()).grid(column=4, row=1)
    Button(root, text="Flipside", width=15, command=lambda:flipside()).grid(column=0, row=2)
    Button(root, text="Fuck", width=15, command=lambda:fuck()).grid(column=1, row=2)
    Button(root, text="Fucking Happened", width=15, command=lambda:fuckinghappened()).grid(column=2, row=2)
    Button(root, text="Killed your cat", width=15, command=lambda:killedcat()).grid(column=3, row=2)
    Button(root, text="So Fucking Funny", width=15, command=lambda:fuckingfunny()).grid(column=4, row=2)
    Button(root, text="Indifference", width=15, command=lambda:goodmen()).grid(column=0, row=3)
    Button(root, text="Saints Prayer", width=15, command=lambda:brotherprayer()).grid(column=1, row=3)
    Button(root, text="Gay Bar", width=15, command=lambda:gaybar()).grid(column=2, row=3)
    Button(root, text="Gay Lover", width=15, command=lambda:gaylover()).grid(column=3, row=3)
    Button(root, text="Caffe Latte", width=15, command=lambda:caffelatte()).grid(column=4, row=3)
    Button(root, text="Symbology", width=15, command=lambda:symbology()).grid(column=0, row=4)
    Button(root, text="Fag Man", width=15, command=lambda:fagman()).grid(column=1, row=4)
    Button(root, text="MushMouth", width=15, command=lambda:mushmouth()).grid(column=3, row=4)
    Button(root, text="AssKissing", width=15, command=lambda:asskissing()).grid(column=4, row=4)

    Button(root, text="Soundboards", command=lambda:main()).grid(column=2, row=8)

    Button(root, text="Close", command=lambda:close()).grid(column=2, row=10)

def chucky():
    widgets = root.grid_slaves()

    for w in widgets:
        w.destroy()

    root.title("Chucky Soundboard")

    def cameontome():
        mixer.init()
        mixer.music.load("chucky/\/came on to me.mp3")
        mixer.music.play()

    def chuckyattacks():
        mixer.init()
        mixer.music.load("chucky/\/chucky attacks.mp3")
        mixer.music.play()

    def chuckysback():
        mixer.init()
        mixer.music.load("chucky/\/chuckys back.mp3")
        mixer.music.play()

    def chuckyschant():
        mixer.init()
        mixer.music.load("chucky/\/chuckys chant.mp3")
        mixer.music.play()

    def chuckylaugh1():
        mixer.init()
        mixer.music.load("chucky/\/chuckys laugh 1.mp3")
        mixer.music.play()

    def chuckylaugh2():
        mixer.init()
        mixer.music.load("chucky/\/chuckys laugh 2.mp3")
        mixer.music.play()

    def chuckylaugh3():
        mixer.init()
        mixer.music.load("chucky/\/chuckys laugh 3.mp3")
        mixer.music.play()

    def cometopapa():
        mixer.init()
        mixer.music.load("chucky/\/come to papa.mp3")
        mixer.music.play()

    def hidethesoul():
        mixer.init()
        mixer.music.load("chucky/\/hide the soul.mp3")
        mixer.music.play()

    def cutitup():
        mixer.init()
        mixer.music.load("chucky/\/soundtrack cut it up.mp3")
        mixer.music.play()

    def mother():
        mixer.init()
        mixer.music.load("chucky/\/soundtrack mother.mp3")
        mixer.music.play()

    def paparazzos():
        mixer.init()
        mixer.music.load("chucky/\/soundtrack paparazzos delight.mp3")
        mixer.music.play()

    def timetoplay():
        mixer.init()
        mixer.music.load("chucky/\/time to play.mp3")
        mixer.music.play()

    def youremine():
        mixer.init()
        mixer.music.load("chucky/\/youre mine.mp3")
        mixer.music.play()

    Button(root, text="Came on to me", width=15, command=lambda:cameontome()).grid(column=0, row=1)
    Button(root, text="Chucky Attacks", width=15, command=lambda:chuckyattacks()).grid(column=1, row=1)
    Button(root, text="Chucky's Back", width=15, command=lambda:chuckysback()).grid(column=2, row=1)
    Button(root, text="Chucky's Chant", width=15, command=lambda:chuckyschant()).grid(column=3, row=1)
    Button(root, text="Chucky's Laugh 1", width=15, command=lambda:chuckylaugh1()).grid(column=0, row=2)
    Button(root, text="Chucky's Laugh 2", width=15, command=lambda:chuckylaugh2()).grid(column=1, row=2)
    Button(root, text="Chucky's Laugh 3", width=15, command=lambda:asskissing()).grid(column=2, row=2)
    Button(root, text="Come to Papa", width=15, command=lambda:cometopapa()).grid(column=3, row=2)
    Button(root, text="Hide the Soul", width=15, command=lambda:hidethesoul()).grid(column=0, row=3)
    Button(root, text="Cut it up", width=15, command=lambda:cutitup()).grid(column=1, row=3)
    Button(root, text="Mother", width=15, command=lambda:mother()).grid(column=2, row=3)
    Button(root, text="Paprazzo's Delight", width=15, command=lambda:paparazzos()).grid(column=3, row=3)
    Button(root, text="Time to Play", width=15, command=lambda:timetoplay()).grid(column=0, row=4)
    Button(root, text="You're Mine", width=15, command=lambda:youremine()).grid(column=3, row=4)

    Button(root, text="Soundboards", command=lambda:main()).grid(column=1, columnspan=2, row=8)

    Button(root, text="Close", command=lambda:close()).grid(column=1, columnspan=2, row=10)

def armyofdarkness():
    widgets = root.grid_slaves()

    for w in widgets:
        w.destroy()

    root.title("Army of Darkness Soundboard")

    def century():
        mixer.init()
        mixer.music.load("darkness/\/21st century.mp3")
        mixer.music.play()

    def thirteen():
        mixer.init()
        mixer.music.load("darkness/\/1300 ad.mp3")
        mixer.music.play()

    def badash():
        mixer.init()
        mixer.music.load("darkness/\/bad ash.mp3")
        mixer.music.play()

    def bonehead():
        mixer.init()
        mixer.music.load("darkness/\/bonehead.mp3")
        mixer.music.play()  

    def boomstick():
        mixer.init()
        mixer.music.load("darkness/\/boomstick.mp3")
        mixer.music.play()    

    def braggarts():
        mixer.init()
        mixer.music.load("darkness/\/braggarts.mp3")
        mixer.music.play()             

    def cometopapa():
        mixer.init()
        mixer.music.load("darkness/\/come to papa.mp3")
        mixer.music.play()          

    def damnwords():
        mixer.init()
        mixer.music.load("darkness/\/damn words.mp3")
        mixer.music.play()       

    def deadites():
        mixer.init()
        mixer.music.load("darkness/\/deadites.mp3")
        mixer.music.play()            

    def fancypants():
        mixer.init()
        mixer.music.load("darkness/\/fancypants.mp3")
        mixer.music.play()        

    def filthybones():
        mixer.init()
        mixer.music.load("darkness/\/filthy bones.mp3")
        mixer.music.play()        

    def getanaxe():
        mixer.init()
        mixer.music.load("darkness/\/get an axe.mp3")
        mixer.music.play()    

    def getsome():
        mixer.init()
        mixer.music.load("darkness/\/get some.mp3")
        mixer.music.play()           

    def goodbad():
        mixer.init()
        mixer.music.load("darkness/\/good bad.mp3")
        mixer.music.play()    

    def groovy():
        mixer.init()
        mixer.music.load("darkness/\/groovy.mp3")
        mixer.music.play()            

    def gumears():
        mixer.init()
        mixer.music.load("darkness/\/gum ears.mp3")
        mixer.music.play()        

    def hailtotheking():
        mixer.init()
        mixer.music.load("darkness/\/hail to the king.mp3")
        mixer.music.play()    

    def ash():
        mixer.init()
        mixer.music.load("darkness/\/my name is ash.mp3")
        mixer.music.play()            

    def sardinecan():
        mixer.init()
        mixer.music.load("darkness/\/sardine can.mp3")
        mixer.music.play()    

    def shebitch():
        mixer.init()
        mixer.music.load("darkness/\/she bitch.mp3")
        mixer.music.play()            

    def shewitch():
        mixer.init()
        mixer.music.load("darkness/\/she witch.mp3")
        mixer.music.play()        

    def shoelace():
        mixer.init()
        mixer.music.load("darkness/\/shoe lace.mp3")
        mixer.music.play()      

    def shopsmart1():
        mixer.init()
        mixer.music.load("darkness/\/shop smart.mp3")
        mixer.music.play()       

    def shopsmart2():
        mixer.init()
        mixer.music.load("darkness/\/shop smart 2.mp3")
        mixer.music.play()     

    def jerk():
        mixer.init()
        mixer.music.load("darkness/\/sound like a jerk.mp3")
        mixer.music.play()              

    Button(root, text="1300 AD", width=15, command=lambda:thirteen()).grid(column=0, row=1)
    Button(root, text="Bad Ash", width=15, command=lambda:badash()).grid(column=1, row=1)
    Button(root, text="Bonehead", width=15, command=lambda:bonehead()).grid(column=2, row=1)
    Button(root, text="Boomstick", width=15, command=lambda:boomstick()).grid(column=3, row=1)
    Button(root, text="Braggarts", width=15, command=lambda:braggarts()).grid(column=4, row=1)
    Button(root, text="Come to Papa", width=15, command=lambda:cometopapa()).grid(column=0, row=2)
    Button(root, text="Damn Words", width=15, command=lambda:damnwords()).grid(column=1, row=2)
    Button(root, text="Deadites", width=15, command=lambda:deadites()).grid(column=2, row=2)
    Button(root, text="Fancypants", width=15, command=lambda:fancypants()).grid(column=3, row=2)
    Button(root, text="Filthy Bones", width=15, command=lambda:filthybones()).grid(column=4, row=2)
    Button(root, text="Get an axe", width=15, command=lambda:getanaxe()).grid(column=0, row=3)
    Button(root, text="Get Some", width=15, command=lambda:getsome()).grid(column=1, row=3)
    Button(root, text="Good Bad", width=15, command=lambda:goodbad()).grid(column=2, row=3)
    Button(root, text="Groovy", width=15, command=lambda:groovy()).grid(column=3, row=3)
    Button(root, text="Gum Ears", width=15, command=lambda:gumears()).grid(column=4, row=3)
    Button(root, text="Hail to the King", width=15, command=lambda:hailtotheking()).grid(column=0, row=4)
    Button(root, text="My name is Ash", width=15, command=lambda:ash()).grid(column=1, row=4)
    Button(root, text="Sardine Can", width=15, command=lambda:sardinecan()).grid(column=2, row=4)
    Button(root, text="She Bitch", width=15, command=lambda:shebitch()).grid(column=3, row=4)
    Button(root, text="She Witch", width=15, command=lambda:shewitch()).grid(column=4, row=4)
    Button(root, text="Shoe Lace", width=15, command=lambda:shoelace()).grid(column=0, row=5)
    Button(root, text="Shop Smart 1", width=15, command=lambda:shopsmart1()).grid(column=1, row=5)
    Button(root, text="Shop Smart 2", width=15, command=lambda:shopsmart2()).grid(column=2, row=5)
    Button(root, text="Sound like a jerk", width=15, command=lambda:jerk()).grid(column=3, row=5)
    Button(root, text="21st Century", width=15, command=lambda:century()).grid(column=4, row=5)
    
    Button(root, text="Soundboards", command=lambda:main()).grid(column=2, row=8)

    Button(root, text="Close", command=lambda:close()).grid(column=2, row=10)

def waiting():

    widgets = root.grid_slaves()

    for w in widgets:
        w.destroy()

    root.title("Waiting Soundboard")

    def alzheimers():
        mixer.init()
        mixer.music.load("waiting/\/Alzheimers cant be all bad.mp3")
        mixer.music.play()

    def anal():
        mixer.init()
        mixer.music.load("waiting/\/Anal sex.mp3")
        mixer.music.play()

    def extraordinary():
        mixer.init()
        mixer.music.load("waiting/\/Difference between ordinary and extraordinary.mp3")
        mixer.music.play()

    def shenaniganz():
        mixer.init()
        mixer.music.load("waiting/\/Eat at Shenaniganz.mp3")
        mixer.music.play()

    def awefulfood():
        mixer.init()
        mixer.music.load("waiting/\/Food was awful.mp3")
        mixer.music.play()

    def malenudity():
        mixer.init()
        mixer.music.load("waiting/\/Frontal male nudity.mp3")
        mixer.music.play()

    def lesbian():
        mixer.init()
        mixer.music.load("waiting/\/Glad Im a lesbian.mp3")
        mixer.music.play()

    def senile():
        mixer.init()
        mixer.music.load("waiting/\/Going senile.mp3")
        mixer.music.play()

    def hardjob():
        mixer.init()
        mixer.music.load("waiting/\/How hard is ur job.mp3")
        mixer.music.play()

    def slutty():
        mixer.init()
        mixer.music.load("waiting/\/I am slutty.mp3")
        mixer.music.play()

    def bornblind():
        mixer.init()
        mixer.music.load("waiting/\/If you had been born blind.mp3")
        mixer.music.play()

    def immoral():
        mixer.init()
        mixer.music.load("waiting/\Immoral/.mp3")
        mixer.music.play()

    def childmonty():
        mixer.init()
        mixer.music.load("waiting/\/Monty was a child.mp3")
        mixer.music.play()

    def saladbacon():
        mixer.init()
        mixer.music.load("waiting/\/No bacon on the salad.mp3")
        mixer.music.play()

    def overcooked():
        mixer.init()
        mixer.music.load("waiting/\/Overcooked.mp3")
        mixer.music.play()

    def personalethics():
        mixer.init()
        mixer.music.load("waiting/\/Personal ethics and the law.mp3")
        mixer.music.play()

    def values():
        mixer.init()
        mixer.music.load("waiting/\/Project own values.mp3")
        mixer.music.play()

    def genitals():
        mixer.init()
        mixer.music.load("waiting/\/Referencing your genitals.mp3")
        mixer.music.play()

    def happybirthday():
        mixer.init()
        mixer.music.load("waiting/\/Shenaniganz Happy Birthday.mp3")
        mixer.music.play()

    def illegal():
        mixer.init()
        mixer.music.load("waiting/\/Shes illegal.mp3")
        mixer.music.play()

    def taintedyouth():
        mixer.init()
        mixer.music.load("waiting/\/Tainted youths end up being perverts.mp3")
        mixer.music.play()

    def whiskey():
        mixer.init()
        mixer.music.load("waiting/\/Whiskey.mp3")
        mixer.music.play()

    Button(root, text="Alzheimers", width=15, command=lambda:alzheimers()).grid(column=0, row=1)
    Button(root, text="Anal Sex", width=15, command=lambda:anal()).grid(column=1, row=1)
    Button(root, text="Exraordinary", width=15, command=lambda:extraordinary()).grid(column=2, row=1)
    Button(root, text="Eat Shenanigans", width=15, command=lambda:shenaniganz()).grid(column=3, row=1)
    Button(root, text="Awful Food", width=15, command=lambda:awefulfood()).grid(column=4, row=1)
    Button(root, text="Male Nudity", width=15, command=lambda:malenudity()).grid(column=0, row=2)
    Button(root, text="Lesbian", width=15, command=lambda:lesbian()).grid(column=1, row=2)
    Button(root, text="Going Senile", width=15, command=lambda:senile()).grid(column=2, row=2)
    Button(root, text="Hard Job", width=15, command=lambda:hardjob()).grid(column=3, row=2)
    Button(root, text="I'm Slutty", width=15, command=lambda:slutty()).grid(column=4, row=2)
    Button(root, text="Born Blind", width=15, command=lambda:bornblind()).grid(column=0, row=3)
    Button(root, text="Immoral", width=15, command=lambda:immoral()).grid(column=1, row=3)
    Button(root, text="Child Monty", width=15, command=lambda:childmonty()).grid(column=2, row=3)
    Button(root, text="Bacon on the Salad", width=15, command=lambda:saladbacon()).grid(column=3, row=3)
    Button(root, text="Overcooked", width=15, command=lambda:overcooked()).grid(column=4, row=3)
    Button(root, text="Personal Ethics", width=15, command=lambda:personalethics()).grid(column=0, row=4)
    Button(root, text="Values", width=15, command=lambda:values()).grid(column=1, row=4)
    Button(root, text="Refrence Genitals", width=15, command=lambda:genitals()).grid(column=2, row=4)
    Button(root, text="Happy Birthday", width=15, command=lambda:happybirthday()).grid(column=3, row=4)
    Button(root, text="Shes Illegal", width=15, command=lambda:illegal()).grid(column=4, row=4)
    Button(root, text="Tainted Youths", width=15, command=lambda:taintedyouth()).grid(column=0, row=5)
    Button(root, text="Whiskey", width=15, command=lambda:whiskey()).grid(column=4, row=5)
  
    Button(root, text="Soundboards", command=lambda:main()).grid(column=2, columnspan=1, row=8)

    Button(root, text="Close", command=lambda:close()).grid(column=2, columnspan=1, row=10)
    

def hal():

    widgets = root.grid_slaves()

    for w in widgets:
        w.destroy()

    root.title("HAL 9000 Soundboard")

    def better():
        mixer.init()
        mixer.music.load("hal/\/better.mp3")
        mixer.music.play()

    def cantdothat():
        mixer.init()
        mixer.music.load("hal/\/cant do that.mp3")
        mixer.music.play()

    def daisy():
        mixer.init()
        mixer.music.load("hal/\/daisy.. daisy.mp3")
        mixer.music.play()

    def halerror():
        mixer.init()
        mixer.music.load("hal/\/errpr.mp3")
        mixer.music.play()

    def foolproof():
        mixer.init()
        mixer.music.load("hal/\/foolproof.mp3")
        mixer.music.play()

    def game():
        mixer.init()
        mixer.music.load("hal/\/game.mp3")
        mixer.music.play()

    def goodbye():
        mixer.init()
        mixer.music.load("hal/\/good bye.mp3")
        mixer.music.play()

    def goodevening():
        mixer.init()
        mixer.music.load("hal/\/good evening.mp3")
        mixer.music.play()

    def iamhal():
        mixer.init()
        mixer.music.load("hal/\/i am hal.mp3")
        mixer.music.play()

    def mindisgoing():
        mixer.init()
        mixer.music.load("hal/\/my mind is going.mp3")
        mixer.music.play()

    def personalquestion():
        mixer.init()
        mixer.music.load("hal/\/personal question.mp3")
        mixer.music.play()

    def disconnect():
        mixer.init()
        mixer.music.load("hal/\/planning to disconnect me.mp3")
        mixer.music.play()

    def stresspill():
        mixer.init()
        mixer.music.load("hal/\/stress pill.mp3")
        mixer.music.play()

    def doingdave():
        mixer.init()
        mixer.music.load("hal/\/what do you think our doing dave.mp3")
        mixer.music.play()

    Button(root, text="Better", width=15, command=lambda:better()).grid(column=0, row=1)
    Button(root, text="Can't Do That", width=15, command=lambda:cantdothat()).grid(column=1, row=1)
    Button(root, text="Daisy...Daisy", width=15, command=lambda:daisy()).grid(column=2, row=1)
    Button(root, text="Error", width=15, command=lambda:halerror()).grid(column=3, row=1)
    Button(root, text="FoolProof", width=15, command=lambda:foolproof()).grid(column=4, row=1)
    Button(root, text="Game", width=15, command=lambda:game()).grid(column=0, row=2)
    Button(root, text="Good Bye", width=15, command=lambda:goodbye()).grid(column=1, row=2)
    Button(root, text="Good Evening", width=15, command=lambda:goodevening()).grid(column=2, row=2)
    Button(root, text="I am HAL", width=15, command=lambda:iamhal()).grid(column=3, row=2)
    Button(root, text="My Mind is Going", width=15, command=lambda:mindisgoing()).grid(column=4, row=2)
    Button(root, text="Personal Question", width=15, command=lambda:personalquestion()).grid(column=0, row=3)
    Button(root, text="Disconnect Me", width=15, command=lambda:disconnect()).grid(column=1, row=3)
    Button(root, text="Stress Pill", width=15, command=lambda:stresspill()).grid(column=3, row=3)
    Button(root, text="What doing Dave?", width=15, command=lambda:doingdave()).grid(column=4, row=3)

    Button(root, text="Soundboards", command=lambda:main()).grid(column=2, columnspan=1, row=8)

    Button(root, text="Close", command=lambda:close()).grid(column=2, columnspan=1, row=10)
    
    

def main():
    widgets = root.grid_slaves()

    for w in widgets:
        w.destroy()

    root.title("Soundboards")

    Button(root, text="The Big Lebowski", width=15, command=lambda:lebowski()).grid(column=0, columnspan=1, row=0)
    Button(root, text="Boondock Saints", width=15, command=lambda:boondocksaints()).grid(column=1, columnspan=1, row=0)
    Button(root, text="Army of Darkness", width=15, command=lambda:armyofdarkness()).grid(column=2, columnspan=1, row=0)
    Button(root, text="Chucky", width=15, command=lambda:chucky()).grid(column=0, columnspan=1, row=2)
    Button(root, text="Waiting", width=15, command=lambda:waiting()).grid(column=1, columnspan=1, row=2)
    Button(root, text="HAL 9000", width=15, command=lambda:hal()).grid(column=2, columnspan=1, row=2)
    Button(root, text="Close", width=15, command=lambda:close()).grid(column=1, columnspan=1, row=4)
    Button(root, text="Random Sound", width=15, command=lambda:randomsound()).grid(column=1, columnspan=1, row=3)
    
main()
root.mainloop()