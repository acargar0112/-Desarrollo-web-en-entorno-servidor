n_impares = []

for i in range(100):
    if len(n_impares) < 20:
        if i % 2 != 0:
            n_impares.append(i)

print(n_impares)