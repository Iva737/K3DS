import pygame
from time import time

pygame.init()
sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
mx, my = sc.get_width(), sc.get_height()
cub = (mx if mx > my else my)*.16
path = "assets/img/"

# load img file: {w, h, n}
loadImg = {
"player.png": {"w": 1, "h": 1, "n": 1},
"fon.png": {"w": 50, "h": 50}
}
textures = {}
for i in loadImg.keys():
    name = i.split('.')[0]
    
    textures[name+"Prime"] = pygame.image.load(path+i)
    if "w" in loadImg[i] and "h" in loadImg[i]:
        textures[name] = pygame.transform.scale(textures[name+"Prime"], (cub*loadImg[i]["w"], cub*loadImg[i]["h"]))
print(textures.keys())

px, py = cub//2, cub//2
speed = cub*.16

button = [False, False, False, False]
CLOSE = False

while not CLOSE:
    #sc.fill((75, 75, 75))
    t1 = time()
    sc.blit(textures["fon"], (-px + mx//2, -py + my//2))
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT or (evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE):
            CLOSE = True
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
    
    if button[1]:
        py-=speed * t * 10
    if button[0]:
        px-=speed * t * 10
    if button[2]:
        px+=speed * t * 10
    if button[3]:
        py+=speed * t * 10
    
    sc.blit(textures["player"], (mx//2-textures["player"].get_width()//2, my//2-textures["player"].get_height()//2))
    pygame.display.update()
    t2 = time()
    t = t2-t1