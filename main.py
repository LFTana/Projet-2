##############################
###Caculatrice Hexadécimale###
##############################


b=((input("Entrez un nombre Héxadécimal : ")))
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
