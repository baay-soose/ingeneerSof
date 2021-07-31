def saisie() :
    n = int(input("Veuillez saisir la valeur de n"))
    return n
def numerateur(n) :
    num =  2*n * 2*n
    return num
def denominateur(n) :
    denom = (2*n - 1)*(2*n + 1)
    return denom
def quotient(num, denom) :
    q = num/denom
    return q
def produitCumule(n) :
    p = 1
    for i in range(1, n+1) :
        p *= quotient(numerateur(i), denominateur(i))
        return p        
def principal():
    a = saisie()
    b = produitCumule(a)
    print(b)

if __name__ == "__main__" :
    principal()


""" Fonction 1
Objectifs : Calculer la valeur du numerateur
Methode : Expression et Affectation 
Besions : n
Connus : -
Entrees : n
Sorties : Num
Rsultats : -
Hypothese : n>=1
 """
""" Fonction 2
Objectifs : Calculer la valeur du denominateur
Methode : Expression et affectation
Besoins : n
Connus : -
Entrees : n
Sorties : Denom
Resultats : -
Hypothese : n>=1
 """
""" Fonction 3
Objectif : Calculer le quotient
Methode : Expresion et affectation
Besoins : Num et Denom
Connus : -
Entrees : Num et denom 
Sorties : q
Resultats : 
Hypothese : num > 0 denom > 0 """
""" Fonction 4
Objectif : Produit cumule de rapport en fonction de la variation
Methode : Boucle
Besoins : q
Connus : -
Entrees : q
Sorties : p
Resultats : -
Hypothese : - """