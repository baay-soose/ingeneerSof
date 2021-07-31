def saisie() :
    x,n = float(input("Saisie la valeur de x : ")), int(input("Saisie la valeur de n : "))
    return x,n

def factoriel(n) :
    f=1
    for i in range(1, n+1) :
        f*=i
        return f

def puissance(x, n) :
    p=1
    for i in range(1, n+1) :
        p*=x
        return p

def quotient(p,f) :
    q = p/f
    return q

def sommeHarmonique(x,n) :
    somme=0
    for i in range(0, n+1) :
        if i % 2 == 0 :
            somme += quotient(puissance(x, 2*i), factoriel(2*i))
        else :
            somme -= quotient(puissance(x, 2*i), factoriel(2*i))
    return somme

def principal() :
    a,b = saisie()
    c = sommeHarmonique(a,b)
    print(c)
    

if __name__ == '__main__':
    principal()     