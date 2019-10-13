"""
UN SOCKET ESTA COMPUESTO POR DOS PARTES:
    -UNA DIRECCION IP(Si utilizamos la familia de protocolos TCP/IP [(Transmission Control Protocol), Protocolo de Control de Transmisión)
    -UN PUERTO(Este identifica un programa entre todos los que se conectan a Internet o comparten recursos)
 """

#SOCK_STREAM: Este protocolo nos da una comunicación fiable de dos direcciones en un flujo de datos(TCP)
#SOCK_DGRAM: Este protocolo nos da una conexión no fiable. (UDP)
#SOCK_RAW: este protocolo es para acceder a los campos e interfaces internos de la red.
#SOCK_RDM: Este protocolo garantiza la llegada de paquetes pero no garantiza el orden de llegada
#SOCK_SEQPACKET: datagramas fiables y secundarios, de longitud fija, basado en la conexión.
#SOCK_PACKET: Coloca el socket en modo promiscuo en la que recibe todos los paquetes de la red.

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Creamos un objeto que haga la funcion de un socket
s.bind(("127.0.0.1", 9999))#Asignamos la direccion IP y el puerto del socket
s.listen(5)#Asignamos el numero limite de clientes que puede haber conectados
 
print ("Servidor Vergas\n")
 
while True:#Inicia el ciclo para la entrada y salida de datos
        print ("Esperando a un puto cliente...")#Un simple mensaje formal del servidor
        sc, addr = s.accept()#Agregamos el metodo accept() para aceptar la solicitud del cliente
        print ("IP del cliente: ", addr)#Imprime de donde esta conectado el cliente
 
        while True:#Cuando la peticion del cliente sea aceptada...
                recibido = sc.recv(1024)#Recibe datos por parte del cliente
                if recibido == "salir":#Si el mensaje que envia el cliente es salir entoces terminara la conexion
                        break#Rompe el ciclo
                print ("Mensaje del cliente: ", recibido)#Imprime el mensaje del cliente
 
                nuestra_respuesta = "Hola pinche cliente feo"#Mensaje formal que sera enviado por parte del servidor
                sc.send(nuestra_respuesta.encode('utf-8'))#Agregamos esto porque no queremos que se cague si escribes un acento en el mensaje
 
print ("Adios Culero")#Se despide del cliente formalmente
sc.close()#Cierra la conexion del cliente
s.close()#Cierra el socket