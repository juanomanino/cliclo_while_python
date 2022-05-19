"""Ejercicio 2  :
Programa que dado un rango de números enteros, obtenga la
cantidad de números que contiene:"""

print("------------------------------------")
print("----CANTIDAD NÚMEROS EN UN RANGO----")
print("------------------------------------")

#input

a=int(input("Ingrese el extremo inferior del rango (a): "))
b=int(input("Ingrese el extremo superior del rango (b): "))


#processing
if a<b:
    s=0
    a=a+1
    while a<b:
        a=a+1
        s= s+1
else:
    print("a debe ser menor que b")

#output
print("La cantidad de números del rango es: ", s)

