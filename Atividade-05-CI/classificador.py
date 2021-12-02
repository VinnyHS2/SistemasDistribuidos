### Comunicação Indireta ###
# Autores: Henrique e Vinicius
# Data de criação: 02/12/21
# Data de modificação: 02/12/21
# O classificador irá obter os tweets utilizando as palavras: impeachment, 
# bolsonaro e lula. Envia para as filas que requisitaram.

import pika

def main():
    # Conexão com o servidor RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    # Criação do canal
    channel = connection.channel()

    # Declaração da fila
    channel.queue_declare(queue='tweets')

    # Função para o consumo de mensagens
    def callback(ch, method, properties, body):
            key = []
            # Faz a decodificação do tweet
            data = body.decode()
            # Verifica se o tweet contém alguma das palavras-chave e adiciona ao vetor 'key'
            if 'bolsonaro' in data.lower():
                key.append('bolsonaro')
            if 'ladrão' in data.lower():
                key.append('ladrão')
            if 'lula' in data.lower():
                key.append('lula')
            if 'preso' in data.lower():
                key.append('preso')
            channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
            # Envia para a fila de tópico correspondente ao tweet
            for chave in key:
                channel.basic_publish(exchange='direct_logs', routing_key=str(chave), body=data)
    
    # Define a função de consumo de mensagens para a fila 'tweets'
    channel.basic_consume(queue='tweets', on_message_callback=callback, auto_ack=True)
    # Inicia o consumo de mensagens
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Encerrado")