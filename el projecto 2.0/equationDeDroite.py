from math import sqrt
from fractions import *

xa = 0 #variable des abscisses et des ordonnées
xb = 0
ya = 0
yb =0
result = 0 #variable du résultat
aa = 0 # a dans ax+b
bb = 0 #b dans ax+b

def eqDroite():
    response = "empty" #variable de la réponse 

    response = input("Que voulez vous caculer dans les équations de droite ? Le milieu ? la distance ? ")

    if response == "milieu":    # équation pour trouver le milieu de la droite
        xa = float(input("entrez la valeur de xa :"))		#input pas besoin de préciser
        xb = float(input("entrez la valeur de xb :"))
        ya = float(input("entrez la valeur de ya :"))
        yb = float(input("entrez la valeur de yb :"))

        result = (xb - xa) /2 , (yb - ya) / 2 ; # calcul xb- xa sur yb - ya
        print (result)

    elif response == "distance" : 				#calcul de la distance entre deux points
        xa = float(input("entrez la valeur de xa :"))
        xb = float(input("entrez la valeur de xb :"))
        ya = float(input("entrez la valeur de ya :"))
        yb = float(input("entrez la valeur de yb :"))

        result =  sqrt((xb - xa) ** 2 + (yb - ya) ** 2) #variable du résultat étant égal au calcul de la distance
        print(result)

    elif response == "équation de droite": #calcul ax +b
        xa = float(input("entrez la valeur de xa :"))
        xb = float(input("entrez la valeur de xb :"))
        ya = float(input("entrez la valeur de ya :"))
        yb = float(input("entrez la valeur de yb :"))


        aa = (yb - ya) / (xb - xa) #calcul pour trouver a 
        bb = xb / yb				#calcul pour trouver b
        if aa == -0.0:				#brève tentative  d'enlever un - du calcul
            aa == 0.0
        print ("y = " , aa,"x +", bb ) #écriture fractionner en chaîne du résultat












