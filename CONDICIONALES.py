'''
Condicionales
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''

n = 4
if n >0:
    print("el numero es positivo")
else: 
    print("el numero es negativo")

#2. Ejercicio: Dado un número, imprime si es par o impar.

n = 2
if n % 2 == 0:
    print("es par")
else:
    print("es impar")

#3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.

a = 1
b = 2
c = 3
if a >= b and a>= c:
    print("el numero mayor es:{a}")
elif b >= a and b >= c:
    print("el numero mayor es:{b}")
elif c >= a and c>= b:
    print("el numero mayor es:{c}")
