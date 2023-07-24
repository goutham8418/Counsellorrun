import sys
import pgzero
import pgzrun

WIDTH = 600
HEIGHT = 350

start_button = Actor('startbutton', (108,50))

def draw():
    screen.clear()
    start_button.draw()
    screen.fill(('White'))
    screen.blit('titletext',(78, 5))
    screen.blit('startbutton',(74, 5))

def on_key_escape():
        screen.clear()


pgzrun.go()


    

