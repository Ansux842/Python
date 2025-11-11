#Variables

# MyVariable = "My String Variable"

"""
Aunque esta forma de declarar la variable no esté mal, siguiendo las convenciones de Python 
debemos escribir el nombre de las variables en minúsculas y en snake case, es decir, 
con barras bajas en cada palabra.
"""
# Esta seria la forma correcta de declarar una variable.

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Podemos concatenar variables usando comas ",".
print(my_string_variable, my_int_to_str_variable, my_bool_variable)

# Esta es la forma de concatenar texto con variables.
print("Este es el valor de: ", my_bool_variable)

# Algunas funciones del sistema.
print(len(my_string_variable)) # Cuenta los caracteres que componen, en este caso, la variable.

# Variables en una sola línea. Mucho cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Sergio", "Carrasco", "Ansux", 31
print("Me llamo:", name, surname, ". Mi edad es:", age, "y mi alias es:", alias,".")

# Inputs. Son entradas por teclado en pantalla.
# name = input("¿Cual es tu nombre? ")
# age = input("¿Cuantos años tienes? ")

# print("Hola", name)
# print("Tienes", age, "años")

# Cambiamos su tipo
name = 31
age = "Sergio"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
print(type(address))