class Node(object):
    def __init__(self, id:int, pos:tuple):
        self.id = id
        self.pos = pos

    def __str__(self):
        return f"id:{self.id} pos:{self.pos}"

    def __repr__(self):
        return f"id:{self.id} pos:{self.pos}"

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getPos(self):
        return self.pos

    def setPos(self, pos):
        self.pos = pos


