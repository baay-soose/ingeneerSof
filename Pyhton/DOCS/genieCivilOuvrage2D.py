""" Module pour turtle des fonctions cercle, rectangle, 
triangle, trapeze, carre, polygone, losange, Ellipse, demi-cercle
"""
from turtle import *

# Fonction carre
# entree : cote
def carre(cote):
    for i in range(4) :
        forward(cote)
        left(90)

# Fonction cercle       
# entree : rayon 
def cercle(rayon):
    circle(rayon)
# Fonction demi-cercle       
# entree : rayon     

def demicercle(rayon):
    circle(rayon, 180)

# Fonction rectangle
# entree longueur, largeur    
def rectangle(longueur, largeur):
    for i in range(2):
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)

# Fonction  triangle rectangle
# entree : a et b
def triangle(a,b):
    width(3)
    goto(a,b)  
    rt(90)
    forward(a)
    rt(90)  
    forward(b)

# Fonction polygone
# entree : n le type de polygone et le cote en  px
def polygone(n,cote):
    for i in range(n):
        forward(cote)
        lt(360/n)

# Fonction losange
# entree : cote   
def losange(cote):
    for i in range(2):
        forward(cote)
        left(120)
        forward(cote)
        left(60)
