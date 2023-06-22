#Funciones en python 
#def name_function(params);
#  codigo
#  return

#Funcion sin parametro y sin retorno
def saludos():
    print("Hola")
saludos()

#funcones con 1 parametro
def get_age_in_future(age):
    print(f"En 3 años tendras {age + 3} años")
get_age_in_future(39)

#Funciones con 2 parametros sin retorno
def suma(num1, num2):
    print(f"{num1} + {num2} = {num1+num2}")
suma(12,35)

#funciones con parametros opcionales
def get_heroes (heroe1= "Iron Man", heroe2="Spiderman" ):
    print([heroe1, heroe2])
get_heroes()
get_heroes("Flash")
get_heroes("Flash","Superman")
get_heroes(heroe1="Flash", heroe2="Superman")

#Funciones con retorno
def title(texto):
    return texto.title()

text_changed= title("Hola jejej")
print(text_changed)