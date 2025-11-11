# Bucles

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es mayor o igual a 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1    
    if my_condition == 15:
        print("Mi condición es 15, saliendo del bucle")
        break  # Sale del bucle
    print(my_condition)

print("La ejecucion continua")

# For

my_list =  [31, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)
print(" ")
my_tuple = (32, 1.78, "Sergio", "Carrasco", "Sergio")
for  element in my_tuple:
    print(element)
print(" ")
my_set = {"Sergio", "Carrasco", 32}
for element in my_set:
    print(element)
print(" ")
my_dict = {"Nombre": "Sergio", "Apellido": "Carrasco", "Edad": 32, "Lenguajes": {"Python", "Swift", "Kotlin"}, 1: 1.78}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecucion continua")

my_dict = {"Nombre": "Sergio", "Apellido": "Carrasco", "Edad": 32, "Lenguajes": {"Python", "Swift", "Kotlin"}, 1: 1.78}
for element in my_dict:
    print(element)
    if element == "Edad":
        continue  # Continúa con la siguiente iteración
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
