
#importo la libreria ftp

from ftplib import FTP



#datos de conexion de prueba a un server

host = 'ftp.iconovirtual.net'
user = 'u373631942.backup'
password = 'lucheTTi-01'

#me conecto

try:
    #conexion
    ftp = FTP(host,user,password)
    print("CONEXION ESTABLECIDA")
    print("nos encontramos en la carpeta: "+ftp.pwd() +'\n' )
    ftp.retrbinary("RETR wp-admin",open("wp-admin", "wb").write)
    ftp.quit()

except Exception as e:
    print("conexion errada " +str(e))