class c1:

    def __init__(self):
        self.x = None
        self.y = None

    def setX1(self,v):
        self.x = v

    def setY1(self,v):
        self.y = v

    def getX1(self):
        return self.x

    def getY1(self):
        return self.y

class c2(c1):


    def __init__(self):
        self.x = None
        self.y = None


    def setY2(self,v):
        self.y = v

    def getX2(self):
        return self.x

    def getY2(self):
        return self.y

def main():

    o2 = c2() 

    o2.setX1(101)
    o2.setY1(102)
    o2.setY2(999)

    print(o2.getX1())
    print(o2.getY1())
    print(o2.getX2())
    print(o2.getY2())

main()
