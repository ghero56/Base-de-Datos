import pymysql

DATA = [] # variable que recibe y envia datos al servidor
Comando = '' # variable comando con varios valores (entrada y salida)



Conector = pymysql.connect( # clase connect para ingresar el servidor
    host="127.0.0.1",
    port=3306,
    user='root',
    password='',
    db='genesis'
)

print('Conexion establecida!!!!')

Cursor = Conector.cursor()

Cursor.execute(Comando)

DATA.append(Cursor.fetchall())

def Datos_Consola ():
    for i in DATA:
        for j in i:
            yield from j

Imprimir = Datos_Consola()
for i in Imprimir:
    print(i)

Cursor.close()
Conector.close()
