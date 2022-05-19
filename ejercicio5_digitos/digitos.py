"""Ejercicio 5:
Programa que dado un número determine cuántos dígitos tiene:"""


print("--------------------------------")
print("------DIGITOS DE UN NÚMERO------")
print("--------------------------------")

#input

n=int(input("Ingrese n: "))


#processing
s=0
x=n
while n>0:
    n=n//10
    s=s+1


#output
print("El número ", x, "tiene : ", s, " dígitos.")
