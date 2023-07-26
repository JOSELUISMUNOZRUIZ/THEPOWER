#1. Ejercicio: Define una función que tome dos números y retorne su suma.


def suma(a, b):
    return a + b 
resultado = suma(5, 3)
print(resultado)

#2. Ejercicio: Define una función que tome un número y retorne su factorial.

def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado
fact3=factorial(3)
print(fact3)

#3. Ejercicio: Define una función que tome un número y determine si es primo.

a = 2

def es_primo(num):
      contador = 0
      for i in range(1, num+1):
            contador += 1
      if contador == 2:
            return True
      else:
            return False
print(es_primo(a))


#4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.

def suma(numeros):
      suma = 0 
      for numero in numeros:
            suma += numero
      return suma 

lista = [2, 4, 6, 8]
print(suma(lista))

#5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.

def bienvenido(nombre):
      print(f"hola {nombre}")
bienvenido("Jose Luis")
print(bienvenido)