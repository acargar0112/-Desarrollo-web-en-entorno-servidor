num = int(input("Introduce un número entero: "))
cont = 0

for i in range(1,10 + 1):
    resultado = num * i
    cont += 1
    print(f"{num} * {cont} : {resultado}")
    