"""Ejercicio 6:
Programa que lea un capital C, y que averigüe e imprima en cuantos meses 
se duplica, si lo colocamos a un interés compuesto del 5% mensual:"""


print("---------------------------------")
print("------INTERES EN UN CAPITAL------")
print("---------------------------------")

#input

c=int(input("Ingrese el capital: "))


#processing
n=0
x=c
d=c*2
while c<d:
    c=c+c*0.05
    n=n+1


#output
print("El capital ", x, "tarda ", n, " meses en duplicarse.")
