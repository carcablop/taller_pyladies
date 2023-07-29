import socket
import threading


HOST= '127.0.0.1'
PORT= 65123

usuario= input('Escriba un nombre de usuario asi:(@nombre_usuario): ')

socket_cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_cliente.connect((HOST,PORT))

socket_cliente.sendall(usuario.encode('utf-8'))


def recibir_mensajes():
    while True:
        try:
            data=socket_cliente.recv(1024).decode('utf-8')
            print(data)
        except:
            socket_cliente.close()
            break


def enviar_mensajes():
    try:
        while True:
            mensaje = f'{usuario}: {input()}'
            socket_cliente.send(mensaje.encode('utf-8'))
    except KeyboardInterrupt as e:
        print('cliente desconectado')
        socket_cliente.close()

thread_enviar= threading.Thread(target=enviar_mensajes)
thread_enviar.start()
thread_enviar= threading.Thread(target=recibir_mensajes)
thread_enviar.start()
