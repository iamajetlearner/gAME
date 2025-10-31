import pgzrun
import random
WIDTH=800
HEIGHT=600
ship=Actor("ship")
ship.x=400
ship.y=500
astroids=[]
bullets=[]
for i in range(5):
    astroid=Actor("astroid")
    astroid.x=random.randint(50,WIDTH-50)
    astroid.y=-50
    astroids.append(astroid)
def draw():
    screen.blit("space",(0,0))
    ship.draw()
    for astroid in astroids:
        astroid.draw()
    for bullet in bullets:
        bullet.draw()
def update():
    global astroids,bullets
    if keyboard.left:
        ship.x-=5   
    elif keyboard.right:
        ship.x+=5 
    for bullet in bullets:
        for astroid  in astroids:  
            if astroid .colliderect(bullet):    
                astroids.remove(astroid)
                bullets .remove(bullet)
        bullet.y-=5
def fall():
    for astroid in astroids:
        astroid.x=random.randint(50,WIDTH-50)
        astroid.y=-50
        animate(astroid,duration=5,y=HEIGHT + 50,on_finished=fall)
def on_key_down(key):
    if key == keys.SPACE:
        bullet=Actor("bullet")
        bullet.x=ship.x
        bullet.y=ship.y
        bullets.append(bullet)
fall()
pgzrun.go()
