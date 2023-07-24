import sys
import pgzero
import pgzrun

WIDTH = 600
HEIGHT = 350

def draw():
    screen.clear()
    screen.fill(('White'))
    #screen.blit('titletext',(78, 5))
    screen.blit('startbutton',(200, 200))

#def on_key_escape():
        #screen.clear()


pgzrun.go()


    

