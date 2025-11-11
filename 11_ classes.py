# Clases

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname): # def __init__(self) es el constructor
        self.name = name
        self.surname = surname 

my_person = Person("Sergio", "Carrasco")
print(f"{my_person.name} {my_person.surname}")


class Person:
    def __init__(self, name, surname, alias = "Sin alias"): # def __init__(self) es el constructor
        self.full_name = f"{name} {surname} ({alias})" # Alias es un parámetro opcional. Atributo público.
        self.__name = name # Atributo privado, no se puede acceder desde fuera de la clase

    def get_name (self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} Está caminando")
my_person = Person("Sergio", "Carrasco")
print(my_person.full_name)
print(my_person.get_name()) # No se puede acceder al atributo privado directamente
my_person.walk()

my_other_person = Person("Sergio", "Carrasco", "Ansux")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Irene Camacho (Renn)" # Aqui no usamos el constructor sino que le damos el valor entero.
print(my_other_person.full_name)
print(type(my_other_person.full_name))

my_other_person.full_name = 619 # Como el tipado de Python es dinamico, podemos cambiar el tipo de dato.
print(my_other_person.full_name)
print(type(my_other_person.full_name))