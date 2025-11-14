import pgzrun
WIDTH= 521
HEIGHT= 544
player=Actor("player")
player.x=260
player.y=272
game = True
def on_mouse_down(pos):
    if game == True:
        animate(player,pos=pos, duration=0.1,angle=player.angle_to(pos),tween="bounce_end")
def draw():
    screen.blit("bg",(0,0))
    player.draw()
pgzrun.go()