def main():
    pass

if __name__ == '__main__':
    main()

le_monde_est_plat = 1
if le_monde_est_plat:
    rebord = "Attention au rebord!".center(50)
    print (rebord)

a = 3
print(type(a))

#Pour faire des commentaires#

#écriture simplifiée TOUJOURS + AVANT =
a+=5
print(a)

b=4
c = a + b

print(a, '+', b, '=', c, "\n")
# a == 5 + 3 et b == 4
# donc a == 12


#transfomer en integer et afficher type + valeur
d = (int((50-5*6)/4))
print(type(d), d)

#afficher le type et la valeur
e = 7.0/2
print(type(e), e)

#transformer en float et afficher
f = (float(3))
print(f, "\n")

#\n saute une ligne\r correspond au caractère ASCII CR.
#\n correspond au caractère ASCII LF.
#CR te permettra de retourner en début de lignes
#tandis que LF te permettra d'aller à la ligne suivante.

#Les variables
g = (a<1)
print(type(g),"g =", g)
# => boolean false

h = 6/3
print(type(h), "h =", h)
# => float 2.0

i = 6//3
print(type(i), "i =", i, "\n")
# => int 2, les doubles // retounent un entier

j = a + b
print(type(i), "j =", i)
# int 2

k = a + f
print(type(k), "k =", k)
# float 11.0

print("***************".center(60))
print("\n JOUR SUIVANT\n".center(60))

l = "3.14"
print(type(l), "l =", l)#string on transforme en float
m = float(l)
print(type(m), "m =", m, "\n")
#n = l + m
# on ne peut pas concaténer 2 floats deux types différents

o = str(a)
p = str(f)
print(a, o, f, p, sep="***")
#8***8***3.0***3.0  ==> sep est u separateur, un paramètre de print
print("a+f=", a+f, " et o+p=", o+p)
#a+f= 11.0  et o+p= 83.0

texte= "Salut tu vas bien ??"
print('"', texte, '" Est affilié à la variable texte \n')

#prenom = input("Tapez votre prénom : ")
#print("Vous vous appelez : ", prenom)

#q = input ("Donnez un nombre : ")
#q = int(o) + 7


#r = float(input("Donnez un entier : "))
#print(type(r), r)
#float

#s = int(input("Donnez un entier :"))
#print(type(s), s)
#int

#t = int(3.14)
#print(type(t), t, "\n")
#int 3

u = 8
v = "Truc"

w = (u <= 10)
x = ( v == "truc")
y = (v < "truc")

print(type(w),"w = ", w)

print(type(x),"x = ", x)

print(type(y),"y = ", y, "\n")

# w and x
print("w and x", w  and x )

# w or x
print("w or x", w  or x )

# w or y
print("w or y", w  or y )

# not y
print("not y", not y )

# w or (not y)
print("w or (not y)", w  or (not y))

# w and (not y)
print("w and (not y)", w  and (not y))

# (not w) and x
print("(not w) and x",  (not w) or x)

# not (w and x)
print(" not (w and x)",  not( w and x), "\n")

z = 37
aa = 7
quotient = z//aa
reste = z%aa
print(z, "=", aa, "x", quotient, "+", reste, "\n")




