import pgzrun
import random
score=0
health=100
WIDTH= 521
HEIGHT= 544
player=Actor("player")
player.x=260
player.y=272
enemies=[]
game = True
enemy_images=["greenship","blueship","greyship","redship"]
health= 3
timer=0
def makeenemies():
    enemy=Actor("greenship")
    enemies.append(enemy)
    enemy.image=enemy_images[random.randint(0,3)]
    if enemy.image == "greenship":
        enemy.pos=0,0
    if enemy.image == "redship":
        enemy.pos=0,544
    if enemy.image == "greyship":
        enemy.pos=512,544
    if enemy.image == "blueship":
        enemy.pos=512,0
def on_mouse_down(pos):
    if game == True:
        animate(player,pos=pos, duration=0.1,angle=player.angle_to(pos),tween="bounce_end")
def draw():
    global timer,health
    screen.clear()
    screen.blit("bg",(0,0))
    player.draw()
    if game == True:
        timer +=1
        if timer%20==0:
            makeenemies()
            timer=0
        for enemy in enemies:
            enemy.draw()
            animate(enemy,pos=player.pos, duration=0.5,angle=enemy.angle_to(player.pos), tween = "accel_decel")
            if enemy.colliderect(player):
                enemies.remove(enemy)
                health -=1
pgzrun.go()
