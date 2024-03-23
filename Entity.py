import math
class Entity:
    x, y = 0, 0
    resX, resY = 0, 0
    vx, vy = 0, 0
    t = 0
    m = 1
    width = 1;  widDev = 0
    height = 1; heiDev = 0
    turn = "stand" #stand, left, right, jumpStart, jumpLast
    texture = "None"
    hp = 50
    maxHP = 50
    
    def giveDamage(self, damage):
        self.hp -= damage * self.t
        self.hp = (0 if self.hp<0 else (self.maxHP if self.hp>self.maxHP else self.hp))
        if self.hp == 0:
            self.dead()
    def dead(self):
        self.x = self.resX
        self.y = self.resY
        self.hp = self.maxHP
        self.vx = 0
        self.vy = 0
    def getCollisionBox(self, level, t):
        dx, dy = self.x-self.width/2+self.widDev, self.y-self.height/2+self.heiDev
        self.collision = False
        self.collisionRect = []
        for x in range(math.ceil(dx+self.width)-int(dx)):
            self.collisionRect.append([])
            for y in range(math.ceil(dy+self.height)-int(dy)):
                mat = level.getBlock(x+int(dx), y+int(dy))
                if mat.isSolid:
                    self.collision = True
                    self.giveDamage(mat.damage)
                    self.collisionRect[-1].append(mat)
                else:
                    self.collisionRect[-1].append(None)
        return self.collision
