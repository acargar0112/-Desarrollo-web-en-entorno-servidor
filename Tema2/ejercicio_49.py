inventario = {"manzanas": {"precio": 1,"cantidad": 109,"reseñas": [7, 6, 9]},"queso": {"precio": 1.6,"cantidad": 27,"reseñas": [5, 4, 5]},"pan": {"precio": 0.8,"cantidad": 35,"reseñas": [10, 9, 6]}}

inventario["peras"] = {"precio": 0.8,"cantidad": 55, "reseñas": [8,4,6]}

print(inventario)
print("")


inventario["pan"]["precio"] = 1.2
inventario["pan"]["cantidad"] = 20

print(inventario)
print("")


print(f"Información Manzanas: {inventario["manzanas"]}")
print("")


inventario.pop("manzanas")
print(inventario)
print("")


comprobar = "peras"

if comprobar in inventario:
    print(f"{comprobar} esta en el inventario.")
else:
    print(f"{comprobar} no esta en el inventario.")


print(f"Nombres de los productos: {inventario.keys()}")
print("")


print(f"Nombres de los productos: {inventario.values()}")
print("")


for i in inventario:
    print(f"Información de {i}: {inventario[i]}")
