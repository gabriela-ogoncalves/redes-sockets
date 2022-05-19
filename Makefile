setup:
	npm install ip

run_client:
	python3.8 client.py

run_server:
	node server.js

client-py:
	python3.8 client.py

server-py:
	python3.8 additional_connection/server.py

server-js:
	node server.js

client-js:
	node additional_connection/client.js