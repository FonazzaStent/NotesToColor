"""Notes to Color 1.0.0 - Convert melodies to colors.
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

def ablend(a, fg, bg):
    return ((1-a)*fg[0]+a*bg[0],
            (1-a)*fg[1]+a*bg[1],
            (1-a)*fg[2]+a*bg[2])

# replace ablend with hsvblend
def hsvblend(a, fg, bg):
    fgh = rgb_to_hsv(fg[0]/255.,fg[1]/255.,fg[2]/255.)
    bgh = rgb_to_hsv(bg[0]/255.,bg[1]/255.,bg[2]/255.)
    ret = hsv_to_rgb(
            (1-a)*fgh[0]+a*bgh[0],
            (1-a)*fgh[1]+a*bgh[1],
            (1-a)*fgh[2]+a*bgh[2])
    return ret[0]*255,ret[1]*255,ret[2]*255

rainbow=[(255,0,255),(128,0,255),(0,0,255),(0,255,0),(255,255,0),(255,128,0),(255,0,0)]
notes=['c','d','e','f','g','a','b']
notescap=['C','D','E','F','G','A','B']
notescount=[0,0,0,0,0,0,0]
percents=[0,0,0,0,0,0,0]
checkinput=False
firstnote=True
oldcol=(0,0,0)
num=8.0
noteinput=''
fg=(255, 255, 0)
bg=(128,128,128)
total=0


def noteinputfun():
    global noteinput
    noteinput=input("Note: ")
    print ('\n')
    


def addnote():
    global fg
    global bg
    global firstnote
    global oldcol
    global coldisplay
    global total
    #print (notes.index(noteinput))
    fg=rainbow[notes.index(noteinput)]
    if firstnote==True:
        bg=fg
        firstnote=False
    else:
        #print('bg ok')
        bg=oldcol

    col = hsvblend(.5, fg, bg)
    #print (bg,fg,col)
    notescount[notes.index(noteinput)]=notescount[notes.index(noteinput)]+1
    hex_color = '#%02x%02x%02x' % (int(col[0]), int(col[1]), int(col[2]))
    coldisplay.configure(bg=hex_color)
    print("Color: ",hex_color+'\n')
    oldcol=col
    for count in notescount:
        total=total+count
    for i in range (0, 7):
        percents[i]=int((notescount[i]/total)*100)
    #print (total,notescount, percents)
    for n in range (0,7):
        print (str(notescap[n])+": "+str(notescount[n]), str(percents[n])+"%")
    total=0
    print ('\n')



while noteinput!='quit':
    noteinputfun()
    checkinput=False
    counter=0
    for note in notes:
        if noteinput==note:
            checkinput=True
            addnote()
            checkinput=False
        counter=counter+1
        if noteinput=='new':
            notescount=[0,0,0,0,0,0,0]
            percents=[0,0,0,0,0,0,0]
            firstnote=True
        if noteinput=='quit':
            quit()

root.mainloop()
