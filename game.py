import pgzrun
import random
WIDTH=800
HEIGHT=600
ship=Actor("ship")
ship.x=400
ship.y=500
astroid=Actor("astroid")
astroid.x=random.randint(50,WIDTH-50)
astroid.y=-50
def draw():
    screen.blit("space",(0,0))
    ship.draw()
    astroid.draw()
def update():
    if keyboard.left:
        ship.x-=5   
    elif keyboard.right:
        ship.x+=5
def fall():
    astroid.x=random.randint(50,WIDTH-50)
    astroid.y=-50
    animate(astroid,duration=2,y=HEIGHT + 50,on_finished=fall)
fall()
pgzrun.go()