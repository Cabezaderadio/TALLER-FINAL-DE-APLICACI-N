import time

class Vehiculo:

    def __init__(self, marca, velocidad):

        self.marca = marca
        self.velocidad = velocidad

    def mover(self):

        print("Vehiculo en movimiento")

class trafico:

    def __init__(self):

        self.parar = "ROJO"

    def Semaforo(self):

        if self.parar == "ROJO":

            self.parar = "VERDE"
        else:

            self.parar = "ROJO"

    def Verde(self):

        return self.parar == "Verde"
    
class  Cruce:

    def __init__(self, cruce, semaforo):

        self.cruce = cruce
        self.semaforo = semaforo

    def simulartraafico(self):

        while True:
            for semaforo in self.semaforo:
                semaforo.change_state()

            print(f"\n{self.name} - Traffic state:")
            for semaforo in self.semaforo:
                state = "green" if semaforo.is_green() else "red"
                print(f"{semaforo}: {state}")

            time.sleep(2)


carro = Vehiculo("Cherolet", 45)
carro2 = Vehiculo("Mazda", 20)

semaforo1 = trafico()
semaforo2 = trafico()

cruce1 = Cruce("Cruce 1", [semaforo1])
cruce2 = Cruce("Cruce 2", [semaforo2])

carro.mover()
carro2.mover()