class Edge(object):
    def __init__(self, src:int, dst:int, w:float):
        self.src = src
        self.dst = dst
        self.w = w

    def __str__(self):
        return f"src:{self.src} dst:{self.dst} weight:{self.w}"

    def __repr__(self):
        return f"src:{self.src} dst:{self.dst} weight:{self.w}"

    def getSrc(self):
        return self.src

    # def setId(self, id):
    #     self.id = id

    def getDst(self):
        return self.dst

    # def setPos(self, pos):
    #     self.pos = pos
    def getWeight(self):
        return self.w
