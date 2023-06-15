drinks = []

def add_drink(drink):
    drinks.append(drink)
def del_drink(drink):
    try:
       drinks.remove(drink)   
    except Exception:
        print("Error 404") 
def show_drinks():
    print("_" * 4, "My drinks", "_" * 4) 
    for drink in drinks:
        print("-->", drink)

choice_text = ''' 
Elige una opcion:
1.- Agregar
2.- Eliminar
3.- Mostrar
4.- Salir
'''   
while True: 
   choice_user = int(input(choice_text))
   if choice_user == 1:
       drink = input ('Ingresa una bebida: ')
       add_drink(drink)
   elif choice_user == 2:
       drink = input('Ingresa una bebida')
       del_drink(drink)
   elif choice_user == 3: 
       show_drinks()
   elif choice_user == 4:
       break
   else:
       print('Opcion incorrecta')   

