##############################
###Caculatrice Hexadécimale###
##############################

b=((input("Entrez un nombre Héxadécimal : ")))  ##on entre le nomre hexadécimal à additionner ou multiplier## on le définit b##
c= '0x'                                       ## on doit définir c= '0x' pour que pythoon comprenne que nous travaillons en hex##    
d=int(c+b,16)                                 ##python commrend oxb, en base 16##

e=(str(input("Entrez un signe de calcul: ")))  ##on définit la chaîne de calcul e##

f=((input("Entrez un nombre Héxadécimal : ")))  ## on entre u la deuxieme valeur à additioner##
g=int(c+f,16)

if e=="+":
    a=d+g
elif e=="*":
    a=d*g

print(hex(a))    # la commande hex nous permet de définir tous les termes nécessaires au calcul, on évite ainsi décrire tous les nombres en héxadécimal##
print((a))
