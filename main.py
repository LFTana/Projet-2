##############################
###Caculatrice Hexadécimale###
##############################

b=((input("Entrez un nombre Héxadécimal : ")))  ##on entre le nomre hexadécimal à additionner ou multiplier## on le définit b##
c= '0x'                     
d=int(c+b,16)

e=(str(input("Entrez un signe de calcul: ")))

f=((input("Entrez un nombre Héxadécimal : ")))
g=int(c+f,16)

if e=="+":
    a=d+g
elif e=="*":
    a=d*g

print(hex(a))
print((a))
