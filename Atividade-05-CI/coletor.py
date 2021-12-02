### Comunicação Indireta ###
# Autores: Henrique e Vinicius
# Data de criação: 02/12/21
# Data de modificação: 02/12/21
# O coletor obtem os tweets do dataset direita_filtro2.csv e adicionados em 
# uma fila, para o que o classificador insira na fila específica dos tópicos
import pika
import tweepy

def main():
    with open('tokens.txt', 'r') as f:
        tokens = f.read().splitlines()
    auth = tweepy.OAuthHandler(tokens[0], tokens[1])
    auth.set_access_token(tokens[2], tokens[3])
    api = tweepy.API(auth)
    public_tweets = api.search_tweets(q='politica lula bolsonaro',result_type='mixed',count=100)

    # Conexão com o servidor RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    # Criação do canal
    channel = connection.channel()
    # Percorre todos os tweets
    for tweet in public_tweets:
        # Armazena o nome do usuário que fez o tweet
        user = "Usuário: " + tweet.user.name
        # Armazena o conteúdo do tweet
        twt = "Tweet: " + tweet.text
        dadoUserTweet = user + "\n" + twt + "\n"
        # Troca as mensagens recebidas de callback da fila tweet
        channel.exchange_declare(exchange='tweets', exchange_type='direct')
        # Envia o que recebido da fila de tweets
        channel.basic_publish(exchange='', routing_key='tweets', body= dadoUserTweet)


    # Fecha a conexão
    connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Encerrado")