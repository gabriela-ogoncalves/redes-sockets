const net = require('net');

const PORT = 8080;

const handleConnection = socket => {
	console.log('Alguem se conectou')

  socket.on('end', () => {
    console.log('end')
    socket.write('Desconectado')
  });

  socket.on('data', data => {
    const str = data.toString()

    if(str === 'end') {
      socket.end()
    }

    console.log(str)
    return;
  })
}

const server = net.createServer(handleConnection);
server.listen(PORT, '127.0.0.1', () => {
  console.log(`Server listening for connection requests on socket ${server.address().address}:${PORT}`);
});
