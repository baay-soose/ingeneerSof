import math

class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def affiche(self): 
        print("POINT(",self.x,self.y,")")

class Cercle(Point) :
    def __init__(self,x,y,r) :
       self.r=r
       Point.__init__(self,x,y)
    def afficheCercle(self):
        print("Cercle(",self.x,self.y,self.r,")")    

    def getPerimetre(self):
        return 2*math.pi*self.r

    def getSurface(self):
        return math.pi*self.r**2
    #def appartient(self,x,y,r) :
    
class Cylindre(Cercle, Point):
    def __init__(self,x,y,r,h):
        self.h=h
        Cercle.__init__(self,x,y,r)
        Point.__init__(self,x,y)
    def afficheCylindre(self):
        print("Cylindre(",self.x,self.y,self.r,self.h,")") 

   ###test
POINT=Point(4,6)        
POINT.affiche()
cercle=Cercle(4,8,4)
cercle.afficheCercle()
p = cercle.getPerimetre()
s = cercle.getSurface()
print(p)
print(s)
cylindre=Cylindre(2,5,7,8)
cylindre.afficheCylindre()


