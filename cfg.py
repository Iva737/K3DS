path = "assets/img/"
Debug = False
FPS = 30
gravity = 1.89
maxSpeed = 3
loadImg = { # load img file: {w, h, files}
"X3mall":     {"w": 3,    "h": 3,    "files": ["player.png", "wall.png", "cactus.png"]},
"wall":       {"w": 1.03, "h": 1.03, "files": ["wall.png"]  },
"cactus":     {"w": 1.03, "h": 1.03, "files": ["cactus.png"]}
}

mapX = 0
mapY = 0
t = 0
tick = 0 # 0-29
timeTick = 250
absTime = 0
textures = {}
button = [False, False, False, False]
Close = False
win = False

