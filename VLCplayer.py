from tkinter import *
from numpy import loadtxt
from pygame import *
import glob

i = 0

radio_stations = glob.glob("lebowski\/*")
print (radio_stations)

root = Tk()
root.title('Internet Radio')
root.configure(background='royal blue')

def previous_station():
    global i
    global radio_stations
    global now_playing
    if i == 0: 
        i = len(radio_stations) - 1
    else:
        i = i - 1
    now_playing = Label(root,bg='gray', fg='black', text=radio_stations[i], width=25, padx=5, pady=5).grid(column=0,columnspan=5, row=0)

def play_stop():
    global radio_stations
    now_playing = Label(root,bg='gray', fg='black', text=radio_stations[i], width=25, padx=5, pady=5).grid(column=0,columnspan=5, row=0)
    playing = False
    #Find some method for playing URLS
    
    if playing == False:
        mixer.init()
        mixer.music.load(radio_stations[i])
        mixer.music.play()
    else:
        mixer.music.stop()
        playing = False


def next_stations():
    global i
    global radio_stations
    global now_playing
    if i == (len(radio_stations) -1):
        i = 0
    else: 
        i = i + 1
    now_playing = Label(root,bg='gray', fg='black', text=radio_stations[i], width=25, padx=5, pady=5).grid(column=0,columnspan=5, row=0)
    
def close_program():
    root.destroy()



previous = Button(root, bg='dark red', fg='white',width=8, text='Previous', command=lambda:previous_station())
previous.grid(column=0, row=2,)

play = Button(root, bg='dark red', fg='white',width=8, text='Play/Stop', command=lambda:play_stop())
play.grid(column=2, row=2)

next_station = Button(root, bg='dark red', fg='white',width=8, text='Next', command=lambda:next_stations())
next_station.grid(column=4, row=2)

close = Button(root, bg='dark red', fg='white',text='Exit', command=lambda:close_program())
close.grid(column=2,columnspan=2, row=6, padx=10, pady=10)



root.mainloop()