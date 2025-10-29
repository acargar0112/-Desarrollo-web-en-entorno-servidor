vinos_jerez = ["Sherry Classic", "Vino Blanco", "Fino SHERRY", "Moscatel", "ShErry Cream"]

vinos_analizados = {}

def analisis():
    # Recoge la lista de vinos y comprueba mediante un if si la palabra sherry existe en esa variable. La he convertido a minuscula para poder identificar cualquier Sherry da igual como este escrito. Todo esto lo he hecho iterando con un for en la lista.
    for i in vinos_jerez:
        if "sherry" in i.lower():
            vinos_analizados[i] = True
        else:
            vinos_analizados[i] = False
    return vinos_analizados

filtrado = filter(lambda i: "sherry" in i.lower(), vinos_jerez)


print(f"Diccionario de vinos: {analisis()}")
print(f"Lista de vinos con Sherry: {list(filtrado)}")
