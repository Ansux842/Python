# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list =  [31, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [32, 1.78, "Sergio", "Carrasco"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30)) # Cuenta la cantidad de veces que aparece un elemento en la lista
# print(my_other_list[-5]) IndexError value error, no existe el índice -5
# print(my_other_list[4]) IndexError value error, no existe el índice 4

age, height, name, surname = my_other_list # Asignación de variables
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] # Reasignación de variables
print(age)

print(my_list + my_other_list)  # Concatenación de listas
print(my_list * 2)  # Repetición de listas

my_other_list.append("KSOMG") # Añade un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") # Inserta un elemento en la posición indicada
print(my_other_list)

my_other_list[1] = "Azul" # Modifica el elemento en la posición indicada
print(my_other_list)

my_other_list.remove("Azul") # Elimina el primer elemento que coincida con el valor
print(my_other_list)

my_list.remove(30) # Elimina el primer elemento que coincida con el valor
print(my_list)

print(my_list.pop()) # Elimina el elemento en la posición indicada y lo devuelve
print(my_list) 

my_pop_element = my_list.pop(2) # Elimina el elemento en la posición indicada y lo guarda en una variable
print(my_pop_element) 
print(my_list)

del my_list[2] # Elimina el elemento en la posición indicada
print(my_list)

my_new_list = my_list.copy() # Crea una copia de la lista

my_list.clear() # Elimina todos los elementos de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # Invierte el orden de los elementos de la lista
print(my_new_list)

my_new_list.sort() # Ordena los elementos de la lista
print(my_new_list)

print(my_new_list[1:3]) # Slicing, devuelve una sublista desde el índice 1 hasta el 3 (sin incluir el 3)

my_list = "Hola Python"
print(my_list)
print(type(my_list))