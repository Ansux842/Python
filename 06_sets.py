# Sets

my_set = set()
my_other_set = {}

print(type(my_set))  # <class 'set'>
print(type(my_other_set))  # Inicialmente es un <class 'dict'>, un diccionario.

my_other_set = {"Sergio", "Carrasco", 32}
print(type(my_other_set)) # Ahora es un <class 'set'>

print(len(my_other_set)) # len() devuelve el número de elementos en el set

# print(my_other_set[0]) Esto dará un error, los sets no son indexados

my_other_set.add("Ansux")
print(my_other_set) # Un set no tiene orden.

my_other_set.add("Ansux") # No se añade porque ya existe el elemento, los sets no permiten duplicados.
print(my_other_set)

print("Sergio" in my_other_set) # Devuelve True o False si el elemento está en el set.
print("Irene" in my_other_set)

my_other_set.remove("Ansux") # Elimina el elemento "Ansux"
print(my_other_set) 

my_other_set.discard("Sergio") # Elimina "Sergio" si existe, no da error si no existe
print(my_other_set)

my_other_set.clear() # Elimina todos los elementos del set
print(len(my_other_set))

del my_other_set # Elimina el set por completo
# print(my_other_set) Esto dará un error porque my_other_set ya no existe

my_set = {"Sergio", "Carrasco", 32}
print(type(my_set))  # <class 'set'>
my_list = list(my_set)
print(my_list)  # Convierte el set a una lista, el orden puede variar
print(my_list[0])
print(type(my_list))

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set) # Une dos sets
print(my_new_set)  # {'Kotlin', 'Swift', 'Python', 'Sergio', 'Carrasco', 32}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))  # Unión de sets, no duplica elementos

print(my_new_set.difference(my_set)) # Elementos en my_new_set que no están en my_set

print(my_new_set.intersection(my_set)) # Elementos comunes entre my_new_set y my_set