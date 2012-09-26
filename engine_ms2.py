

#Release 5 Milestone 2(pre-ALPHA)
#--------------------------------------Import------------------------------
import pygame, time, GDB
from pygame.locals import *
from sys import exit
from uti2 import *
from random import randint
#--------------------------------------Game--------------------------------
pygame.init()

pygame.mouse.set_visible(True)

screen = pygame.display.set_mode((1280,720), pygame.DOUBLEBUF|pygame.FULLSCREEN, 32)
pygame.display.set_caption("Global Battle MS2")

initialize()
playmusic(sndPATH + "\song.ogg")
screen.blit(initscreen, (0,0))
pygame.display.flip()
pygame.time.wait(3000)

#------------------------------------Login&Register------------------------
try:
    userfile = open("C:\gbuserfile.txt", "r")
    userfile = userfile.read()
    print userfile
except IOError:
    user_login()

#------------------------------------Function------------------------------
def market_tool(operation):
    global maritm_v1, mar_itm, info_mar_itm, wname, wmoney, wdamage
    if operation == "add":
        mar_itm = mar_itm.split("v")
        NOP = mar_itm[1]
        NOP = int(NOP)
        NOP += 1
        if not NOP == 5:  #LIMIT HERE---------------------------- (Limit = Amount-1)
            NOP = str(NOP)
            
            mar_itm =  marPATH +"\mar_itmv" + NOP + "v.png"   #pic change
            
            info_mar_itm =  marPATH +"\mar_itmv" + NOP + "v.txt" #info file change
            info_mar_itm = open(info_mar_itm, "r")

            #-----Type Get
            wtype = info_mar_itm.read()
            wtype = wtype.split(",")
            wname = wtype[0]
            wmoney = int(wtype[1])
            wdamage = int(wtype[2])
            wtype = wtype[3]
            print wtype
            print wname
            #/----Type Get

            maritm_v1 = pygame.image.load(mar_itm)
        else:
            
            NOP = 1
            NOP = str(NOP)
            
            mar_itm =  marPATH +"\mar_itmv" + NOP + "v.png"  #pic change
            
            info_mar_itm =  marPATH +"\mar_itmv" + NOP + "v.txt" #info file change
            info_mar_itm = open(info_mar_itm, "r")

            #-----Type Get
            wtype = info_mar_itm.read()
            wtype = wtype.split(",")
            wname = wtype[0]            
            wmoney = int(wtype[1])
            wdamage = int(wtype[2])
            wtype = wtype[3]
            print wtype
            print wname
            #/----Type Get

            maritm_v1 = pygame.image.load(mar_itm)
    if operation == "sub":
        mar_itm = mar_itm.split("v")
        NOP = mar_itm[1]
        NOP = int(NOP)
        NOP -= 1
        if not NOP == 0:
            NOP = str(NOP)
            mar_itm =  marPATH +"\mar_itmv" + NOP + "v.png"

            info_mar_itm =  marPATH +"\mar_itmv" + NOP + "v.txt" #info file change
            info_mar_itm = open(info_mar_itm, "r")

            #-----Type Get
            wtype = info_mar_itm.read()
            wtype = wtype.split(",")
            wname = wtype[0]
            wmoney = int(wtype[1])
            wdamage = int(wtype[2])
            wtype = wtype[3]
            print wtype
            print wname
            #/----Type Get
            
            maritm_v1 = pygame.image.load(mar_itm)
        else:
            NOP = 4 #------------------------------------This is when it loops
            NOP = str(NOP)
            
            mar_itm =  marPATH +"\mar_itmv" + NOP + "v.png"
            
            info_mar_itm =  marPATH +"\mar_itmv" + NOP + "v.txt" #info file change
            info_mar_itm = open(info_mar_itm, "r")

            #-----Type Get
            wtype = info_mar_itm.read()
            wtype = wtype.split(",")
            wname = wtype[0]
            wmoney = int(wtype[1])
            wdamage = int(wtype[2])
            wtype = wtype[3]
            print wtype
            print wname
            #/----Type Get
            
            maritm_v1 = pygame.image.load(mar_itm)
#--------------------------------GLOBALVAR---------------------------------
Current = ["L_0", None, None, None] 
# |1:Level of menu  |2:Name of L1  |3:Name of L2, |4:Name of L3
wamount = 3
#----------------------------------GameLoop Start--------------------------
while 1:
    m_events = pygame.event.get()
    for event in m_events:    #event control
        if event.type == QUIT:
            exit()
        if Current[0] == "L_0":
            if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE: #ESC to quit
                    exit()
                    
                if md == True:  #if choose bar can be moved down
                    if event.key == K_DOWN:
                        chy += 150
                        itm1_s = False
                        itm2_s = True
                        md = False
                        mu = True
                        
                elif mu == True: #if choose bar cam be moved up
                    if event.key == K_UP:
                        chy -= 150
                        itm1_s = True
                        itm2_s = False
                        md = True
                        mu = False
                        
                if event.key == K_RETURN: #enter to choose
                
                    if itm1_s == True:
                        playmusic(sndPATH + "\FX1.ogg")
                        Current[0] = "L_1"
                        
                    if itm2_s == True:
                        pass

