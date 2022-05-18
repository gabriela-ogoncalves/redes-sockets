#!/usr/bin/python3
import json
import socket
import time

IP_SERVER = input('Digite o IP do servidor: ')
PORT = int(input('Digite a porta: '))
DESTINO = (IP_SERVER, PORT)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = INET (exemplo IPv4)
# socket.SOCK_STREAM = usaremos TCP

tcp.connect(DESTINO) # inicia a conexao TCP

while 1:
  mensagem = input('\nMensagem a ser enviada: ').strip() # mensagem recebera dados do teclado
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

  start = time.time_ns()

  tcp.send(json.dumps(data).encode('utf-8')) # enviar a mensagem para o destino da conexao
  data = tcp.recv(1024).decode('utf-8')
  end = time.time_ns()

  print("Devolvido:", json.loads(data))
  print('RTT: {}ns'.format(end-start))

tcp.close()
