#Ciclo While 
#Whilw Exp_bool: True

i=0
num=7
while i <= 10:
    print(f"{num} * {i} = {num*i}")
    i += 1
else:
    print("ciclo terminado")
#ciclo  inifinito
while True:
    #Rompemos con break
    break
#El  for recorre iterables
#Un iterable es algo que se puede recorrer

#for variable in iterables
my_string = "Hola"
for letra in my_string:
    print(letra, end=",")
lista = ["uno", "dos", "tres", "cuatro"]
for item in lista:
    print(item)

#function range
#range (end)
for i in range (10):
    print(i, end= '.')
print()
#range(ini,end)
for i in range (10,20):
    print(i, end= '.')
print()
# range(ini,end,step)
for i in range (10,20,2):
    print(i, end= '.')
print()