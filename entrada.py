# function input -> retorna string
num_a = int(input("Ingresa el numero: "))
num_b = int(input("Ingresa el numero: "))

print(num_a + num_b)
name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad:"))
city = input("Ingresa tu ciudad/pueblo: ")

#string fromart
""" 
      Hola, soy name, tengo age años y vivo en city
"""
greeting = "Holaa, soy {}, tengo {} años y vivo en {}"
print(greeting.format(name, age,city))
greeting_2 = "Holaa, soy { name }, tengo { age } años y vivo en { city }"

print(greeting.format(name, age, city))