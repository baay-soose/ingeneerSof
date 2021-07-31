from math import pow
def saisie():
    n = int(input("donner la valeur de n:  "))
    return n
    

def numerateur(n):
    num =  pow(2*n, 2)
    return num

def denominateur(n):
    denom = (2*n -1)*(2*n +1)
    return denom

def quotient(num, denom):
    q = num/denom
    return q


def produitCumule(n):
    p = 1
    for i in range(1, n+1):
        p*=quotient(numerateur(i), denominateur(i))        

    return p


def principal():
    a = saisie()
    b = produitCumule(a)
    print(b)    
    
if __name__ == '__main__':
    principal()    
    
    

"""Fonction1: numerateur
Objectifs : Calculer la valeur du numerateur
methode : Expression et Affectation
Besoin : n
Connus : –
Entrees : n
Sorties : Num
Resultatss : –
Hypothese : n>=1"""

"""Fonction1: denominateur
Objectifs : Calculer la valeur du denominateur
methode : Expression et Affectation
Besoin : n
Connus : –
Entrees : n
Sorties : denom
Resultats : –
Hypothese : n>=1"""

"""Fonction1: quotient
Objectifs : Calculer la valeur du quotient
methode : Expression et Affectation
Besoin : num, denom
Connus : –
Entrees : n
Sorties : quot
Resultats : –
Hypothese : num>0, denom>0(on pouvait ne pas faire l'hypothese)"""

"""Fonction1: Produit
Objectifs : Produit cumule de rappot en fonction de la variation
methode : Boucle
Besoin : quot
Connus : –
Entrees : quot
Sorties : Produit
Resultats : –
Hypothese :  
"""
