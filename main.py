##############################
###Caculatrice Hexadécimale###
##############################

w=0
x=((input("Entrez un nombre Héxadécimal : ")))
# je dois pouvoir rentrer A2 par exemple comme nombre ...
y=(int(input("Entrez un nombre Héxadécimal : ")))
z=(str(input("Entrez un signe de calcul: ")))
if z=="+":
    w=x+y
elif z=="*":
    w=y*x
print(w)

print("hello")
