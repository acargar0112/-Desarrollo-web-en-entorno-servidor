def mostrar_menu():
    print("MENU DE RESERVAS")
    print("1. Agregar reserva")
    print("2. Cancelar reserva")
    print("3. Calcular costo total de una reserva")
    print("4. Mostrar resumen de todas las reservas")
    print("5. Salir")


def agregar_reserva(reservas):
    try:
        nombre = input("Ingrese el nombre del cliente: ").strip().title()
        if nombre in reservas:
            print("ERROR, ya existe la reserva.")
            return

        noches = int(input("Ingrese el número de noches: "))
        if noches <= 0:
            print("ERROR, ingrese el número de noches:")
            return

        print("Tipos de habitación disponibles: [Sencilla, Doble, Suite]")
        tipo = input("Ingrese el tipo de habitación: ").strip().capitalize()

        if tipo not in ["Sencilla", "Doble", "Suite"]:
            print("ERROR, introduciste un tipo de habitación no disponible.")
            return

        reservas[nombre] = {"noches": noches, "tipo": tipo}
        print(f"Reserva agregada para {nombre}.")

    except ValueError:
        print("ERROR, intente más tarde.")


def cancelar_reserva(reservas):
    nombre = input("Ingrese el nombre del cliente a cancelar: ").strip().title()
    if nombre in reservas:
        del reservas[nombre]
        print(f"Reserva de {nombre} cancelada.")
    else:
        print("No existe una reserva con el nombre de cliente que has proporcionado.")


def calcular_costo(reservas):
    nombre = input("Ingrese el nombre del cliente: ").strip().title()
    if nombre not in reservas:
        print("No existe una reserva con ese nombre.")
        return

    tarifas = {"Sencilla": 50, "Doble": 100, "Suite": 150}
    r = reservas[nombre]
    costo = r["noches"] * tarifas.get(r["tipo"], 0)
    print(f"El costo total para {nombre} es: ${costo}")


def mostrar_resumen(reservas):
    if not reservas:
        print("No hay reservas registradas.")
        return

    tarifas = {"Sencilla": 50, "Doble": 100, "Suite": 150}
    print("RESERVAS")

    costos = {nombre: datos["noches"] * tarifas[datos["tipo"]] for nombre, datos in reservas.items()}

    for cliente, costo in costos.items():
        info = reservas[cliente]
        print(f"- {cliente}: {info['noches']} noches en habitación {info['tipo']} → ${costo}")

    print(f"\nTotal general: ${sum(costos.values())}")


def main():
    reservas = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                agregar_reserva(reservas)
            case "2":
                cancelar_reserva(reservas)
            case "3":
                calcular_costo(reservas)
            case "4":
                mostrar_resumen(reservas)
            case "5":
                print("Saliendo...")
                break
            case _:
                print("ERROR, intente de nuevo.")


if __name__ == "__main__":
    main()
