Compilar e executar:
    Para compilar o servidor 
    - javac --class-path .:protobuf-java-3.19.1.jar *.java
	Para iniciar o servidor:
	- java --class-path ".:protobuf-java-3.19.1.jar: .:sqlite-jdbc-3.27.2.1.jar" servidor
	Para iniciar o cliente:
	- python3 cliente.py

Bibliotecas python
  - socket:   Esta biblioteca fornece acesso à interface de socket BSD. Ela foi utilizada para criar a conexão TCP.
Bibliotecas Java
  - java.io:  Esta biblioteca permite o uso de funções para a realização de entrada e saída
  - java.net: Esta biblioteca permite o uso de funções para a realização de conexões TCP
  - java.sql: Esta biblioteca permite o uso de funções para a realização de conexões com o banco de dados SQLite

Exemplos de uso: 
	Listar todos as diciplinas de um curso
  		Após compilar e executar o programa digite no terminal do cliente:
		- Digite 4 para selecionar a opção de listagem de disciplinas de um curso em seguida digite o código do curso:
		O terminal do cliente irá exibir a todas as disciplinas de um curso, caso ocorra algum erro ele irá exibir uma
        mensagem detalhando o erro.

	Listar os arquivo do servidor utilizando o comando GETFILESLIST
  		Após compilar e executar o programa digite no terminal do cliente o comando:
		- GETFILESLIST
		Após enviar este comando irá ser exibido no terminal do cliente os nome dos arquivos caso ocorra um erro
		será exibido a mensagem "ERROR".