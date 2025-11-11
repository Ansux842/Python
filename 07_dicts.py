# Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Sergio", "Apellido": "Carrasco", "Edad": 32, 1: "Python"} # Mezclamos String con int como claves

my_dict = {
    "Nombre": "Sergio", 
    "Apellido": "Carrasco", 
    "Edad": 32, 
    "Lenguajes": {"Python", "Swift", "Kotlin"}, # Un String como clave con un set como valor
    1: 1.78
    }

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"]) # Acceso a un valor por su clave -------------------------IMPORTANTE-------------------------

my_dict["Nombre"] = "Pedro" # Modificamos el valor de una clave
print(my_dict["Nombre"])

print(my_dict[1]) # Acceso a un valor por su clave, en este caso un int

my_dict["Calle"] = "Calle Falsa 123" # Añadimos una nueva clave y su valor -------------------------IMPORTANTE-------------------------
print(my_dict)
print(my_dict["Calle"])

del my_dict["Calle"] # Eliminamos una clave y su valor -------------------------IMPORTANTE-------------------------
print(my_dict) 

my_dict.pop("Apellido") # Eliminamos una clave y su valor, pero obtenemos el valor eliminado -------------------------IMPORTANTE-------------------------
print(my_dict)

print("Sergio" in my_dict) # Comprobamos si una CLAVE existe en el diccionario, devuelve True o False
print("Nombre" in my_dict) 

print(my_dict.items()) 
print(my_dict.keys()) # Obtenemos las CLAVES del diccionario
print(my_dict.values()) # Obtenemos los VALORES del diccionario

my_list = ["Nombre", 1, "Apellidos"]

my_new_dict = dict.fromkeys((my_list)) # Creamos un nuevo diccionario con las claves del diccionario original y un valor por defecto
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Apellidos"))
print(dict.fromkeys((my_new_dict)))

my_new_dict = dict.fromkeys(my_dict) # Creamos un nuevo diccionario con las claves del diccionario original y un valor por defecto
print(dict.fromkeys((my_new_dict)))

my_new_dict = dict.fromkeys(my_dict, "KSOMG") # Creamos un nuevo diccionario con las claves del diccionario original y un valor por defecto
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))