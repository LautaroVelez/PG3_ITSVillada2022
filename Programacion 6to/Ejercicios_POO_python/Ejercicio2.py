class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_nota(self):
        if self.nota<=6:
            print("El alumno esta desaprobado")
        else:
            print("El alumno esta regular")

nota=int(input("Ingrese la nota del alumno:"))
nombre=input("Ingrese el nombre del alumno:")
alumno1=Alumno()
alumno1.inicializar(nombre,nota)
alumno1.imprimir()
alumno1.mostrar_nota()
