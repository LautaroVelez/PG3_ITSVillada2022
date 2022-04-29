class Persona:

    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre: ",self.nombre)


persona1=Persona()
nombre=input("Ingrese su nombre:")
persona1.inicializar(nombre)


persona2=Persona()
nombre2=input("Ingrese su nombre:")
persona2.inicializar(nombre2)

persona1.imprimir()
persona2.imprimir()