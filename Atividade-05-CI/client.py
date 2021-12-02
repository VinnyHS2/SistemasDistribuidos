### Comunicação Indireta ###
# Autores: Henrique e Vinicius
# Data de criação: 02/12/21
# Data de modificação: 02/12/21
# Cria filas com as palavras: impeachment, bolsonaro e lula. 
import pika
import sys

def main():
    # Conexão com o servidor RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    # Criação do canal
    channel = connection.channel()

    # Declaração da fila para troca
    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Lista de topicos que podem ser criados
    filas = ["bolsonaro", "lula", "ladrão", "preso"]
    topicos = sys.argv[1:]

    # Verifica se o tópico existe
    if not topicos:
        print(
            "Cadastre-se em um dos topicos a seguir: [preso] [ladrão] [bolsonaro] [lula]", end="")
        sys.exit(1)

    for i in range(len(topicos)):
        if topicos[i] not in filas:
            print(
                "Cadastre-se em um dos topicos a seguir: [preso] [ladrão] [bolsonaro] [lula]", end="")
            sys.exit(1)

    # Cria a fila do topico
    for topico in topicos:
        channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=topico)

    print(' [*] Aguardando logs. Para sair pressione CTRL+C')

    # Exibe o retorno
    def callback(ch, method, properties, body):
        data = body.decode()
        print("Tópico: %r" % (method.routing_key))
        print(data)
        print("------------------------------------------------------")


    # Define a função de consumo de mensagens para a fila 'tweets'
    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    # Inicia o consumo de mensagens
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Encerrado")
