import pymysql

#--------------------Variables para Python---------------------#
DATA = [] # variable que recibe y envia datos al servidor
Comando = 'SELECT * FROM `primeraetapa`' # variable comando con varios valores (entrada y salida)

#--------------------Clases---------------------#
Conector = pymysql.connect( # clase connect para ingresar el servidor
    host="127.0.0.1", # ip del servidor al que se debe conectar
    port=3306, # puerto en el cual esta nuestro servidor sql
    user='root', # este es el usuario desde el que se accedera, con los correspondientes privilegios
    password='', # en caso de tener contraseña va aqui
    db='genesis' # aqui va el nombre de la base de datos
)

# print('Conexion establecida!!!!') # bandera para saber si ya esta conectado

Cursor = Conector.cursor() # clase cursor para mandar las peticiones al servidor

Cursor.execute(Comando) # funcion exectue para pedir al servidor


#--------------------Almacenamiento---------------------#
DATA.append(Cursor.fetchall()) # en la variable local DATA se almacena la informacion recibida del servidor

#--------------------Funcion---------------------#
def Datos_Consola (): # defino una funcion para poder gestionar los datos desde otro archivo
    for i in DATA:
        for j in i:
            yield from j # retorno un yield con la informacion contenida


#--------------------Test en consola---------------------#
Imprimir = Datos_Consola() # para probar la funcion le doy el objeto yield a Imprimir
for i in Imprimir:
    print(i) # lo itero para imprimirlo en consola


#--------------------HammerTime---------------------#
Cursor.close() # se detienen las clases utilizadas
Conector.close()
