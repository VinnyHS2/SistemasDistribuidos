Como executar:
    Para que seja possível executar essa aplicação é necessário instalar primeiramento o RabbitMQ.
    Abaixo está o link para instalação do RabbitMQ:
        - link: https://www.rabbitmq.com/ 

1. Executar o client.py passando como parâmetro os tópicos:
    - python client.py lula preso bolsonaro ladrão

2. Executar o classificador:
    - python classificador.py

3. Executar o coletor:
    - python coletor.py

Bibliotecas:   
    tweepy: Implementa uma interface para acessar o Twitter.
    pika: Implementa o protocolo AMQP 0-9-1, tentando permanecer bastante independente da biblioteca de suporte à rede subjacente.

Exemplos de uso: 
    Existem 4 possíveis fila que o cliente podem se inscrever:
        - bolsonaro
        - ladrão
        - lula
        - preso

    Ambos são temas relacionados a política.
    
	Exemplo de uso 1: Se inscrever na fila "bolsonaro" e "lula":

    Em um terminal inicie o client, passando como parâmetro as filas que deseja se inscrever:
        - python client.py bolsonaro lula

	Em um outro terminal, execute o classificador:
        - python classificador.py
	
	E por fim, em um último terminal, execute o coletor:
        - python coletor.py

    Todos estarão executando ao mesmo tempo.

	Agora, no console do client irá aparecer os tweets realcionados com os tópicos da fila,
        indicando de qual fila ele foi consumido, os usuário que realizou o tweet e o tweet em sí.
    A seguir está um exemplo de saída recebida pelo client:

        Tópico: 'bolsonaro'
        Usuário: 🔰Eliana DiCarvalho☘️
        Tweet: Esse homem é o próprio diabo😈.   Bolsonaro comemorou quando Lula foi solto, diz Moro https://t.co/vOZxZhUNpa
