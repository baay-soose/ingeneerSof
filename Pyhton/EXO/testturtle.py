import turtle 


def carre():
    car = turtle.Turtle()
    for i in range(4) :
        car.width(3)
        car.forward(100)
        car.left(90)
def cercle():
    cer = turtle.Turtle()
    cer.circle(100)
def demicercle():
    dmcer = turtle.Turtle()
    dmcer.circle(50, 180)
def rectangle():
    rec = turtle.Turtle() 
    for i in range(2):
        rec.forward(100)
        rec.left(90)
        rec.forward(50)
        rec.left(90)

def triangle():
    trg = turtle.Turtle()
    trg.width(3)
    trg.goto(100,200)  
    trg.rt(90)
    trg.forward(200)
    trg.rt(90)  
    trg.forward(100)
def polygone(cote):
    for i in range(cote):
        turtle.forward(100)
        turtle.lt(360/cote)
def losange():
    los = turtle.Turtle()
    for i in range(2):
        los.forward(40)
        los.left(120)
        los.forward(40)
        los.left(60)
    



if __name__ == '__main__':
    """ carre()
     rectangle()
     triangle() 
     cercle()
    demicercle()
    losange()"""

    


   
    turtle.done()