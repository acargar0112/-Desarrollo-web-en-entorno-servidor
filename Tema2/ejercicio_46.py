set_1 = {1,2,3,4}
set_2 = {3,4,5,6}

print(set_1 | set_2)

print(set_1.intersection(set_2))

print(f"El set 1 tiene los siguientes números diferentes: {set_1.difference(set_2)} y el set 2 tiene {set_2.difference(set_1)}")