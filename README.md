# Trabalho de Redes - Sockets

![node](https://img.shields.io/badge/node-10.16.2-blue "Node 10.16.2")

## Sobre o projeto

O objetivo desse trabalho é construir um programa, utilizando sockets, que contenha servidor, cliente e um tipo de protocolo. 

## Definições

| Cliente   |  Servidor | Protocolo  |
| :-------: | :-------: | :--------: |
|  Python   |  NodeJS   |    TCP     |


São funções do **cliente**:
- Usuário pode selecionar se vai transmitir um inteiro, um caractere ou uma cadeia de
caracteres (string);
- Ao receber a resposta, irá exibir;
- O cliente tem que cronometrar o RTT.

São funções do **servidor**:
- Se receber um inteiro, incrementa o valor e devolve;
- Se receber um caractere, inverte a “caixa” e devolve;
- Se for uma string, inverte e devolve.

O conjunto **TCP** pode, ou não responder em um processo ou thread separado.

```
{
  "tipo": "int" | "char" | "string", 
  "val": 37 | 'm' | "uma frase"
}
```

## Rodando o projeto

Para rodar o servidor, abra o seu terminal e digite o comando:

```shell
make run_server
```

Para rodar o cliente, abra uma outra janela do terminal e digite o comando:

```shell
make run_client
```

Para testar, temos implementada uma base de servidor e cliente em python e em nodejs. Para rodar, digite o comando:

`make server-py` ou `make server-js`

e para o cliente, utilize:

`make client-py` ou `make client-js`
