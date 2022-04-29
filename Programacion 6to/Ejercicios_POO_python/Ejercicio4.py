class Operaciones:

    def __init__(self):
        self.num1=int(input("Ingrese el primer numero:"))
        self.num2=int(input("Ingrese el segundo numero:"))
        self.calculo()
        

    def calculo(self):
        sum=self.num1+self.num2
        resta=self.num1-self.num2
        div=self.num1/self.num2
        mul=self.num1*self.num2
        print("La suma es:",sum)
        print("La resta es:",resta)
        print("La division es:",div)
        print("La multiplicacion es:",mul)

operacion1=Operaciones()
