#EJERCICIO NÚMERO 3 // CREACIÓN DE UN SISTEMA DE RESERVA DE VUELOS
class Vuelo:
    def __init__(self, origen, destino, fecha):

        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.asientos = []
class Pasajero(Vuelo):
    def __init__(self, origen, destino, fecha, nombre, edad, cedula):
        super().__init__(origen, destino, fecha)    
    
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula

class Reserva(Pasajero):
    def __init__(self, origen, destino, fecha, nombre, edad, cedula,clase):
        super().__init__(origen, destino, fecha, nombre, edad, cedula)
    
        self.clase = clase
        self.costo = 0


    def Tipeclass(self):

        if self.clase.lower() == "economica":

            self.asientos = []
            while True:
                asiento = int(input("Seleccione un asiento: "))
                if asiento in self.asientos:
                    print(f"El asiento {asiento} ya ha sido seleccionado. Por favor, seleccione otro.")
                else:
                    self.asientos.append(asiento)
                    print(f"Ha seleccionado el asiento {asiento}.")
                return self.asientos
            
        if self.clase.lower() == "ejecutiva":

            self.asientos = []
            while True:
                asiento = int(input("Seleccione un asiento: "))
                if asiento in self.asientos:
                    print(f"El asiento {asiento} ya ha sido seleccionado. Por favor, seleccione otro.")
                else:
                    self.asientos.append(asiento)
                    print(f"Ha seleccionado el asiento {asiento}.")
                    return self.asientos

            
        if self.clase.lower() == "primera clase":
          
            self.asientos = []
            while True:
                asiento = int(input("Seleccione un asiento: "))
                if asiento in self.asientos:
                    print(f"El asiento {asiento} ya ha sido seleccionado. Por favor, seleccione otro.")
                else:
                    self.asientos.append(asiento)
                print(f"Ha seleccionado el asiento {asiento}.")
                return self.asientos

    def Cost(self):

        if self.clase.lower() == "economica":
            return self.costo + 500000
    
        if self.clase.lower() == "ejecutiva":
            return self.costo + 1500000
            
        if self.clase.lower() == "primera clase":
            return self.costo + 2500000
        else:
            return self.costo
            



def menu():
    
    print("BIENVENIDO AL CENTRO DE RESERVAS DE NUESTRA AEROLINEA")
    print("DESEA REALIZAR UNA RESERVA\nESCRIBA:\nSI\nNO")
    opcion = input('SELECCIONE:')
    return opcion

def Datos(opcion):
    
    if opcion.lower() == "si":
        
        nombre = input("INGRESE SU NOMBRE:")
        edad = int(input("INGRESE SU EDAD:"))
        cedula = int(input("INGRESE SU CEDULA:"))
        origen = input("INGRESE SU LUGAR DE ORIGEN:")
        destino = input("INGRESE SU DESTINO:")
        clase = input("INGRESE LA CLASE EN LA CUAL DESEA REALIZAR SU VIAJE (economica, ejecutiva, primera clase):")
        fecha = input("INGRESE LA FECHA EN LA CUAL DESEA REALIZAR SU VIAJE:")
        
        pasajero = Reserva(origen,destino,fecha,nombre,edad,cedula,clase)
        pasajero.Tipeclass()
        return pasajero

    if opcion.lower() == "no":
        return None  

opcion = menu ()
lista = []
contador = 0
while opcion.lower() != "no":
    contador += 1
    pasajero = Datos(opcion)
    if pasajero is not None:
        lista.append(pasajero)
    opcion = menu()

print("                 INFORMACIÓN TRIPULANTES         ")
print(" NOMBRE    EDAD    DNI   ORIGEN   DESTINO  CLASE  COSTO VUELO")
for pasajero in lista:
    
    costo = pasajero.Cost()

    print(pasajero.nombre, pasajero.edad, pasajero.cedula, pasajero.origen, pasajero.destino, pasajero.clase, costo)

print("TOTAL PASAJEROS:", contador)
