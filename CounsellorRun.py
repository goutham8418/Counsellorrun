#Import librarys
import sys
import pgzero
import pgzrun

#Define variables and screen size
WIDTH = 600
HEIGHT = 350
TITLE = "Main Menu"
STATE = 0
MC = None

print(STATE)

startbutton = Actor('startbutton', (310, 175))
joe = Actor("pixilart-drawing.png")
emilie = Actor("pixilart-drawing 3.png")
harrison = Actor("harrison.png")
mark = Actor("mark.png")
callum = Actor("callum.png")

#Draw the game screen depending on the state
def draw():
    if STATE==0:
        screen.clear()
        screen.fill(('White'))
        startbutton.draw()
        screen.blit('titletext',(78, 5))
    elif STATE==2:
        screen.clear()
        screen.fill("firebrick")
        screen.draw.text("Choose your character!", center=(WIDTH / 2, HEIGHT / 2 - 120), fontsize=30, color="white")
        screen.draw.filled_rect(Rect(WIDTH / 2 - 180, HEIGHT / 2 - 90, 100, 80), "grey")
        screen.draw.filled_rect(Rect(WIDTH / 2 - 180, HEIGHT / 2 - 5, 100, 80), "grey")
        screen.draw.filled_rect(Rect(WIDTH / 2 - 180, HEIGHT / 2 + 80, 100, 80), "grey")
        screen.draw.filled_rect(Rect(WIDTH / 2 + 70, HEIGHT / 2 - 100, 100, 80), "grey")
        screen.draw.filled_rect(Rect(WIDTH / 2 + 70, HEIGHT / 2 - 15, 100, 90), "grey")
        screen.draw.filled_rect(Rect(WIDTH / 2 + 70, HEIGHT / 2 + 80, 100, 80), "grey")

        joe.pos = (160, 119)
        joe.draw()
    
        emilie.pos = (420, 200)
        emilie.draw()

        harrison.pos = (165, 210)
        harrison.draw()
    
        mark.pos = (165, 295)
        mark.draw()
    
        callum.pos = (420, 115)
        callum.draw()
   
#Register clicks on the start button
def on_mouse_down(pos, button):
    global STATE
    if button == mouse.LEFT and startbutton.collidepoint(pos):
        STATE=2
        print(STATE)
    if button == mouse.LEFT and joe.collidepoint(pos):
        MC=joe
        STATE=1
        print(STATE)
        
    if button == mouse.LEFT and emilie.collidepoint(pos):
        MC=emilie
        STATE=1
        print(STATE)
    
    if button == mouse.LEFT and harrison.collidepoint(pos):
        MC=harrison
        STATE=1
        print(STATE)
        
    if button == mouse.LEFT and mark.collidepoint(pos):
        MC=mark
        STATE=2
        print(STATE)
        
    if button == mouse.LEFT and callum.collidepoint(pos):
        MC=callum
        STATE=1
        print(STATE)

#Run the game :)
pgzrun.go()


    

