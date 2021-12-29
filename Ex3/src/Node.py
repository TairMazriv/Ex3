class Node(object):
    def __init__(self, pos:tuple, id:int):
        self.pos = pos
        self.id = id

    def __str__(self):
        return f"pos:{self.pos} , id:{self.id}"

    def __repr__(self):
        return f"pos:{self.pos} , id:{self.id}"

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getPos(self):
        return self.pos

    def setPos(self, pos):
        self.pos = pos
