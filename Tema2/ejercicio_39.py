cadena = str(input("Introduce una cadena de texto: ")).upper()

cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0

for i in cadena:
    match i:
        case "A":
            cont_a += 1
        case "E":
            cont_e += 1
        case "I":
            cont_i += 1
        case "O":
            cont_o += 1
        case "U":
            cont_u += 1

print(f"A: {cont_a}\nE: {cont_e}\nI: {cont_i}\nO: {cont_o}\nU: {cont_u}")