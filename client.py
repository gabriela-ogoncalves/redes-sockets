#!/usr/bin/python3
import socket

IP_SERVER = '127.0.0.1'
PORT = 8080
DESTINO = (IP_SERVER, PORT)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = INET (exemplo IPv4)
# socket.SOCK_STREAM = usaremos TCP

tcp.connect(DESTINO) # inicia a conexao TCP

while 1:
  mensagem = input('Mensagem a ser enviada: ') # mensagem recebera dados do teclado
  tcp.send(bytes(mensagem, "utf8"))
  # enviar a mensagem para o destino da conexao (IP + porta)
  # bytes(mensagem,"utf8") = converte tipo str para byte

#recebe do servidor - máx. 1024 bytes
data = tcp.recv(1024).decode('utf-8')
print(data)

tcp.close()
