const net = require('net');

const PORT = 8080;
const IP_SERVER = '127.0.0.1';

const handleConnection = socket => {
  console.log('Alguem se conectou');

  socket.on('close', () => {
    console.log('Connection closed');  
  });

  socket.on('error', (err) => {
    console.error(`Connection error: ${err.message}`)
  });

  socket.on('data', data => {
    if (!data) return;
    
    console.log(`Recebido: ${data}`)
  
    const obj = JSON.parse(data);
    const response = {}
    response.tipo = obj.tipo;

    if (obj.tipo === 'int') {
      response.val = obj.val + 1;
    } else if (obj.tipo === 'char') {
      response.val = obj.val == obj.val.toUpperCase() 
        ? obj.val.toLowerCase()
        : obj.val.toUpperCase()
    }
    else if (obj.tipo === 'string') {
      response.val = [...obj.val].reverse().join("");
    } else return;

    socket.write(JSON.stringify(response));
    return;
  })
}

const server = net.createServer(handleConnection);
server.listen(PORT, IP_SERVER, () => {
  console.log(
    `Server listening for connection requests on socket ${server.address().address}:${server.address().port}`
  );
});
