#EJERCICIO NÚMERO 3 // CREACIÓN DE UN SISTEMA DE RESERVA DE VUELOS

class Pasajero:
    def __init__(self, nombre, edad, cedula):
        
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula

class Vuelo(Pasajero):
    def __init__(self, nombre, edad, cedula, destino):
        super().__init__(nombre, edad, cedula)
    
        self.destino = destino
        
    pass

class Reserva(Pasajero):
    
    def __init__(self, nombre, edad, cedula, cl, asientos):
        super().__init__(nombre, edad, cedula)
        
        self.clase = cl
        self.asientos = asientos
        
    
    pass

def menu():
    
    print("¿DESEA REALIZAR UNA RESERVA DE VUELO EN NUESTRA AEROLINEA?")
    print(" 1.SI/2.NO")
    opcion = int(input('SELECCIONE:'))
    return opcion

def Datos(opcion):
    
    if opcion == 1:
        
        nombre = input("INGRESE SU NOMBRE:")
        edad = int(input("INGRESE SU EDAD"))
        cedula = int(input("INGRESE SU CEDULA"))
        destino = input("INGRESE SU DESTINO")

        pasajero = Vuelo(nombre,edad,cedula,destino)
        pass
    if opcion == 2:
        pass    

opcion = menu ()
