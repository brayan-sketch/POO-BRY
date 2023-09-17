estudiantes = {}

class Estudiante:
    def calcular_nota_final(self, notas):
        nota_final = sum(notas) / len(notas)
        resultado = "Gana" if nota_final >= 3.5 else "Pierde"
        return nota_final, resultado

while True:
    print("\n******* Menu *******")
    print("1. Agregar estudiante")
    print("2. Modificar nota")
    print("3. Calcular nota final")
    print("4. Salir")

    opcion = input("Eliga una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        notas = []
        for i in range(3):
            nota = float(input(f"Ingrese la nota {i + 1} del estudiante: "))
            notas.append(nota)
        estudiantes[nombre] = notas
        print(f"Estudiante {nombre} agregado con éxito.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
            nota_a_modificar = int(input("Ingrese el número de la nota a modificar (1, 2 o 3): "))
            if 1 <= nota_a_modificar <= 3:
                nueva_nota = float(input("Ingrese la nueva nota: "))
                estudiantes[nombre][nota_a_modificar - 1] = nueva_nota
                print(f"Nota {nota_a_modificar} modificada con éxito.")
            else:
                print("Número de nota inválido.")
        else:
            print(f"El estudiante {nombre} no existe en la base de datos.")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
            notas = estudiantes[nombre]
            nota_final, estado = Estudiante().calcular_nota_final(notas)
            print(f"Nota final de {nombre}: {nota_final:.2f}")
            print(f"El estudiante {nombre} {estado}.")
        else:
            print(f"El estudiante {nombre} no existe.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no invalida. Por favor, elija una opción válida.")