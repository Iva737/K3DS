class Map:
    passBlock = 0
    
    def __init__(self, level = 0):
        self.load(f"{level}map.txt")
        self.passBlock = Block()
        self.translate()
    
    def load(self, path):
        file = open(path, 'r')
        text = file.read().split('\n')
        file.close()
        self.idata = []
        for i in range(len(text)):
            self.idata.append(list(text[i]))
        self.idata = self.idata[0:-1]
        self.height = len(self.idata)
        self.width  = len(self.idata[0])
    
    def translate(self):
        self.data = []
        for y in range(self.height):
            self.data.append([])
            for x in range(self.width):
                self.data[y].append( Block(data=int(self.idata[y][x]), x=x, y=y) )
    
    def getBlock(self, x, y):
        if 0<=x<self.width and 0<=y<self.height:
            return self.data[y][x]
        else:
            return self.passBlock

class Block:
    SolidBlocks = [1, 2]
    DamageBlocks = {2: 80}
    TextureBlocks = {1: "wall", 2: "cactus"}
    
    def __init__(self, data = 0, x = None, y = None):
        self.isSolid = data in Block.SolidBlocks
        self.damage  = (Block.DamageBlocks[data]  if data in Block.DamageBlocks  else 0)
        self.texture = (Block.TextureBlocks[data] if data in Block.TextureBlocks else "None")
