from turtle import *
def carre(taille, couleur):
        "fonction qui dessine un carré de taille et de couleur déterminées"
        color(couleur)
        c =0
        while c <4:
                forward(taille)
                right(90)
                c = c + 1

if __name__ == "__main__":
    
        up() # relever le crayon
        goto(-150, 50) # reculer en haut à gauche
        for i in range(10):# dessiner dix carrés rouges, alignés :
            down() # abaisser le crayon
            carre(25, 'red') # tracer un carré
            up() # relever le crayon
            forward(30) # avancer + loin
            down()

