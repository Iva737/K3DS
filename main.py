import pygame
import math
from time import time

class Player():
    hp = 100
    collision = False
    collisionPosition = (0, 0)
    vx, vy = 0, 0
    def __init__(self, name):
        global cub
        self.name = name
        self.x, self.y = 0, 0
        self.speed = 0
        self.w, self.h = 1.4*cub, 2.9*cub
        self.W, self.H = 1.4,     2.9
    def Debug(self):
        global mx, my
        color = ((255, 0, 0) if self.collision else (0, 255, 0))
        pygame.draw.circle(sc, color, (mx//2, my//2), 3)
        pygame.draw.rect(sc, color, (mx//2-self.w//2, my//2-self.h//2, self.w, self.h), 1)
    def checkCollision(self):
        global t
        px, py = self.x-self.W/2, self.y-self.H/2
        self.collision = False
        for x in range(math.ceil(px+self.W)-int(px)):
            for y in range(math.ceil(py+self.H)-int(py)):
                mat = getPointLvl(x+int(px), y+int(py))
                if mat!="0":
                    self.collision = True
                    self.collisionPosition = (x+int(px), y+int(py))
                    if mat == "2":
                        self.hp -= 1 * t; self.hp = (self.hp if self.hp>=0 else 0)
        return self.collision

def loadTextures(loadImg):
    global textures
    # load img file: {w, h, n}
    for i in loadImg.keys():
        name = i.split('.')[0]
        textures[name+"Prime"] = pygame.image.load(path+i)
        if "w" in loadImg[i] and "h" in loadImg[i]:
            textures[name] = pygame.transform.scale(textures[name+"Prime"], (cub*loadImg[i]["w"], cub*loadImg[i]["h"]))

def loadLevel(n):
    global level
    # load Map
    file = open(f"{n}map.txt", 'r')
    text = file.read().split('\n')[0:-1]
    file.close()
    level = []
    for i in text:
        level.append(list(i))

def getPointLvl(x, y):
    if 0<=y<len(level) and 0<=x<len(level[y]):
        return level[y][x]
    else:
        return "0"

def checkLevel():
    global level, px, py, mx, my, levelX, levelY, cub
    pass

def drawLevel():
    global level

pygame.init()
sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
mx, my = sc.get_width(), sc.get_height()


Debug = False
t1, t2 = 0, 0
path = "assets/img/"
textures = {}
loadImg = { # load img file: {w, h, n}
"player.png": {"w": 3, "h": 3, "n": 1},
"wall.png": {"w": 1.03, "h": 1.03, "n": 1},
"cactus.png": {"w": 1.03, "h": 1.03, "n": 1}
}
button = [False, False, False, False]
CLOSE = False
level = []
levelX = 0
levelY = 0
win = False

cub = (mx if mx > my else my)*.03
p = Player("X3mall")
p.x, p.y = 5, 17
p.speed = 3
mapX, mapY = mx//2 - p.x*cub, my//2 - p.y*cub

loadTextures(loadImg)
loadLevel(1)
    

textures["fon"] = pygame.Surface((len(level[0])*cub, len(level)*cub))
for i in range(len(level)):
    for j in range(len(level[0])):
        if getPointLvl(j, i) == '1':
            textures["fon"].blit(textures["wall"], (j*cub, i*cub))
        elif getPointLvl(j, i) == '2':
            textures["fon"].blit(textures["cactus"], (j*cub, i*cub))
textures["fon"].set_colorkey((0, 0, 0))





while not CLOSE:
    t = t2-t1
    sc.fill((52, 52, 52))
    mapX, mapY = mx//2 - p.x*cub, my//2 - p.y*cub
    t1 = time()
    sc.blit(textures["fon"], (mapX, mapY))
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT or (evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE):
            CLOSE = True
        elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_F3:
            Debug = not Debug
        elif evt.type == pygame.KEYDOWN or evt.type == pygame.KEYUP:
            mat = evt.type == pygame.KEYDOWN
            if (evt.key == pygame.K_LEFT or evt.key == pygame.K_a):
                button[0] = mat
            elif (evt.key == pygame.K_UP or evt.key == pygame.K_w):
                button[1] = mat
            elif (evt.key == pygame.K_RIGHT or evt.key == pygame.K_d):
                button[2] = mat
            elif (evt.key == pygame.K_DOWN or evt.key == pygame.K_s):
                button[3] = mat
    if not win:
        p.vy += t * .4
    if button[1]:
        p.vy = (p.vy - p.speed * t * .3 if -p.speed<p.vy else -p.speed)
    if button[0]:
        p.vx = (p.vx - p.speed * t * .3 if -p.speed<p.vx else -p.speed)
    if button[2]:
        p.vx = (p.vx + p.speed * t * .3 if p.speed>p.vx else p.speed)
    if button[3]:
        p.vy = (p.vy + p.speed * t * .3 if p.speed>p.vy else p.speed)
    p.x += p.vx * t * 10
    if not win and p.checkCollision():
        p.x -= p.vx * t * 10
        p.vx *= .3
    p.y += p.vy * t * 10
    if not win and p.checkCollision():
        p.y -= p.vy * t * 10
        p.vy *= .3
        p.vx *= .98
    if not win:
        p.checkCollision()
    if win:
        if   not 0<=p.x: p.vx = .7*abs(p.vx)
        elif not p.x<len(level[0]): p.vx = -.7*abs(p.vx)
        if   not 0<=p.y: p.vy = .7*abs(p.vy)
        elif not p.y<len( level  ): p.vy = -.7*abs(p.vy)
        
    sc.blit(textures["player"], (mx//2-textures["player"].get_width()//2, my//2-textures["player"].get_height()//2))
    pygame.draw.rect(sc, (255, 0, 0), (7, 7, 3*cub*p.hp//100, cub*.5))
    pygame.draw.rect(sc, (0, 0, 0), (0, 0, 3*cub+14, cub*.5+14), 5)
    
    
    if Debug:
        p.Debug()
        pygame.draw.line(sc, (255, 0, 0), (0, mapY), (mx, mapY), 1)
        pygame.draw.line(sc, (0, 255, 0), (mapX, 0), (mapX, my), 1)
        pygame.draw.rect(sc, (0,255,255), (mapX, mapY, len(level[0])*cub, len(level)*cub), 1)
    if not win and (p.hp<=0 or not (0<p.y<len(level) and 0<p.x)):
        p.x, p.y = 5, 17; p.vx, p.vy = 0, 0
        p.hp = 100
    if not win and p.x>len(level[0]):
        win = True
        Debug = True
        p.vx -= 2
        p.vy += .78
        p.hp = 999
    pygame.display.update()
    t2 = time()

