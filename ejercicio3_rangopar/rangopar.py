"""Ejercicio 3:
Dado un rango de números enteros obtenga la cantidad de números pares que contiene:"""


print("------------------------------------------")
print("----CANTIDAD NUMEROS PARES EN UN RANGO----")
print("------------------------------------------")

#input

a=int(input("Ingrese el extremo inferior del rango (a): "))
b=int(input("Ingrese el extremo superior del rango (b): "))


#processing
if a<b:
    s=0
    a=a+1
    while a<b:
        r=a%2
        if r==0:
            s=s+1
        a= a+1
else:
    print("a debe ser menor que b")

#output
print("La cantidad de números pares del rango es: ", s)

