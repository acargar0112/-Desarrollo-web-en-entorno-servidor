class Empleado:
    salario_medio = []
    dni_unico = set()

    def __init__(self,nombre,salario,dni):
        if dni in Empleado.dni_unico:
            print(f"El dni {dni} ya esta registrado.")

        self.__nombre = nombre
        self.__salario = salario
        self.__dni = dni

        Empleado.salario_medio.append(salario)
        Empleado.dni_unico.add(dni)
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario
    
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni
    
    def detalles(self):
        return f"\nDETALLES EMPLEADO/GERENTE\n{"-" * (17)}\nNombre: {self.__nombre}\nSalario: {self.__salario}\nDNI: {self.__dni}"
    
    @classmethod
    def calcular_salario_medio(cls):
        return f"Salario medio: {cls.salario_medio}"
    
    def __del__(self):
        print(f"El objeto con nombre {self.nombre} ha sido eliminado.")
    
class Gerente(Empleado):

    def __init__(self, nombre, salario, dni, departamento):
        super().__init__(nombre, salario, dni)
        self.__departamento = departamento
    
    def detalles(self):
        print(f"{super().detalles()}\nDepartamento: {self.__departamento}\n")
    
    def descuesto_sueldo(self):
        descuesto = self.salario * 0.90
        self.salario = descuesto
        return self.salario

    @staticmethod
    def impuesto(salario):
        salario *= 0.21
        return salario

empleado1_empleado = Empleado("Pepe",1000,31313131)
empleado2_empleado = Empleado("Juan",1500,32323232)

empleado1_gerente = Gerente("Pepe",1000,31313131,"Informática")
empleado2_gerente = Gerente("Juan",1500,32323232,"Desarrollo")

print(empleado1_empleado.detalles())
print(empleado2_empleado.detalles())

empleado1_gerente.detalles()
empleado2_gerente.detalles()
""" print(empleado1.descuesto_sueldo())
print(Gerente.impuesto(10)) """



    