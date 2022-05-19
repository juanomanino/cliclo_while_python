"""Ejercicio 4:
Programa que obtenga la cantidad de los primeros N números múltiplos de 5:"""


print("--------------------------------")
print("----PRIMEROS N MULTIPOS DE 5----")
print("--------------------------------")

#input

b=int(input("Ingrese n: "))


#processing
a=1
if a<b:
    s=0
    a=a+1
    while a<=b:
        r=a%5
        if r==0:
            s=s+1
        a= a+1


#output
print("La cantidad de números pares del rango es: ", s)

