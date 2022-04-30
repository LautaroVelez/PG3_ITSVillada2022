class Persona:
    def persona(self):
        self.nom=str(input("Ingrese su nombre:"))
        self.edad=int(input("Ingrese su edad:"))

    def imprimir(self):
        print("Nombre:",self.nom)
        print("Edad:",self.edad)
    
class Empleado(Persona):
    def empleado(self):
        super().persona()
        self.salario=int(input("Ingrese su salario:"))

    def imprimir(self):
        super().imprimir()
        print("Salario:",self.salario)

    def pagar_impuestos(self):
        if self.salario>=3000:
            print("El empleado debe pagar impuestos")
        else:
            print("El empleado no debe pagar impuestos")


persona1=Empleado()
persona1.empleado()
persona1.imprimir()
persona1.pagar_impuestos()

