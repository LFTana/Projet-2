##############################
###Caculatrice Hexadécimale###
##############################
(Il faut utiliser hex() qui permet de convertir un nombre decimal en hexadecimal sur python)

##############################
#je propose une petite piste : 
a = 'A2'                      
b='0x'                        
c=int(b+a,16)                 
print(c)
print(hex(c))
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
