evento = {
    "combates": {
        #"Main Event": {
        #   "luchadores": ["StreamerA", "StreamerB"],
        #   "rounds": 3,
        #   "peso": "LIGERO",
        #   "resultado": None
        #} ESTRUCTURA
    },
    "artistas": [
        #{"nombre": "Artista1", "setlist": ["Tema1", "Tema2"]} ESTRUCTURA
    ],
    "entradas": {
        "vendidas": 0,
        "tipos": {"general": 25.0, "premium": 60.0, "vip": 120.0}
    },
    "staff": {
        "seguridad": {"miembros": {"Ana", "Luis", "Eva"}},
        "ring": {"miembros": {"Pablo", "Irene"}}
    }
}

# EXCEPCIONES

class Resultado_completado(Exception):
    pass

def comprobar_resultado(evento):
    for i in evento["combates"].values():
        if i["resultado"] != None:
            raise Resultado_completado("Este combate ya ha sido cerrado.")
    return True

class Artista_existente(Exception):
    pass

def comprobar_artista_existente(evento,nombre):
    for i in evento["artistas"]:
        if nombre == i.nombre:
            raise Artista_existente("El artista ya existe.")
    return nombre

class Combate_invalido(Exception):
    pass

def comprobar_combate_invalido(evento, titulo):
    if titulo not in evento["combates"]:
        raise Combate_invalido("El combate no existe.")
    return titulo

class Ganador_invalido(Exception):
    pass

def comprobar_ganador_invalido(evento,titulo,ganador):
    for i in evento["combates"][titulo]["luchadores"]:
        if ganador == i.nombre:
            return ganador
    raise Ganador_invalido("El ganador no existe.")

class Combate_existente(Exception):
    pass

def comprobar_combate_existente(evento,titulo):
    if titulo in evento["combates"]:
        raise Combate_existente("Titulo de combate utilizado.")
    return titulo

class Combate_rounds(Exception):
    pass

def comprobar_numero_rounds(rounds):
    if rounds > 5:
        raise Combate_rounds("El número de rounds tiene que ser inferior a 5.")
    return rounds

class Combate_str(Exception):
    pass

def comprobar_combate_str(titulo,luchador1,luchador2,peso):
    combate_str_list = [titulo,luchador1,luchador2,peso]
    for i in combate_str_list:
        if type(i) is not str:
            raise Combate_str(f"La entrada ({i}) debe de ser str.")
    return titulo

class Temas_str(Exception):
    pass

def comprobar_tema_str(*temas):
    for i in temas:
        if type(i) is not str:
            raise Temas_str("La entrada de los temas no es str.")
    return temas

class Comprobar_artista(Exception):
    pass

def comprobar_artista_str(nombre):
    if type(nombre) is not str:
        raise Comprobar_artista("La entrada del artista no es str.")
    return nombre


class Tipo_Entrada(Exception):
    pass

def comprobar_entrada(evento,tipo):
    if tipo not in evento["entradas"]["tipos"].keys():
        raise Tipo_Entrada("Este tipo de entrada no es válido.")
    return tipo

# FUNCIONES

def vender_entradas(evento,tipo,unidades):
    suma = 0
    try:
        comprobar_entrada(evento,tipo)
    except Tipo_Entrada as e:
        print(f"ERROR: {e}")
    else:
        match tipo.lower().strip():
            case "general":
                suma += evento["entradas"]["tipos"]["general"] * unidades
            case "premium":
                suma += evento["entradas"]["tipos"]["premium"] * unidades
            case "vip":
                suma += evento["entradas"]["tipos"]["vip"] * unidades
        evento["entradas"]["vendidas"] += unidades
        return f"Se han vendido {unidades} entradas {tipo} por un total de {suma} €"
    
def agregar_artista(evento, nombre, *temas):
    try:
        comprobar_tema_str(*temas)
        comprobar_artista_str(nombre)
        comprobar_artista_existente(evento,nombre)
    except Temas_str as e:
        print(f"ERROR: {e}")
    except Comprobar_artista as i:
        print(f"ERROR: {i}")
    except Artista_existente as j:
        print(f"ERROR: {j}")
    else:
        nuevo_artista = Artista(nombre, list(temas))
        evento["artistas"].append(nuevo_artista)
        return "Artista añadido correctamente."
    

