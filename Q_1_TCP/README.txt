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
  - hashlib:    Esta biblioteca implementa uma interface para diferentes tipo de hash e para o tratamento de mensagens.

Exemplos de uso: 
	Se connectar no servidor 
  		Após compilar e executar o programa digite no terminal do cliente o comando:
		- connect pato 123
		Após enviar este comando o terminal do cliente irá exibir a mensagem "SUCCESS" e irá permitir o uso das
        outras funções caso o usuario ou a senha estejá incorreta o terminal irá exibir a mensagem de "ERROR"
        Caso o usuario não execute este comando ele esterá limita a executar somente os comandos de "connect" e "exit"        

    Exibir o diretório atual do servidor
	    Após compilar e executar o programa digite no terminal do cliente o comando:
		- connect pato 123
        Após se conectar será possivel utilizar os comandos "PWD", "GETFILES", "GETDIRS" e "CHDIR" 
        Para exibir o diretório atual será utilizado o comando:
        - pwd
        Após enviar este comando será exibido no terminal do cliente o diretório atual
        Caso sejá enviado o comando pwd ante de realizar o connect não será exibido nada.