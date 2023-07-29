import socket
import threading

clientes=[]
usuarios=[]

def enviar_todos(mensaje, cliente):
    for cl in clientes:
        if cl !=cliente:
            cl.send(mensaje.encode('utf-8'))

def recibir_mensajes(cliente, direccion):
    while True:
        try:
            mensaje= cliente.recv(1024).decode('utf-8')
            if not mensaje:
                break
            print(f'mensaje recibido: {mensaje}')
            enviar_todos(mensaje,cliente)
        except:
            indice= cliente[cliente]
            user=usuarios[indice]
            enviar_todos(f'El{user} se desconecto' .encode('utf-8'))
            clientes.remove(cliente)
            usuarios.remove(user)
            cliente.close()
            break
        

#funcion principal que se encargara de aceptar las conexiones de los clientes
def run():
    HOST= "172.20.34.129"
    PORT = 65123 

    socket_server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_server.bind((HOST,PORT))
    socket_server.listen()
    print('Servidor iniciado')
    try:
        while True:
            conexion_cliente, direccion_cliente=socket_server.accept()
            print(f"usuario conectado desde {direccion_cliente[0], direccion_cliente[1]}")
            conexion_cliente.send('conectado al servidor'.encode('utf-8'))
            #agregarlos a la lista el cliente conectado:
            clientes.append(conexion_cliente)

            #recibe el username
            n_usuario= conexion_cliente.recv(1024).decode('utf-8')
            usuarios.append(n_usuario)

            #mensaje de difusion a todos los clientes que se conecto un cliente nuevo:
            mensaje_difusion= f'ChatBot: usuario {n_usuario} desde {direccion_cliente[0]} se ha unio al chat'
            enviar_todos(mensaje_difusion,conexion_cliente)

            #crear un subproceso por cad aclienteque se cliente:
            thread= threading.Thread(target=recibir_mensajes, args=(conexion_cliente,direccion_cliente))
            thread.start()
    except KeyboardInterrupt as e:
        print("Servidor desconectado")
        socket_server.close()
run()
