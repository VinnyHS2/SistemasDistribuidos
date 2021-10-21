Compilar e executar:
	Para iniciar o servidor:
	- python3 server.py
	Para iniciar o cliente:
	- python3 client.py

Bibliotecas
  - socket:     Esta biblioteca fornece acesso à interface de socket BSD. Ela foi utilizada para criar a conexão TCP.
  - os:         Esta biblioteca permite o uso de funcionalidades simples que dependem do sistema operacional.
  - threading:  Esta biblioteca constrói interfaces para threading usando o módulo _thread, de mais baixo nível.
  - logging:	Esta biblioteca fornece funções para a criação de um log de maneira simplificada.
Exemplos de uso: 
	Adicionar o arquivo opc.pdf no servidor
  		Após compilar e executar o programa digite no terminal do cliente o comando:
		- ADDFILE opc.pdf
		O terminal do cliente irá exibir a menssagem "SUCCESS" caso ele consiga realizar o upload do arquivo 
		ou exibirá a mensagem "ERROR" caso ele não consiga fazer o upload.
		O arquivo que foi transferido ficará localizado na pasta "arquivosServidor" e o arquivo que você deseja
		tranferir precisa estar na pasta "arquivosCliente"

	Listar os arquivo do servidor utilizando o comando GETFILESLIST
  		Após compilar e executar o programa digite no terminal do cliente o comando:
		- GETFILESLIST
		Após enviar este comando irá ser exibido no terminal do cliente os nome dos arquivos caso ocorra um erro
		será exibido a mensagem "ERROR".