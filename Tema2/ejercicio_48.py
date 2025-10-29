info_estudiantes = {"Jaime": [20,["Matemáticas","Lengua","geografía"]],"Álvaro": [19,["Programación", "Lenguaje de Marca", "Base de datos"]], "Andrés": [18,["Montaje de equipos", "Libre Configuración", "Sistemas Informáticos"]]}

info_estudiantes["Lola"] = [20,["Música", "FOL", "Educación Física"]]

print(info_estudiantes)
print("")

info_estudiantes["Álvaro"][1] = ["Física", "Tecnología", "Ingles"]

print(info_estudiantes)
print("")

print(f"Información Jaime: {info_estudiantes["Jaime"]}")
print("")

info_estudiantes.pop("Andrés")
print(info_estudiantes)
print("")


comprobar = "Jaime"

if comprobar in info_estudiantes:
    print(f"{comprobar} esta en el diccionario.")
else:
    print(f"{comprobar} no esta en el diccionario.")

print("")

print(f"Nombres de los estudiantes: {info_estudiantes.keys()}")
print("")

print(f"Información de los estudiantes: {info_estudiantes.values()}")
print("")

for i in info_estudiantes:
    print(f"Información de {i}: {info_estudiantes[i]}")


