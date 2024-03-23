import pygame
from time import time
from cfg import*
from Map import Map, Block
from Player import Player


def loadTextures():
    global loadImg, cub
    for name in loadImg.keys():
        textures[name+"Prime"] = []
        textures[    name    ] = []
        for i in range(len( loadImg[name]["files"] )):
            textures[name+"Prime"].append( pygame.image.load(path+loadImg[name]["files"][i]) )
            if "w" in loadImg[name] and "h" in loadImg[name]:
                textures[name].append( pygame.transform.scale(textures[name+"Prime"][i], (cub*loadImg[name]["w"], cub*loadImg[name]["h"])) )

def getTick(texture):
    global textures, tick
    return tick%len(textures[texture])

def getSpd(speed):
    return (-maxSpeed if speed<-maxSpeed else (maxSpeed if speed>maxSpeed else speed))

def evtKEY(evt):
    global button
    mat = evt.type == pygame.KEYDOWN
    if (evt.key == pygame.K_LEFT or evt.key == pygame.K_a):
        button[0] = mat
    elif (evt.key == pygame.K_RIGHT or evt.key == pygame.K_d):
        button[1] = mat

def events():
    global Close, Debug, t, p
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT or (evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE):
            Close = True
        elif evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_F3: Debug = not Debug
            elif evt.key == pygame.K_SPACE and p.collision:
                p.vy -= p.speedY
            evtKEY(evt)
        elif evt.type == pygame.KEYUP:
            evtKEY(evt)


def physics():
    global gravity, button, level, p, t
    p.vy += t * gravity
    if button[0]:
        p.vx = (p.vx - p.speedX * t * .3 if -p.speedX<p.vx else -p.speedX)
    if button[1]:
        p.vx = (p.vx + p.speedX * t * .3 if p.speedX>p.vx else p.speedX)
    
    p.vx = getSpd(p.vx)
    p.x += p.vx * t * 10
    if p.getCollisionBox(level, t):
        p.x -= p.vx * t * 10
        p.vx *= .1
    
    p.vy = getSpd(p.vy)
    p.y += p.vy * t * 10
    if p.getCollisionBox(level, t):
        p.y -= p.vy * t * 10
        p.vy *= .1
        if not (button[0] or button[1]):
            p.vx *= .7

def draws():
    global mx, my, textures, p, level, mapX, mapY
    sc.fill((0x34, 0x34, 0x34))
    for y in range(level.height):
        for x in range(level.width):
            mat = level.getBlock(x, y).texture
            if mat != "None":
                sc.blit(textures[mat][getTick(mat)], (x*cub+mapX, y*cub+mapY))
    pl = textures["X3mall"][getTick("X3mall")]
    sc.blit(pl, (mx//2-pl.get_width()//2, my//2-pl.get_height()//2))
    pygame.draw.rect(sc, (255, 0, 0), (7, 7, 3*cub*p.hp//100, cub*.5))
    pygame.draw.rect(sc, (0, 0, 0), (0, 0, 3*cub+14, cub*.5+14), 5)

def drawDebug():
    global mx, my, mapX, mapY, p, cub
    pygame.draw.line(sc, (255, 0, 0), (0, mapY), (mx, mapY), 1)
    pygame.draw.line(sc, (0, 255, 0), (mapX, 0), (mapX, my), 1)
    pygame.draw.rect(sc, (0,255,255), (mapX, mapY, level.width*cub, level.height*cub), 1)
    pygame.draw.circle(sc, (0, 255, 0), (mx//2, my//2), 3)
    pygame.draw.rect(sc, (0, 255, 0), (mx//2-p.width*cub//2+p.widDev*cub, my//2-p.height*cub//2+p.heiDev*cub, p.width*cub, p.height*cub), 1)

def main():
    global Close, Debug, tick, t, mapX, mapY
    while not Close:
        events()
        physics()
        mapX, mapY = mx//2 - p.x*cub, my//2 - p.y*cub
        draws()
        if Debug: drawDebug()
        
        pygame.display.update()
        t = 1/clock.tick(FPS); p.t = t
        tick = ((int(pygame.time.get_ticks()))//timeTick)%30

if __name__=="__main__":
    pygame.init()
    clock = pygame.time.Clock()
    sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    mx, my = sc.get_width(), sc.get_height()
    cub = (mx if mx > my else my)*.03
    
    loadTextures()
    level = Map( level = 1 )
    p = Player()
    p.resX = 4
    p.resY = 4
    p.x = p.resX
    p.y = p.resY
    
    main()

