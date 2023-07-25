import pgzrun
import random

WIDTH = 1080
HEIGHT = 720
bg=[]
upcounter=0
STATE=0

for i in range(3):
    bg.append(Actor("bg.png"))
    bg[i].pos=(i*1080),360
    
lane1=420
lane2=520
lane3=620
anita=[]
for i in range(9):
    anita.append(Actor("anitasprites/tile00"+str(i)+".png"))
    anita[i].pos=50,lane1

"the lines above need to be done for all characters"
"the chosen sprite will be stored in MC"
natasha=[]
for i in range(9):
    natasha.append(Actor("natashasprites/tile00"+str(i)+".png"))
    natasha[i].pos=50,lane1

ellis=Actor("ellis.png")
ellis.x=1080+random.randrange(0,2000,50)
ellis.y=420+random.randrange(0,300, 100)

MC=natasha
Startbutton=Rect((1080/2-50, 720/2-50), (100, 100))
MCinlane=1
coins=[]
boogies=[]
score=0
RED = 200, 0, 0
for i in range (10):
    coins.append(Rect((1080+random.randrange(0,2000,50),420+random.randrange(0,300, 100)), (50, 50)))

for i in range (3):
    boogies.append(Rect((1080+random.randrange(0,2000,50),420+random.randrange(0,300, 100)), (50, 50)))

anitacounter=0
def draw():
    global anitacounter,upcounter,STATE
    if STATE==0:
        screen.draw.filled_rect(Startbutton, RED)
    if (STATE==1):
        if (upcounter%9==0):
            anitacounter=anitacounter+1
        for i in bg:
            i.draw()
    
        for i in coins:
            screen.draw.filled_rect(i, "green")
        for i in boogies:
            screen.draw.filled_rect(i, "blue")
	
        ellis.draw()
        MC[anitacounter%8].draw()

    
def update():
    global MCinlane,upcounter,score
    
    if STATE==1:
        upcounter=upcounter+1
        ellis.x=ellis.x-2
        for i in bg:
            i.x=i.x-2
            if (i.x<-1080):
                i.x=1080*2
        for i in coins:
            i.x=i.x-2
        for i in boogies:
            i.x=i.x-2 
        for j in MC:
        
            for i in coins:
            
                if (i.x<-20):
                    i.x=1080+random.randrange(0,1000,50)
                    
                    score=score-1
                if j.colliderect(i):
                    i.x=1080+random.randrange(0,1000,50)
                    score=score+1
                    print(score)
            
            for i in boogies:
                
                if (i.x<-20):
                    i.x=1080+random.randrange(0,1000,50)
                    
                if j.colliderect(i):
                    i.x=1080+random.randrange(0,1000,50)
                    score=score-1
                    print(score)

            if j.colliderect(ellis):
                score=score-50
                print(score)
                ellis.x=1080+random.randrange(0,1000,50)
        if (upcounter%7==0):
            if keyboard.up and MCinlane!=1:
                for i in MC:
                    i.y=i.y-100
            
                MCinlane=MCinlane-1
        
            if keyboard.down and MCinlane != 3:
                for i in MC:
                    i.y=i.y+100
                MCinlane=MCinlane+1
        
def on_mouse_down(pos, button):
    global STATE
    if button == mouse.LEFT and Startbutton.collidepoint(pos):
        STATE=1


pgzrun.go()
