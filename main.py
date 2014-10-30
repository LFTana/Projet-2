##############################
###Caculatrice Hexadécimale###
##############################

w=0
x=(int(input("Entrez un nombre Héxadécimal : ")))
y=(int(input("Entrez un nombre Héxadécimal : ")))
z=(str(input("Entrez un signe de calcul: ")))
if z=="+":
    w=x+y
elif z=="*":
    w=y*x
print(w)
