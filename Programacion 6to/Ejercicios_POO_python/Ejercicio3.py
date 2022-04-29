class Triangulo:
 

    def es_equilatero(self):
        if self.lado1==self.lado2 and self.lado2==self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")
            
    def lado_mayor_del_triangulo(self):
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print("El lado mayor del triangulo es:",self.lado1)
        elif self.lado2>self.lado1 and self.lado2>self.lado3:
            print("El lado mayor del triangulo es:",self.lado2)
        else:
            print("El lado mayor del triangulo es:",self.lado3)
        
Triangulo1=Triangulo()
Triangulo1.lado1=int(input("Ingrese el valor del primer lado:"))
Triangulo1.lado2=int(input("Ingrese el valor del segundo lado:"))
Triangulo1.lado3=int(input("Ingrese el valor del tercer lado:"))
Triangulo1.es_equilatero()
Triangulo1.lado_mayor_del_triangulo()

