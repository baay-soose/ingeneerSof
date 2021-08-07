import turtle

LARGEUR, HAUTEUR = 100, 150

if __name__ == "__main__":
    turtle.forward(LARGEUR)  #Avance de d'un tiers de la largeur
    turtle.left(90)  #Tourne de 90° à gauche
    turtle.forward(HAUTEUR)
    turtle.pensize(3)  #Change l'épaisseur du tracé
    turtle.home()  #Retourne à la maison
    turtle.exitonclick()  