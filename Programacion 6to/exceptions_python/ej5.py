string= "holadoszetafour"

try:
    file1 = open("Lauu\Programacion\PG3_ITSVillada2022\Programacion 6to\exceptions_python\string1.txt", "w") 
    file1.write(string)
    file1.close()
 
    f = open('Original.txt', 'r')
    if f.mode=='r':
        contents= f.read()
except:
    pass