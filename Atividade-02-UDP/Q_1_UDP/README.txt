Compilar e executar:
	Para iniciar o cliente 1:
	- python3 client.py 1
	Para iniciar o cliente 2:
	- python3 client.py 2

Bibliotecas
  - socket:     Esta biblioteca fornece acesso à interface de socket BSD. Ela foi utilizada para criar a conexão TCP.
  - os:         Esta biblioteca permite o uso de funcionalidades simples que dependem do sistema operacional.
  - threading:  Esta biblioteca constrói interfaces para threading usando o módulo _thread, de mais baixo nível.
  - logging:	Esta biblioteca fornece funções para a criação de um log de maneira simplificada.
  - hashlib:    Esta biblioteca implementa uma interface para diferentes tipo de hash e para o tratamento de mensagens.

Exemplos de uso: 
    Para executar o programa, primeiro é necessário executar em terminais distintos o client 1 e o client 2:
        > No terminal do client 1
            - Insira o apelido "Vinny"
        > No terminal do client 2
            - Insira o apelido "Bit"
            - Envie a mensagem "Tem alguém ai? :duck:"
        > No terminal do client 1
            - A mensagem será recebida e exibida da seguinte forma:
                ~ "Bit said: Tem alguém ai? 🦆"
            - Envie de volta a mensagem "https://www.google.com/"
        > No terminal do client 2
            - A mensagem será recebida e exibida da seguinte forma:
                ~ "Vinny has sent a link: https://www.google.com/