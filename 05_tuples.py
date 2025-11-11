# Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (32, 1.78, "Sergio", "Carrasco", "Sergio")
my_other_tuple = (36, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Sergio")) # Cuenta cuántas veces aparece el elemento
print(my_tuple.index("Carrasco")) # Devuelve el índice del primer elemento encontrado
print(my_tuple.index("Sergio")) # Devuelve el índice del primer elemento encontrado

# my_tuple[5] = 1.80
# print(my_tuple)  # TypeError: 'tuple' object does not support item assignment


my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])  # Slicing de tuplas

my_tuple = list(my_tuple)
print(type(my_tuple))  # Convertir tupla a lista

my_tuple[4] = "KSOMG"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)  # Convertir lista de nuevo a tupla
print(my_tuple)
print(type(my_tuple))  # Verifica el tipo de dato

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple)  NameError: name 'my_tuple' is not defined