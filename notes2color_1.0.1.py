"""Notes to Color 1.0.1 - Convert melodies to colors.
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

root=Tk()
root.geometry("250x250")
root.resizable(0,0)
coldisplay=Frame(root)
coldisplay.place(x=0,y=0,height=250,width=250)
root.title("Color")

rainbow=[(255,0,255),(128,0,255),(0,0,255),(0,255,0),(255,255,0),(255,128,0),(255,0,0)]
notes=['c','d','e','f','g','a','b']
notescap=['C','D','E','F','G','A','B']
R=0
G=0
B=0
Rtot=0
Gtot=0
Btot=0
noteinput=''
total=0


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
    global Rtot
    global Gtot
    global Btot
    total=total+1
    col=rainbow[notes.index(noteinput)]
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
    print ('R:',Rav,'G:',Gav,'B:',Bav)
    hex_color = ('#%02x%02x%02x' % (Rav, Gav, Bav))
    print ('HEX:',hex_color)
    coldisplay.configure(bg=hex_color)



while noteinput!='quit':
    noteinputfun()
    counter=0
    for note in notes:
        if noteinput==note:
            addnote()

        counter=counter+1
        if noteinput=='new':
            total=0
            Rtot=0
            Gtot=0
            Btot=0
        if noteinput=='quit':
            quit()

root.mainloop()
