class Familia:
    def familia(self, padre, madre, hijos):
        self.padre= padre
        self.madre= madre
        self.hijos= hijos

    def __str__(self):
        return "Padre:"+self.padre+"\nMadre:"+self.madre+"\nHijos:"+format(self.hijos)

familia1=Familia()
familia1.familia("Flavio","Karina",["Lauti","Mica"])
print(familia1.__str__())

        



