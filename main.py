##############################
###Caculatrice Hexadécimale###
##############################

#Initialisation:
b=((input("Entrez un nombre Héxadécimal : ")))  ## On entre un nombre hexadécimal, on le définit b
d=int(b,16)                                     ## d prend la valeur b comme étant un nombre entier hexadécimal en base 16

e=(str(input("Entrez un signe de calcul, + ou * : ")))  ## On définit la chaîne de calcul e, e vaut + ou *

f=((input("Entrez un nombre Héxadécimal : ")))  ## On entre un deuxieme nombre hexadécimal, on le définit f
g=int(f,16)                                     ## g prend la valeur f comme étant un nombre entier hexadécimal en base 16

#Traitement:
if e=="+":                       ## Si e est égale à "+"
    a=d+g                        ## alors les deux valeurs d et g vont s'additionner
elif e=="*":                     ## Sinon si e est égale à "*"
    a=d*g                        ## alors d et g vont se multiplier

#Sortie:
chr = str(hex(a))                 ## Le résultat hexadécimal de a est considéré comme une chaîne : chr
chr=chr[2:]                       ## On décompose chr, on aura donc à l'affichage toutes les valeurs sauf les deux premières "0x"

print("Le résultat vaut ",chr.upper(), " en Héxadécimal et ",a, " en Décimal.")    ## On affiche le résultat chr.upper() qui est en hexadécimal et en majuscule, et a qui est en décimal
