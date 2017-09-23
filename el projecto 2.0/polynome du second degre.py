#déclaration de TOUTES les variables dans l'ordre d'apparition + set 0 des Vides


from math import*

#début du code parceque le code c'est important

A=float(input("Rentre la variable A:"))  #prend la valeur de A
B=float(input("Rentre la variable B:"))  #prend la valeur de B
C=float(input("Rentre la variable C:"))  #prend la valeur de C
Delta = pow(B,2)-4*A*C  #fait le calcul=Delta
print("Le discriminant vaut : ", Delta)  #rappel du calcul du discréminent



if Delta<0:         #condition nous permetant de voir si Delta est négatif, positif ou nul 
    print("Le resultat de Delta est négatif donc l'équation n'a pas de solution")
elif Delta==0:
    print("Le réqultat de Delta est nul donc la solution de l'équation est :")
    print(" x = -",B,"/ 2",A)
elif Delta>0:
    print("Le résultat de Delta est positif donc les solutions de l'équation sont :")
    x1 = ((-B+sqrt(Delta)))/(2*A)
    x2 = ((-B-sqrt(Delta)))/(2*A)
    print("x = ", x1)
    print("ou")
    print("x = ", x2)
    
#Je crois que c'est fini.
