class Edge(object):
    def __init__(self, src:int, w:float, dest:int):
        self.src = src
        self.w = w
        self.dest = dest

    def __str__(self):
        return f" src:{self.src} , w:{self.w} , dest:{self.dest}"

    def __repr__(self):
        return f" src:{self.src} , w:{self.w} , dest:{self.dest}"

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def getWeight(self):
        return self.w