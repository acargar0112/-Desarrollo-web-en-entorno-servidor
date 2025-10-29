nota = int(input("Introduzca una nota: "))

if nota <= 4:
    print("Suspenso")
elif nota <= 6:
    print("Aprobado")
elif nota <= 8:
    print("Notable")
else:
    print("Sobresaliente")