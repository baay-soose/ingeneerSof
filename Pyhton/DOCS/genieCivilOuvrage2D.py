""" Module pour turtle des fonctions cercle, rectangle, 
triangle, trapeze, carre, polygone, losange, Ellipse, demi-cercle
"""
import turtle 

# FOnction carre
# entree : cote
def carre(cote):
    car = turtle.Turtle()
    for i in range(4) :
        car.width(3)
        car.forward(cote)
        car.left(90)

# Fonction cercle       
# entree : rayon 
def cercle(rayon):
    cer = turtle.Turtle()
    cer.circle(rayon)
# Fonction demi-cercle       
# entree : rayon     

def demicercle(rayon):
    dmcer = turtle.Turtle()
    dmcer.circle(rayon, 180)

# Fonction rectangle
# entree longueur, largeur    
def rectangle(longueur, largeur):
    rec = turtle.Turtle() 
    for i in range(2):
        rec.forward(longueur)
        rec.left(90)
        rec.forward(largeur)
        rec.left(90)

# Fonction  triangle rectangle
# entree : a et b
def triangle(a,b):
    trg = turtle.Turtle()
    trg.width(3)
    trg.goto(a,b)  
    trg.rt(90)
    trg.forward(a)
    trg.rt(90)  
    trg.forward(b)

# Fonction polygone
# entree : n le type de polygone et le cote en  px
def polygone(n,cote):
    for i in range(n):
        turtle.forward(cote)
        turtle.lt(360/n)

# Fonction losange
# entree : cote   
def losange(cote):
    los = turtle.Turtle()
    for i in range(2):
        los.forward(cote)
        los.left(120)
        los.forward(cote)
        los.left(60)
    



if __name__ == '__main__':
    """ carre()
     rectangle()
     triangle() 
     cercle()
    demicercle()
    losange()"""
    
    
    carre(250)
    triangle(100,200)

   
    turtle.done()