#--------------------------------Imports-----------------------------------

import pygame, time
from pygame.locals import *
from sys import exit
from Tkinter import *

#--------------------------------init---------------------------------------
PATH = open("C:\PATH.txt", "r")
PATH = PATH.read()
picPATH = PATH + "res\\pic"
marPATH = PATH + "res\\market"
sndPATH = PATH + "res\\soundFX"
#--------------------------------Image Path--------------------------------
initscreen = picPATH +"\\init_scr.png"
bkg1 = picPATH +"\\under.png"
map1280 = picPATH +"\\map1280.png"
map800 = picPATH + "\\map800.png"
sp_home = picPATH +"\\sp_home.png"

loading = picPATH +"\loading.png"
error = picPATH +"\\error.png"
success = picPATH +"\\success.png"

sp_e = picPATH +"\\sp_e.png"
mp_e = picPATH +"\\mp_e.png"
choose = picPATH +"\\choose.png"

global mar_itm
mar_itm = marPATH +"\\mar_itmv1v.png"

area1 = picPATH +"\\marea1.png"

marketdock = picPATH +"\\market_dock.png"

buymenu = picPATH +"\\mbuymenu.png"

darken = picPATH +"\\darken.png"

dbbg = picPATH +"\\dbbg.png"
orgbg = picPATH +"\\orgbg.png"
#--------------------------------Image Load--------------------------------

#backgrounds
bkg1 = pygame.image.load(bkg1)
sp_home = pygame.image.load(sp_home)    
map1280 = pygame.image.load(map1280)
map800 = pygame.image.load(map800)
darken = pygame.image.load(darken)
initscreen = pygame.image.load(initscreen)

#Menu item_g

sp_e = pygame.image.load(sp_e)
mp_e = pygame.image.load(mp_e)
choose = pygame.image.load(choose)

#Notify
loading = pygame.image.load(loading)
error = pygame.image.load(error)
success = pygame.image.load(success)

#Market item
maritm_v1 = pygame.image.load(mar_itm)
marketdock = pygame.image.load(marketdock)

#Market Control
buymenu = pygame.image.load(buymenu)

#areas
area1 = pygame.image.load(area1)

#World DataBase
dbbg = pygame.image.load(dbbg)

#Organizer
orgbg = pygame.image.load(orgbg)

#--------------------------------Game Var----------------------------------
 #menu items_var

global i_itm1, i_itm2, i_itm3, i_itm4
i_itm1 = None
i_itm2 = None
i_itm3 = None
i_itm4 = None

global started
started = False

loaded = False

inited = False
chy = 200

global mu, md
mu, md = False, True    #determine if choosebar in menu can be moved or no

global itm1_s, itm2_s
itm1_s, itm2_s= True, False    #Menu item, _s for selected



market_type_menu = False

weapon_num = 0

global new_user

#-------------------------------Function Sets------------------------------

        
        

def menu_choose():
    pass
    
                
    
def playmusic(filename):    #Format OGG only
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def initialize():
   # playmusic("initmusic.ogg")
    #pygame.time.delay(2000)
    inited = True
    

def user_login():
    def save():
        inp = entry.get()
        print inp
        inpf = open(r"C:\gbuserfile.txt", "w")
        inpf.write(inp)
        inpf.close()
        return

    win = Tk()
    win.title("Welcom To Global Battle! Please Register:")
    win.geometry("600x200")
    frame = Frame(win)
    frame.pack()
    var = StringVar()
    label = Label(frame, textvariable = var)
    label.pack()
    entry = Entry(frame, textvariable = var)
    entry.pack()
    CN = Button(frame, text = "Crate New User", command = save)
    CN.pack()
    note = Label(frame, text = '''
Welcome!
1.Type your name in the input box, then click 'Creat New User'
2.After step 1, close this window, and ENJOY!''')
    note.pack()
    win.mainloop()
    
