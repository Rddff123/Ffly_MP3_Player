from tkinter import *
import pygame
from pygame import *
from tkinter import messagebox , filedialog as fd
from os import *
tk = Tk()
#----------------------------------Pre-setting-------------------------------------------#
tk.geometry('1000x600')
tk.title("Ffly MP3 Player")
tk.resizable(False,False)


#----------------------------------------------------------------------------------------#

#if love != life:
#   love_value=0
        
#--------------------------------Main Content--------------------------------------------#

#mp3_location = r"C:\Users\Andy\Downloads\Never Gonna Give You Up.mp3"
# Initialize the mixer module
pygame.init()
pygame.mixer.init()      #Double Initialization, for convenient coding 

playing_list_empty = True       #determine if play list is empty, or else your ear will... BOOM!
playing_list = []      #Play list simply
ifPause_mp3 = False      #For pausing and unpausing mp3
mp3_location = ''


def play_mp3():
    global playing_list_empty, playing_list      #bring playing_list_empty, playing_list    to the def
    mp3_location = fd.askopenfilename()
    if mp3_location == '':
        messagebox.showerror("You do not choose a file","You need to choose a file to play!")      # If user cancel action, pop this
        playing_list_empty = True       
    else:
        if playing_list_empty == False:
            stop_mp3        #determine if play list is empty, or else your ear will... BOOM!
        pygame.mixer.music.load(mp3_location)      #load location of mp3
        pygame.mixer.music.play()          #play the mp3
        playing_list_empty = False      #change to false

def stop_mp3():
    pygame.mixer.music.stop()     #stop mp3

def pause_mp3():
    global ifPause_mp3
    if ifPause_mp3 == True:
        mixer.music.unpause()
    else:
        mixer.music.pause()
    ifPause_mp3 = not ifPause_mp3




'''file_path = getcwd()
file_path = file_path + "\Music"





makedirs(file_path)
file_path = file_path + ""

def play_mp3():
   makedirs(file_path)'''  #Testing Code(Beta ;)?)









#------------------------------------GUI-------------------------------------------------#
play_button = Button(text="Play",command=play_mp3)    #Set play button
play_button.place(x=500,y=500,height=30,width=50)

play_button = Button(text="Pause",command=pause_mp3)     #Set Pause button
play_button.place(x=500+70,y=500,height=30,width=50)
#----------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------#
tk.mainloop()