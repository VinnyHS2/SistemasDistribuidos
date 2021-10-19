'''
    # Questão 1 - TCP Servidor #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 17/10/2021
    # Data de modificação: 17/10/2021
    # Descrição:
        Faz o processamento de mensagens recebidas do cliente, nas quais atualmente são possiveis as seguintes operações:
        - ADDFILE: adiciona um arquivo novo.
        - DELETE: remove um arquivo existente.
        - GETFILESLIST: retorna uma lista com o nome dos arquivos.
        - GETFILE: faz download de um arquivo.


'''
from genericpath import isdir
import logging
import threading
import socket
import os

host = ""
port = 5973
addr = (host, port)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(addr)
FORMAT = '%(asctime)-1s %(clientip)s %(user)s %(message)s'
logging.basicConfig(format=FORMAT,level=20)
logger = logging.getLogger('tcpserver')

commands = "######## BitServer ########\n;CONNECT user password: Confere os dados informados e realiza a conexão do usuário ao servidor; PWD: Devolve ao cliente o caminho atual'; CHDIR *path*: Muda o diretório para o *path* especificado; GETFILES: Devolve ao cliente todos os arquivos do diretório atual; GETDIRS: Devolve ao cliente todos os diretórios do diretório atual; EXIT: Finaliza a conexão com o cliente;"

'''
### threadConnection(ip, port, con) ###
# Metodo que executa as requisições do cliente
# Params: 
    - Ip: ip do cliente
    - Port: porta que o cliente se conectou
    - Conexao: a conexao realizada
'''


def createFile(name):
    try:
        newArchive = open(name, "w")
        newArchive.close()
        return 1
    except:
        return 2

def threadConnection(ip, port, connection):
    d = {'clientip': ip, 'user': port}
    while True:
        header = bytearray(3)
        # Recebe a mensagem
        msg = bytearray(connection.recv(1024))
        print(msg)
        messageType = int(msg[0])
        commandId = int(msg[1])
        fileNameSize = int(msg[2])
        # Decodifica o nome do Arquivo
        fileName = msg[3:].decode('utf-8')
        
        # Adiciona um novo arquivo
        if(commandId == 1):
            logger.info('Protocol info: %s', 'Received ADDFILE request', extra=d)
            tamanhoArquivo = int.from_bytes(connection.recv(4), byteorder='big')
            # Recebe o arquivo
            arquivo = b''
            for _ in range(tamanhoArquivo):
                bytes = connection.recv(1)
                arquivo += bytes
            
            # Salva o arquivo na pasta do servidor
            with open('./arquivosServidor/' + fileName, 'w+b') as file:
                file.write(arquivo)

            # Busca todos os arquivos do diretório do servidor
            arquivos = os.listdir(path='./arquivosServidor')
            # Verifica se o arquivo foi adicionado
            if fileName in arquivos:
                header[2] = 1
                logger.info('Protocol info: %s', 'ADDFILE SUCCESS', extra=d)
            else:
                header[2] = 2
                logger.info('Protocol info: %s', 'ADDFILE ERROR', extra=d)
            header[0] = 2
            header[1] = 1
            connection.send(header)
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
                    header[2] = 2
                    logger.info('Protocol info: %s', 'DELETE ERROR', extra=d)

                else:
                    header[2] = 1
                    logger.info('Protocol info: %s', 'DELETE SUCCESS', extra=d)

            else:
                header[2] = 2
            header[0] = 2
            header[1] = 2
            # Envia o cabeçalho
            connection.send(header)
            logger.info('Protocol info: %s', 'DELETE response sent', extra=d)

        # Lista todos os arquivos 
        elif(commandId == 3):
            # Log
            logger.info('Protocol info: %s', 'Received GETFILESLIST request', extra=d)
            numberFiles = 0
            dirs: list[str] = []
            # Busca tudo o que está dentro do diretório
            files = os.listdir('./arquivosServidor/')
            # Verifica se o que foi encontrado no diretório é arquivo ou diretorio
            header[0] = 2
            header[1] = 3
            for nameFile in files:
                if (os.path.isfile(str('./arquivosServidor/' + nameFile))):
                    numberFiles = numberFiles + 1
                    # Cria um vetor com os nomes dos arquivos encontrados
                    dirs.append(str(nameFile))
            # Verifica se foi encontrado algum arquivo
            if (numberFiles > 0):
                header[2] = 2
                numberFiles = 255
                connection.send(header)
                # Envia o numero de arquivos
                connection.send(numberFiles.to_bytes(2, "big"))
                # Envia o nome dos arquivos
                # connection.send(str(dirs).encode('utf-8'))
            else:
                connection.send(('Nenhum diretorio encontrado').encode('utf-8'))
        
        # GetFile faz download de um arquivo
        elif(commandId == 4):
            # Log
            logger.info('Protocol info: %s', 'Received GETFILE request', extra=d)
            connection.send(commands.encode('utf-8'))

'''
### main() ###
# Metodo que realiza a conexão do cliente
# Params: 
    - none
'''


def main():
    vetorThreads = []

    while 1:
        # Limite de 20 conexões
        serverSocket.listen(20)
        # Servidor escuta as conexões
        (connection, (ip, port)) = serverSocket.accept()
        # Define usuário e a porta para o log
        d = {'clientip': ip, 'user': port}
        # Log
        logger.info('Protocol info: %s', 'connection established', extra=d)

        # Cria e inicia uma thread para cada novo client
        thread = threading.Thread(
            target=threadConnection, args=(ip, port, connection, ))
        thread.start()

        # Adiciona a lista de threads
        vetorThreads.append(thread)

    # Espera a finalização de todas as threads
    for socketThreads in vetorThreads:
        socketThreads.join()

    # Finaliza a conexao
    serverSocket.close()


main()

