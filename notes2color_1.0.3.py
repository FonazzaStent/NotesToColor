"""Notes to Color 1.0.3 - Convert melodies to colors.
Copyright (C) 2024  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

from tkinter import *
from colorsys import rgb_to_hsv, hsv_to_rgb
import sys

root=Tk()
root.geometry("250x350")
root.resizable(0,0)
coldisplay=Frame(root)
coldisplay.place(x=0,y=0,height=250,width=250)
root.title("Notes to Color")
RGBvalues= Text(root)
RGBvalues.place(x=5,y=260,height=30,width=240)
HEXvalue=Text(root)
HEXvalue.place(x=5,y=300,height=30,width=240)

rainbow=[(255,0,255),(128,0,255),(64,0,255),(32,0,255),(0,0,255),(0,255,0),(128,255,0),(255,255,0),(255,128,0),(255,64,0),(255,32,0),(255,0,0)]
notes=['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']
notescap=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
R=0
G=0
B=0
Rtot=0
Gtot=0
Btot=0
noteinput=''
total=0
try:
    file=str(sys.argv[1])
except:
    file='melody.txt'

def noteinputfun():
    global noteinput
    noteinput=input("Note: ")
    print ('\n')

def addnote():
    global coldisplay
    global total
    global R
    global G
    global B
    global Rav
    global Gav
    global Bav
    global Rtot
    global Gtot
    global Btot
    total=total+1
    col=rainbow[notes.index(melodynote)]
    R= col[0]
    G=col[1]
    B=col[2]
    Rtot=Rtot+R
    Gtot=Gtot+G
    Btot=Btot+B
    Rav=Rtot/total
    Gav=Gtot/total
    Bav=Btot/total
    Rav=int(Rav)
    Gav=int(Gav)
    Bav=int(Bav)

def create_context_menu():
    global menu
    menu = Menu(root, tearoff = 0)
    menu.add_command(label="Copy", command=copy_text)
    root.bind("<Button-3>", context_menu)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()
        
def copy_text():
    HEXvalue.event_generate(("<<Copy>>"))

create_context_menu()
melodyfile=open(file,'r')
melody=melodyfile.read()
melodynotes=melody.split()
melodyfile.close()

for melodynote in melodynotes:
    counter=0
    for note in notes:
        if melodynote==note:
            addnote()
        if melodynote==notescap[notes.index(note)]:
            melodynote=melodynote.lower()
            addnote()

        counter=counter+1

#print ('R:',Rav,'G:',Gav,'B:',Bav)
RGBstring=('R:',Rav,'G:',Gav,'B:',Bav)
RGBvalues.insert(END,RGBstring)
RGBvalues.configure(state="disabled")
hex_color = ('#%02x%02x%02x' % (Rav, Gav, Bav))
HEXvalue.insert(END,hex_color)
HEXvalue.configure(state="disabled")
#print ('HEX:',hex_color)
coldisplay.configure(bg=hex_color)
        
root.mainloop()
