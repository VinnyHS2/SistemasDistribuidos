'''
    # Questão 1 - TCP Servidor #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 17/10/2021
    # Data de modificação: 19/10/2021
    # Descrição:
        Faz o processamento de mensagens recebidas do cliente, nas quais atualmente são possiveis as seguintes operações:
        - ADDFILE: adiciona um arquivo novo.
        - DELETE: remove um arquivo existente.
        - GETFILESLIST: retorna uma lista com o nome dos arquivos.
        - GETFILE: faz download de um arquivo.


'''
import logging
import threading
import socket
import os

host = ""
port = 5973
addr = (host, port)

# Cria o socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Define as opções do socket
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Define qual o ip da instancia do socket
serverSocket.bind(addr)
# Formato do log
FORMAT = '%(asctime)-1s %(clientip)s %(user)s %(message)s'
# Define o log para info
logging.basicConfig(format=FORMAT,level=20)
# Define o nome do log
logger = logging.getLogger('tcpserver')


def threadConnection(ip, port, connection):
    d = {'clientip': ip, 'user': port}
    while True:
        header = bytearray(3)
        # Define o tipo de resposta
        header[0] = 2
        # Recebe a mensagem
        msg = bytearray(connection.recv(1024))
        # Obtem o tipo de mensagem recebido
        messageType = int(msg[0])
        # Obtem o ID do comando enviado
        commandId = int(msg[1])
        # Obtem o tamanho do arquivo
        fileNameSize = int(msg[2])
        # Decodifica o nome do Arquivo
        fileName = msg[3:].decode('utf-8')
        
        # Adiciona um novo arquivo
        if(commandId == 1):
            # Log
            logger.info('Protocol info: %s', 'Received ADDFILE request', extra=d)
            # Recebe o tamanho do arquivo em bigendian
            tamanhoArquivo = int.from_bytes(connection.recv(4), byteorder='big')
            arquivo = b''
            # Log
            logger.info('Protocol info: %s', 'Download started', extra=d)
            # Recebe o arquivo
            arquivo = connection.recv(tamanhoArquivo)
            # Log
            logger.info('Protocol info: %s', 'Download finished', extra=d)
            
            # Salva o arquivo na pasta do servidor
            with open('./arquivosServidor/' + fileName, 'w+b') as file:
                file.write(arquivo)

            # Busca todos os arquivos do diretório do servidor
            arquivos = os.listdir(path='./arquivosServidor/')
            # Verifica se o arquivo foi adicionado
            if fileName in arquivos:
                # Status code SUCCES
                header[2] = 1
                # Log
                logger.info('Protocol info: %s', 'ADDFILE SUCCESS', extra=d)
            else:
                # Status code ERROR
                header[2] = 2
                # Log
                logger.info('Protocol info: %s', 'ADDFILE ERROR', extra=d)
            # ADDFILE = commandId = 1
            header[1] = 1
            # Envia o cabeçalho
            connection.send(header)
            # Log
            logger.info('Protocol info: %s', 'ADDFILE response sent', extra=d)


        # Deleta um arquivo
        elif(commandId == 2):
            # Log
            logger.info('Protocol info: %s', 'Received DELETE request', extra=d)
            # Verifica se existe o arquivo informado
            if(os.path.isfile('./arquivosServidor/' + fileName)):
                # Tenta remover o arquivo
                os.remove('./arquivosServidor/' + fileName)
                # Verifica se o arquivo ainda existe
                if(os.path.isfile('./arquivosServidor/' + fileName)):
                    # Status code ERROR
                    header[2] = 2
                    # Log
                    logger.info('Protocol info: %s', 'DELETE ERROR', extra=d)

                else:
                    # Status code SUCCESS
                    header[2] = 1
                    # Log
                    logger.info('Protocol info: %s', 'DELETE SUCCESS', extra=d)

            else:
                # Status code ERROR
                header[2] = 2
            # DELETE = commandId = 2
            header[1] = 2
            # Envia o cabeçalho
            connection.send(header)
            # Log
            logger.info('Protocol info: %s', 'DELETE response sent', extra=d)

        # Lista todos os arquivos 
        elif(commandId == 3):
            # Log
            logger.info('Protocol info: %s', 'Received GETFILESLIST request', extra=d)
            numberFiles = 0
            files: list[str] = []
            # Busca tudo o que está dentro do diretório
            dir = os.listdir('./arquivosServidor/')
            # Verifica se o que foi encontrado no diretório é arquivo ou diretorio
            header[1] = 3
            fileNameSizeResponse = 0
            # Passa por tudo que foi encontrado para verificar o que é arquivo
            for nameFile in dir:
                # Verifica o número de arquivos
                if (os.path.isfile(str('./arquivosServidor/' + nameFile))):
                    numberFiles = numberFiles + 1
                    # Cria um vetor com os nomes dos arquivos encontrados
                    files.append(str(nameFile))
            # Verifica se foi encontrado algum arquivo
            if (numberFiles > 0):
                # Status code SUCCESS
                header[2] = 1
                # Envia o cabeçalho
                connection.send(header)
                # Envia o número de arquivos em bigendian
                connection.send(numberFiles.to_bytes(2, "big"))
                # Passa por todos os arquivos encontrados
                for nameFile in files:
                    # Obtem o tamanho do nome do arquivo
                    fileNameSizeResponse = len(nameFile)
                    # Envia o tamanho do nome do arquivo
                    connection.send(fileNameSizeResponse.to_bytes(1,"big"))
                    # Envia o nome do arquivo
                    connection.send(nameFile.encode())
            else:
                # Log
                logger.info('Protocol info: %s', 'GETFILESLIST error', extra=d)
                # Status code ERROR
                header[2] = 2
                # Envia o cabeçalho de requisição
                connection.send(header) 
                # Log
                logger.info('Protocol info: %s', 'GETFILESLIST header sent', extra=d)
        
        # GetFile faz download de um arquivo
        elif(commandId == 4):
            # Log
            logger.info('Protocol info: %s', 'Received GETFILE request', extra=d)
            # GETFILE = commandId = 4
            header[1] = 4
            # Lista os arquivos da pasta do servidor
            arquivos = os.listdir('./arquivosServidor')
            if(arquivos.__contains__(fileName)):
                if(len(fileName) <= 255):
                    # Status code SUCCESS
                    header[2] = 1
                    # Envia o cabeçalho de resposta
                    connection.send(header) 
                    # Log
                    logger.info('Protocol info: %s', 'GETFILE header sent', extra=d)
                    #Pega o tamanho do arquivo e coverte em bytes e ordena em big endian
                    fileSize = (os.stat('./arquivosServidor/' + fileName).st_size).to_bytes(4, "big") 
                    #Envia o tamanho do arquivo
                    connection.send(fileSize) 
                    #Abre o arquivo no modo leitura binaria
                    fileOpen = open('./arquivosServidor/' + fileName, 'rb') 
                    #Transforma o arquivo em bytes
                    file = fileOpen.read() 
                    # Log
                    logger.info('Protocol info: %s', 'Upload started', extra=d)
                    # Envia o arquivo
                    connection.send(file)
                    # Log
                    logger.info('Protocol info: %s', 'Upload finished', extra=d)
            else:
                logger.info('Protocol info: %s', 'GETFILE error', extra=d)
                # Status code ERROR
                header[2] = 2
                # Envia o cabeçalho de resposta
                connection.send(header) 
                logger.info('Protocol info: %s', 'GETFILE header sent', extra=d)


def main():
    vetorThreads = []

    while 1:
        # Limite de 5 conexões
        serverSocket.listen(5)
        # Servidor escuta as conexões
        (connection, (ip, port)) = serverSocket.accept()
        # Define usuário e a porta para o log
        d = {'clientip': ip, 'user': port}
        # Log
        logger.info('Protocol info: %s', 'connection established', extra=d)

        # Cria e inicia uma thread para cada client
        thread = threading.Thread(target=threadConnection, args=(ip, port, connection, ))
        thread.start()

        # Adiciona a lista de threads
        vetorThreads.append(thread)

    # Espera a finalização de todas as threads
    for socketThreads in vetorThreads:
        # Faz com que o pai aguarde a finalização das threads filhas
        socketThreads.join()

    # Finaliza a conexao
    serverSocket.close()


main()

