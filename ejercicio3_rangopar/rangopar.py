"""Ejercicio 3:
Dado un rango de números enteros obtenga la cantidad de números pares que contiene:"""


print("------------------------------------------")
print("----CANTIDAD NUMEROS PARES EN UN RANGO----")
print("------------------------------------------")

#input
suma=0
j=1
n=int(input("Dame el valor de n: "))

#processing

while j<=n:
    suma=suma+j
    j=j+1

#output
print("La suma de los ", n," primeros números naturales es: ",suma)

