""" Module pour turtle des fonctions cercle, rectangle, 
triangle, trapeze, carre, polygone, losange, Ellipse, demi-cercle
"""
from turtle import *

# Fonction carre
# entree : cote
def deplacer(x,y):
    up() #relever le crayon
    goto(x, y) # reculer en haut à gauche
    down() #baisser le crayon
    
def carre(cote):
    """ Fonction dessine carre python turtle """    
    for i in range(4) :
        forward(cote)
        left(90)

# Fonction cercle       
# entree : rayon 
def cercle(rayon):
    """ Fonction dessine cercle python turtle """    
    circle(rayon)
# Fonction demi-cercle       
# entree : rayon     
def demicercle(rayon):
    """ Fonction dessine demi-cercle python turtle """    
    circle(rayon, 180)

# Fonction rectangle
# entree longueur, largeur    
def rectangle(longueur, largeur):
    """ Fonction rectangle ellipse python turtle """
       
    for i in range(2):
        width(1.5)
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)

# Fonction  triangle 
# entree : a  b et c
def triangle(a,b,c):
    """ Fonction dessine triangle python turtle """    
    forward(a)  
    rt(360/3)
    forward(b)
    rt(360/3)  
    forward(c)

#Fonction triangle rectangle 
# entree : largeur hauteur
def triangleRectangle(LARGEUR, HAUTEUR):
    """ Fonction dessine triangle rectangle python turtle """    
    forward(LARGEUR)  #Avance de d'un tiers de la largeur
    left(90)  #Tourne de 90° à gauche
    forward(HAUTEUR)
    pensize(3)  #Change l'épaisseur du tracé
    home()  #Retourne à la maison     

# Fonction polygone
# entree : n le type de polygone et le cote en  px
def polygone(n,cote):
    for i in range(n):
        forward(cote)
        lt(360/n)

# Fonction losange
# entree : cote   
def losange(cote):
    """ Fonction dessine losange python turtle """    
    for i in range(2):
        forward(cote)
        left(120)
        forward(cote)
        left(60)

#Fonction : Ellipse
#entree : rad
def ellipse(rad): 
    """ Fonction dessine ellipse python turtle """    
    circle(rad,90) 
    circle(rad//2,90) 

 # Fonction : trapeze
 # entree  
    
