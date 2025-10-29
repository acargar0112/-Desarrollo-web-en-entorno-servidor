lista_1 = [3,5,2,6,4]
lista_2 = [6,2,7,3,6]

lista_zip = []

for num_1, num_2 in zip(lista_1,lista_2):
    resultado = num_1 * num_2
    lista_zip.append(resultado)

print(lista_zip)