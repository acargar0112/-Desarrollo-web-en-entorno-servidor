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

print("Lo siento pero solo podrán asistir 2 personas a la fiesta al final")

while len(invitados) > 2:
    eliminado = invitados.pop()
    print(f"Lo siento {eliminado} al final no puedes venir a la fiesta.")

for invitado in invitados:
    print(f"No te preocupes {invitado}, tu sigues invitado a la fiesta.")

del invitados[0]
del invitados[0]

print(invitados)