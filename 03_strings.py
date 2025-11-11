# Strings

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string) 

my_new_line_string = "Este es un String \ncon un salto de linea."
print(my_new_line_string)

my_tab_line_string = "\tEste es un String con tabulación."
print(my_tab_line_string)

my_scape_line_string = "\tEste es un String \n escapado."
print(my_scape_line_string)

# Formateo

name, surname, age = "Sergio", "Carrasco", 31

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Se usa {} si queremos meter el item tal cual.
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # %s para formateos de tipo Strings, %d para formateos de tipo int.
print(f"Mi nombre es {name} {surname} y mi edad es {age}.") # Esto se llama inferencias.

# Desempaquetado de caractéres

language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Métodos o funciones del sistema

print(language.capitalize()) # Pone la primera letra en mayusculas.
print(language.upper()) # Pone la cadena de texto completa en mayusculas.
print(language.count("t")) # Cuenta cuantas unidades de lo que haya entre el segundo parentesis hay en lo que se busque.
print(language.isnumeric()) # Devuelve True o False según detecte o no que el contenido es un número. En este caso devuelve False.
print("1".isnumeric()) # Ejemplo de True ya que "1" es un número.
print(language.lower()) # Pone la cadena de texto completa en minusculas.
print(language.upper().isupper()) # Concatenación que pone en mayusculas y comprueba si está en mayusculas. En este caso devuelve True.
print(language.startswith("Py")) # Comprueba si comienza por lo que se pida en el segundo paréntesis. En este caso dará False ya que Python compara mayusculas y minusculas.