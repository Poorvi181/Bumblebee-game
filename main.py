import pgzrun,random
TITLE="Catch the Flower"
WIDTH=500
HEIGHT=500
bee=Actor("bumblebee")
bee.pos=100,100
flower=Actor("flower")
flower.pos=200,200
score=0
gameover=False
def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score:"+str(score),center=(400,30),fontsize=30)
    if gameover:
        screen.fill("black")
        screen.draw.text("Time's up your final score is:"+str(score),midtop=(200,30),fontsize=30,color="white")
def update():
    global score
    if keyboard.left:
        bee.x-=2
    if keyboard.right:
        bee.x+=2
    if keyboard.up:
        bee.y-=2
    if keyboard.down:
        bee.y+=2
    flowercollected=bee.colliderect(flower)
    if flowercollected:
        flower.x=random.randint(50,450)
        flower.y=random.randint(50,450)
        score+=1

def timeup():
    global gameover
    gameover=True

clock.schedule(timeup,60)
pgzrun.go()