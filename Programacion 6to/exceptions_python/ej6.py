import pymysql

while True:
    connection = pymysql.connect(host='127.0.0.1', user='lauti', password='pepe1234', db='Exceptions', database="Ej1")
    cursor=connection.cursor()
    code = input("Introduce la accion que desea realizar: ")
    try:
        cursor.execute(code)
    except pymysql.err.ProgrammingError as e:
        print("Ha ocurrido un error: ", e)
    except pymysql.err.IntegrityError as a:
        print("Ha ocurrido un error: ", a)
    except pymysql.err.DataError as b:
        print("Ha ocurrido un error: ", b)
    except pymysql.err.InternalError as c:
        print("Ha ocurrido un error: ", c)
    except pymysql.err.NotSupportedError as d:
        print("Ha ocurrido un error: ", d)
    except pymysql.err.OperationalError as f:
        print("Ha ocurrido un error: ", f)
