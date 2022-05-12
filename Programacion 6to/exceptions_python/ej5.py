string= str(input("Ingrese una cadena: "))

try:
    esono = any(chr.isdigit() for chr in string)
    if esono == True:
        print("No ponga numeros porfas")
        
    elif esono== False:
        file1 = open(".\PG3_ITSVillada2022\Programacion 6to\exceptions_python\string1.txt", "w") 
        file1.write(string)
        file1.close()

        f = open('Original.txt', 'r')

        if f.mode=='r':
            contents= f.read() 
    
except:
    pass