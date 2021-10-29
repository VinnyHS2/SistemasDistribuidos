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
  - tkinter:    Esta biblioteca fornece uma interface padrão para o Tcl/Tk GUI toolkit, foi utilizada para realizar busca de arquivos.
  - PyQt5:      Esta biblioteca fornece funções para facilitar a implementação de interfaces no python

Exemplos de uso: 
	Adicionar o arquivo opc.pdf no servidor
  		Após compilar e executar o programa irá aparecer uma interface para o client:
         - Nesta interface o usuario devera clicar no botão de busca e selecionar um arquivo de texto ou binário (ex: imagens, pdf)
        Em seguida o usuario deve clicar no botão de enviar, após clicar no botão a barra de progresso começará a carregar. Ao chegar em 100%
        significa que o arquivo foi enviado completamente.