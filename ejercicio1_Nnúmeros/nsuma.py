"""Ejercicio 1:
Programa que Calcular la suma de los N primeros números naturales:"""


print("--------------------------------")
print("----SUMA N NUMEROS NATURALES----")
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

