"""Ejercicio 4:
Programa que obtenga la cantidad de los primeros N números múltiplos de 5:"""


print("--------------------------------")
print("----PRIMEROS N MULTIPOS DE 5----")
print("--------------------------------")

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

