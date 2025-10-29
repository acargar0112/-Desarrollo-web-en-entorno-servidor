videojuegos = ["Minecraft", "Valorant","Wow"]
cont=0

for videojuego in videojuegos:
    cont += 1
    print(f"Videojuego Nº{cont}: {videojuego}")


videojuegos[1] = "Rust"

print("Videojuego sustituado")

videojuegos.insert(0, "Ark")
videojuegos.insert(2, "CallofDuty")
videojuegos.append("Gris")

print("Videojuegos insertados")

print(f"Ordenada: {sorted(videojuegos)}")
print(videojuegos)

print(f"Ordenada inversa: {sorted(videojuegos, reverse=True)}")
print(videojuegos)


videojuegos.reverse()
print(f"Reverse1: {videojuegos}")

videojuegos.reverse()
print(f"Reverse2: {videojuegos}")

videojuegos.sort()
print(f"Sort1: {videojuegos}")

videojuegos.sort(reverse=True)
print(f"Sort1: {videojuegos}")

print(f"Cantidad de videojuegos en mi lista: {len(videojuegos)}")


while len(videojuegos) > 2:
    eliminado = videojuegos.pop()
    print(f"{eliminado} a sido eliminado.")

cont2= 0
for videojuego in videojuegos:
    cont2 += 1
    print(f"Videojuego Nº{cont2}: {videojuego}")

del videojuegos[0]
del videojuegos[0]

print(videojuegos)



