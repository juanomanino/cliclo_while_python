"""Ejercicio 5:
Programa que dado un número determinar cuántos dígitos tiene:"""


print("--------------------------------")
print("------DIGITOS DE UN NÚMERO------")
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

