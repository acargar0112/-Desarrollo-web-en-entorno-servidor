class Empleado:
    salario_medio = []
    dnis_registrados = set()

    def __init__(self, nombre, salario, dni):
        if dni in Empleado.dnis_registrados:
            raise ValueError(f"El DNI '{dni}' ya está registrado para otro empleado.")
        
        self.__nombre = nombre
        self.__salario = salario
        self.__dni = dni

        Empleado.salario_medio.append(salario)
        Empleado.dnis_registrados.add(dni)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def salario(self):
        return self.__salario

    @property
    def dni(self):
        return self.__dni

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @dni.setter
    def dni(self, dni):
        if dni in Empleado.dnis_registrados:
            raise ValueError(f"El DNI '{dni}' ya pertenece a otro empleado.")
        Empleado.dnis_registrados.discard(self.__dni)
        self.__dni = dni
        Empleado.dnis_registrados.add(dni)

 
    def detalles(self):
        print(f"Nombre: {self.__nombre}\n Salario: {self.__salario}\n DNI: {self.__dni}")

    @classmethod
    def calcular_salario_promedio(cls):
        if not cls.salario_medio:
            return 0
        return sum(cls.salario_medio) / len(cls.salario_medio)

    def __del__(self):
        print(f"El empleado con DNI {self.__dni} ha sido eliminado.")
        try:
            Empleado.salario_medio.remove(self.__salario)
            Empleado.dnis_registrados.discard(self.__dni)
        except ValueError:
            pass


class Gerente(Empleado):
    def __init__(self, nombre, salario, dni, departamento):
        super().__init__(nombre, salario, dni)
        self.__departamento = departamento

    def detalles(self):
        super().detalles()
        print(f"Departamento: {self.__departamento}")

    def descuento_sueldo(self):
        nuevo_salario = self.salario * 0.9
        self.salario = nuevo_salario
        return self.salario

    @staticmethod
    def impuesto(salario):
        return salario * 0.21


if __name__ == "__main__":
    emp1 = Gerente("Pepe", 3000, "123A", "Ventas")
    emp1.detalles()
    print(f"Salario con descuento: {emp1.descuento_sueldo()}")
    print(f"Impuesto sobre 3000: {Gerente.impuesto(3000)}")

    emp2 = Empleado("Ana", 2500, "456B")
    emp3 = Empleado("Luis", 2800, "789C")

    print(f"\nSalario promedio: {Empleado.calcular_salario_promedio():.2f}")
