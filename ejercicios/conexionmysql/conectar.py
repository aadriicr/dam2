print("Resultados de mysql.connector:")
import mysql.connector
miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='admin', db='sys' )
cur = miConexion.cursor()
cur.execute( "SELECT idclientes, nombre, ciudad FROM sys.clientes" )
for idclientes, nombre, ciudad in cur.fetchall() :
    print (idclientes, nombre, ciudad)
miConexion.close()