def programar_combate(evento, titulo, luchador1, luchador2, rounds, peso):
    try:
        comprobar_combate_str(titulo,luchador1,luchador2,peso)
        comprobar_numero_rounds(rounds)
        comprobar_combate_existente(evento,titulo)
    except Combate_str as e:
        print(f"ERROR: {e}")
    except Combate_rounds as i:
        print(f"ERROR: {i}")
    except Combate_existente as j:
        print(f"ERROR: {j}")
    else:
        l1 = Luchador(luchador1, peso)
        l2 = Luchador(luchador2, peso)
        nuevo_combate ={"luchadores": [l1,l2],
                        "rounds": rounds,
                        "peso": peso,
                        "resultado": None}
        #Añadimos con Titulo para que no sobrescribir el anterior combate que hemos metido.
        evento["combates"][titulo] = nuevo_combate
        return "Combate programado correctamente."

def cerrar_resultado(evento, titulo, ganador):
    try:
        comprobar_combate_invalido(evento,titulo)
        comprobar_ganador_invalido(evento,titulo,ganador)
        comprobar_resultado(evento)
    except Combate_invalido as e:
        print(f"ERROR: {e}")
    except Ganador_invalido as i:
        print(f"ERROR: {i}")
    except Resultado_completado as j:
        print(f"ERROR: {j}")
    else:
        evento["combates"][titulo]["resultado"] = ganador
        return f"Resultado registrado: ganó {ganador}"

# FUNCIONES AUXILIARES LUCHADORES

def combates_pendientes(evento):
    contador = 0
    for i in evento["combates"]:
        if evento["combates"][i]["resultado"] == None:
            contador += 1
    return contador

def combates_cerrados(evento):
    contador = 0
    for i in evento["combates"]:
        if evento["combates"][i]["resultado"] != None:
            contador += 1
    return contador

def combates_totales(evento):
    return len(evento["combates"])

def informe_completo(evento):

    print("=== INFORME DE LA VELADA ===")
    print("")
    print(f"Combates totales: {combates_totales(evento)}")
    print(f" - Cerrador: {combates_cerrados(evento)}")
    print(f" - Pendientes: {combates_pendientes(evento)}")
    print("")
    print("Luchadores inscritos:")
    for i in evento["combates"].values():
        for j in i["luchadores"]:
            print(f" - {j.nombre}")
    print("")
    print("Artistas y canciones:")
    for i in evento["artistas"]:
        print(f" * {i.nombre}")
        for j in i.setlist:
            print(f"    - {j}")
    print("")
    print("Tipos de entradas:")
    for tipo, precio in evento["entradas"]["tipos"].items():
        print(f" - {tipo}: {precio}")
    print("")
    print(f"Entradas vendidas: {evento["entradas"]["vendidas"]}")
    print("")
    print("Staff por área:")
    print(" [Seguridad]")
    for i in evento["staff"]["seguridad"]["miembros"]:
        print(f"    · {i}")
    print(" [Ring]")
    for i in evento["staff"]["ring"]["miembros"]:
        print(f"    · {i}")

def main():
    while True:
        print("=== La Velada - Backstage Manager ===")
        print("1. Vender entradas")
        print("2. Añadir artista")
        print("3. Programar combate")
        print("4. Cerrar combate")
        print("5. Ver informe completo")
        print("6. Salir")

        opcion = int(input("Introduce una opción(1-6): "))
        match opcion:
            case 1:
                print(vender_entradas(evento,"general",2))
            case 2:
                print(agregar_artista(evento,"Duki","Music1","Music2"))
                print(agregar_artista(evento,"Maluma","Music1","Music2"))
            case 3:
                print(programar_combate(evento,"Pelea1","Xokas","Plex",5,"Medio"))
                print(programar_combate(evento,"Pelea2","Mayichi","Aitana",3,"Ligero"))
            case 4:
                print(cerrar_resultado(evento,"Pelea1","Xokas"))
            case 5:
                informe_completo(evento)
            case 6:
                print("Saliendo del programa...")
                break
            case _:
                pass

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
class Luchador(Persona):
    def __init__(self,nombre,peso):
        super().__init__(nombre)
        self.peso = peso

class Artista(Persona):
    def __init__(self, nombre, setlist):
        super().__init__(nombre)
        self.setlist = setlist

        
if __name__ == "__main__":
    main()
