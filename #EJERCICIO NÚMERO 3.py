#EJERCICIO NÚMERO 3 // CREACIÓN DE UN SISTEMA DE RESERVA DE VUELOS
class Vuelo:
    def __init__(self, origen, destino, fecha):

        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.asientos = 200
class Pasajero:
        
        def __init__(self, nombre, edad, cedula):

            self.nombre = nombre
            self.edad = edad
            self.cedula = cedula

class Reserva(Vuelo)
    def __init__(self, origen, destino, fecha, clase):
        super().__init__(origen, destino, fecha)
        
        self.clase = clase
    

def menu():
    
    print("INGRESE EL LUGAR AL CUAL DESEA VIAJAR DESDE COLOMBIA")
    print(" 1.ESPAÑA\n2.VENEZUELA\n3.ESTADOS UNIDOS\n4.NO SE ENCUENTRA SU LUGAR DESEADO")
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
        
        nombre = input("INGRESE SU NOMBRE:")
        edad = int(input("INGRESE SU EDAD"))
        cedula = int(input("INGRESE SU CEDULA"))
        destino = input("INGRESE SU DESTINO")

        pasajero = Vuelo(nombre,edad,cedula,destino)
        pass
    if opcion == 3:
        
        nombre = input("INGRESE SU NOMBRE:")
        edad = int(input("INGRESE SU EDAD"))
        cedula = int(input("INGRESE SU CEDULA"))
        destino = input("INGRESE SU DESTINO")

        pasajero = Vuelo(nombre,edad,cedula,destino)
        pass
    if opcion == 4:
        return None  

opcion = menu ()
