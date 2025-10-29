lugares = ["Tokio","Noruega","Francia","LosAngeles"]

print(f"Ordenada: {sorted(lugares)}")
print(lugares)

print(f"Ordenada inversa: {sorted(lugares, reverse=True)}")
print(lugares)


lugares.reverse()
print(f"Reverse1: {lugares}")

lugares.reverse()
print(f"Reverse2: {lugares}")

lugares.sort()
print(f"Sort1: {lugares}")

lugares.sort(reverse=True)
print(f"Sort1: {lugares}")

