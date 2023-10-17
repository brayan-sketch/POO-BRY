import random

class Personaje:
    id = 0
    nombre = ""
    monedas = 0
    vidas = 3
    tamaño = 'pequeño'
    mundo = 1
    nivel = 1
    p_disparar = False 

    def __init__(self, nombre):
        self.nombre = nombre

    def setmonedas(self, cant):
        self.monedas += cant
        while self.monedas >= 100:
            self.monedas -= 100
            self.vidas += 1
    
    def setmundo(self, n_mundo):
        if n_mundo > 8:
            self.mundo = 1
        else:
            self.mundo = n_mundo
        self.nivel = 1
    
    def setnivel(self, n_nivel):
        if n_nivel > 4:
            self.nivel = 4
        else:
            self.nivel = n_nivel
    
    def sethongo(self):
        if self.tamaño == 'pequeño':
            self.tamaño = 'grande'
        elif self.tamaño == 'grande':
            self.p_disparar = True

    def sethongo_vida(self):
        self.vidas += 1

    def setflor(self):
        if self.tamaño == 'grande':
            self.p_disparar = True

    def setincidente(self, tipo):
        if self.vidas > 0:
            if tipo == 'sencillo':
                if self.tamaño == 'pequeño':
                    self.vidas -= 1
                else:
                    self.tamaño = 'pequeño'
                    self.p_disparar = False
            elif tipo == 'grave':
                self.vidas -= 1
        else:
            print("No te quedan mas vidas.")

    def g_inicidente(self):
        pasos_incidente = random.randint(1, 200)
        return pasos_incidente

    def reiniciar(self):
        self.monedas = 0
        self.vidas = 3
        self.tamaño = 'pequeño'
        self.mundo = 1
        self.nivel = 1
        self.p_disparar = False
        print("Reinicio")

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Monedas: {self.monedas}")
        print(f"Vidas: {self.vidas}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Mundo: {self.mundo}")
        print(f"Nivel: {self.nivel}")
        print(f"Poder de Disparo: {'Sí' if self.p_disparar else 'No'}")

personajes = {
    1: Personaje("Mario"),
    2: Personaje("Luigi")
}

while True:
    print("Personajes")
    print("")
    print("1. Mario")
    print("2. Luigi")
    print("")
    opc = input("Elige un personaje: ")
    if opc.isdigit() and 1 <= int(opc) <= 2:
        p_elegido = personajes[int(opc)]
        break
    else:
        print("Opcion no valida.")

print(f"Informacion de {p_elegido.nombre}:")
p_elegido.mostrar()

pasos = 0
while True:
    pasos += 1
    print(f"\nPasos: {pasos}")

    pasos_incidente = p_elegido.g_inicidente()
    if pasos >= pasos_incidente:
        tipo_incidente = random.choice(["sencillo", "grave"])
        print(f"Incidente {tipo_incidente} ocurrido!")
        p_elegido.setincidente(tipo_incidente)

    p_elegido.mostrar()
    continuar = input("¿Deseas continuar? (s/n): ")
    if continuar.lower() != 's':
        break