#-----------------------------------L_1 Menu Starts Here---------------        
                        
                        
        else:
            if itm1_s == True:
                Current[0] = "L_1"
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: #ESC to quit
                    exit()
                
                if event.key == K_BACKSPACE:
                    
                    if Current[0] =="L_1":
                        
                        Current[0] ="L_0"
                    Current[0] = "L_1"
                    Current[1] = None
                    Current[2] = None
                    
                if event.key == K_a:   #----------------------------Market
                    print"Entering market..."
                    playmusic(sndPATH + "\FX1.ogg")
                    Current[0] = "L_2"
                    Current[1] = "Market"
                        
                if event.key == K_s:   #--------------------World DataBase
                    print "Entering world database..."
                    print "Game is still running background, press Alt + Tab to switch back"
                    playmusic(sndPATH + "\FX1.ogg")
                    Current[0] = "L_2"
                    Current[1] = "WorldDB"
                    GDB.GDB() #Calls the World Database function in GDB.py
                    
                if event.key == K_d:   #----------------------------Attack
                    print"Entering attack mode..."
                    
                if event.key == K_f:    #------------------------Organizer
                    print"Entering organizer..."
                    playmusic(sndPATH + "\FX1.ogg")
                    Current[0] = "L_2"
                    Current[1] = "Organizer"
                    
                if event.key == K_g:
                    print"Entering bank..."
                    
                if event.key == K_TAB:
                    if Current[1] == "Map":
                        Current[0] = "L_1"
                        Current[1] = None
                    Current[0] = "L_2"
                    Current[1] = "Map"
                    
                if Current[1] == "Market":#________________________MARKET
                    if event.key == K_RIGHT:
                        market_tool("add")
                        
                    if event.key == K_LEFT:
                        market_tool("sub")
                        
                    if event.key == K_SPACE: #--------------------BuyMenu
                        Current[0] = "L_3"
                        Current[2] = "BuyMenu"
                        
                    if Current[2] == "BuyMenu":
                        
                        if event.key == K_n:
                            Current[0] = "L_2"
                            Current[2] = None
                            
                        if event.key == K_y: #select yes
                            try:        #______________________________DEBUG!!!
                                weaponfile = open("C:\gbuserweapon.txt", "a")
                            except IOError:
                                weaponfile = open("C:\gbuserweapon.txt", "w")
                                weaponfile.close()
                                weaponfile = open("C:\gbuserweapon.txt", "a")
                            weaponfile.write(wname + ",")
                            weaponfile.close()
                            try:
                                own = open("C:\gbuserown.txt", "r")
                            except IOError:
                                own = open("C:\gbuserown.txt", "w")
                                own.write("money = 1000000000")  #____________Initial Money
                                own.close()
                                own = open("C:\gbuserown.txt", "r")
                            O_R = own.read() #get user's money
                            exec(O_R)
                            print "EXEC Complete"
                            print money
                            print wmoney
                            money = money-wmoney #Substract the cost of the weapon
                            
                            if money >= 0:
                                own = open(r"C:\gbuserown.txt", "w")
                                own.write(str(money))
                                own.close()
                                print wname + "bought"
                                Current[0] = "L_3"
                                Current[2] = "Success"
                                
                            else:
                                own.close()
                                Current[0] = "L_3"
                                Current[2] = "Error"
                                
                if Current[1] == "Organizer":
                    if event.key == K_1:
                        pass
    
    #Display____________________________
    if Current[0] == "L_0":    #Main Menu
        screen.blit(bkg1, (0, 0))
        screen.blit(choose, (200, chy))
        screen.blit(sp_e, (200, 200))
        screen.blit(mp_e, (200, 350)) 
        
    else:
        if itm1_s == True:    #single player
        
            if Current[0] == "L_1":    #Single Player Home
                screen.blit(sp_home, (0, 0))
                #ALPHA__screen.blit(map800, (0,0))
                
            if Current[1] == "Market":
                screen.blit(maritm_v1, (0,0))
                screen.blit(marketdock, (0,600))
                
            if Current[1] == "WorldDB":
                screen.blit(dbbg, (0, 0))
                
            if Current[1] == "Organizer":
                screen.blit(orgbg, (0,0))
                
            if Current[1] == "Map":
                screen.blit(map1280, (0, 0))
                            
            
            #-------------Level 2 Menu
            if Current[2] == "BuyMenu":
                screen.blit(darken, (0, 0))
                screen.blit(buymenu, (440, 300))
                
            if Current[2] == "Error":
                screen.blit(error, (0,0))
            if Current[2] == "Success":
                screen.blit(success, (0,0))
                
    #UPDATE_________________________
    pygame.display.flip()
    
    
