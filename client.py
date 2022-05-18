#!/usr/bin/python3
import json
import socket
import time

IP_SERVER = input('Digite o IP do servidor: ')
PORT = 9009
DESTINO = (IP_SERVER, PORT)

def current_time():
    return round(time.time() * 1000)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = INET (exemplo IPv4)
# socket.SOCK_STREAM = usaremos TCP

tcp.connect(DESTINO) # inicia a conexao TCP

start = current_time()
while 1:
  mensagem = input('Mensagem a ser enviada: ').strip() # mensagem recebera dados do teclado
  data = {}

  if mensagem.isdigit():
    data["tipo"] = "int"
    data["val"] = int(mensagem)
  elif len(mensagem) == 1:
    data["tipo"] = "char"
    data["val"] = mensagem
  else:
    data["tipo"] = "string"
    data["val"] = mensagem

  start = current_time()

  tcp.send(json.dumps(data).encode('utf-8')) # enviar a mensagem para o destino da conexao
  data = tcp.recv(1024).decode('utf-8')

  end = current_time()
  print("Devolvido: ", data)
  print("RTT: ", end - start)

data = tcp.recv(1024).decode('utf-8') #recebe do servidor - máx. 1024 bytes
print(data)

tcp.close()
