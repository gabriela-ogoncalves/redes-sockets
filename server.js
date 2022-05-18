const net = require('net');
var ip = require('ip');

const PORT = 9009;
const IP_SERVER = ip.address();

const handleConnection = socket => {
  const clientAddress = `${socket.remoteAddress}:${socket.remotePort}`; 
  console.log(`\nNew client connected: ${clientAddress}\n`);

  socket.on('close', () => {
    console.log(`Connection closed ${clientAddress}`);  
  });

  socket.on('error', (err) => {
    console.log(`Error occurred in ${clientAddress}: ${err.message}`); 
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
