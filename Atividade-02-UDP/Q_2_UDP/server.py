'''
    # Questão 2 - UDP Servidor #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 24/10/2021
    # Data de modificação: 24/10/2021
    # Descrição:
    #   O servidor recebe um arquivo do cliente e verifica se o checksum é igual ao checksum local.
    #   Caso não seja, o arquivo é deletado e uma mensagem de erro é enviada para o cliente.


    # cabeçalho requisição:
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |               TamanhoDoArquivo: 4 byte                |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |               Nome Do Arquivo: 1020 bytes             |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    - Para cada quantidade de envio:
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |               Arquivo em bytes: 1024 bytes            |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    - No ultimo envio é enviado o checksum do arquivo
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                   checksum: 20 bytes                  |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''

import hashlib
import logging
import math
import os
import socket

ip = "127.0.0.1"
port = 5973

#Variavel contendo o ip e a porta
addr = (ip, port)
#Cria um socket do tipo TCP os parametros AF_INET e SOCK_DGRAM definem
#qual a familia de endereços será utilizada e qual o tipo de socket
socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Permite o reuso de endereços ips
socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  
#Realiza a conexão do socket utilizando o ip e a porta definidos anteriormente
socketServer.bind(addr)

FORMAT = '%(asctime)-1s %(clientip)s %(user)s %(message)s'
# Define o log para info
logging.basicConfig(format=FORMAT,level=20)
# Define o nome do log
logger = logging.getLogger('tcpserver')

def main():
    while True:
        #Recebe a mensagem do cliente
        request, addr = socketServer.recvfrom(1024)
        # Defini o ip do cliente e a porta que aparece na mensagem de log
        d = {'clientip': addr[0], 'user': addr[1]}
        # Atribui o tamanho do arquivo a variável
        fileSize = int.from_bytes(request[:4],'big')
        # Atribui o nome do arquivo a variável
        fileName = request[4:].decode()
        # Define o numero de pacotes que serão recebidos
        numberOfPackets = math.ceil(fileSize/1024)
        # Log
        logger.info('Protocol info: %s', 'Download started', extra=d)
        # Cria um arquivo com o nome do arquivo recebido
        file = open('./arquivosServidor/' + fileName, 'w+b')
        while numberOfPackets > 0:
            #Recebe o pacote
            data, addr = socketServer.recvfrom(1024)
            # Escreve o pacote no arquivo
            # print(numberOfPackets)
            file.write(data)
            # Decrementa o número de pacotes
            numberOfPackets -= 1
        
        # Volta para o inicio do arquivo
        file.seek(0)
        # Cria um checksum do arquivo com base no bytes recebidos
        checksumLocal = hashlib.sha1(file.read()).hexdigest()
        # Recebe o checksum do arquivo do cliente
        checksumClient, addr = socketServer.recvfrom(1024)
        print(checksumClient.__sizeof__())
        checksumClient = checksumClient.decode()
        # Verifica se o checksum recebido é igual ao checksum local
        if checksumClient == checksumLocal:
            # Log
            logger.info('Protocol info: %s', 'Download finished successfully', extra=d)
            # Fecha o arquivo
            file.close()
        # Caso não seja igual, envia uma mensagem de erro e deleta o arquivo
        else:
            # Deleta o arquivo
            os.remove('./arquivosServidor/' + fileName)
            # Log
            logger.info('Protocol info: %s', 'Download finished with error', extra=d)
            # Fecha o arquivo
            file.close()
            
    

main()
