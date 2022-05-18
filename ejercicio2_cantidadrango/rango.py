"""Ejercicio 2  :
Programa que dado un rango de números enteros, obtenga la
cantidad de números que contiene:"""

print("------------------------------------")
print("----CANTIDAD NÚMEROS EN UN RANGO----")
print("------------------------------------")

#input

x=int(input("Ingrese el primer número del rango: "))
y=int(input("Ingrese el último número del rango: "))
s=1

#processing

while x<y:
    x=x+1
    s= s+1

s=s-2
#output
print("La cantidad de números del rango es: ", s)

