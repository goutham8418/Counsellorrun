import sys
import pgzero
import pgzrun

WIDTH = 600
HEIGHT = 350
STATE = 0

print(STATE)

startbutton = Actor('startbutton', (310, 175))

def draw():
    if (STATE==0):
        screen.clear()
        screen.fill(('White'))
        startbutton.draw()
        screen.blit('titletext',(78, 5))
   

def on_mouse_down(pos, button):
    if button == mouse.LEFT and startbutton.collidepoint(pos):
        STATE=1
        print(STATE)


pgzrun.go()


    

