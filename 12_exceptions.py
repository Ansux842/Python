# Excepciones (Manejo de errores)

numberOne, numberTwo = 5, 1

numberTwo = "1"

# Try except
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# try except else finally
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Esto se ejecuta si no hay excepciones
    print("La ejecución continua correctamente")
finally:
    # Se ejecuta siempre, pase lo que pase.
    print("La ejecución continua")

# Captura de excepciones por tipo
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error: # Deberia ser TypeError, que es el error que tenemos aqui. Sirve para ver el error generico con Exception.
    print("Se ha producido un ValueError")
    print(error)
except Exception as exception:
    print("Se ha producido un ValueError")
    print(exception)