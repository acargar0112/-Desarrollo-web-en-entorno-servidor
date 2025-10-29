invitados = ["Afrodita", "Zeus", "Cleopatra"]
for invitado in invitados:
    print(f"Estas invitado a mi fiesta. No faltes {invitado}")

print("Cleopatra no podra asistir a la fiesta.")

invitados[2] = "Vegeta777"

for invitado in invitados:
    print(f"Estas invitado a mi fiesta. No faltes {invitado}")

print("He encontrado una mesa más grande, ahora podrán asistir más personas!!")

invitados.insert(0, "Jaime")
invitados.insert(2, "Ango")
invitados.append("Rivas")

for invitado in invitados:
    print(f"Estas invitado a mi fiesta. No faltes {invitado}")



