'''
    # Questão 1 - TCP Servidor #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 12/10/2021
    # Data de modificação: 12/10/2021
    # Descrição:
        Faz o processamento de mensagens recebidas do cliente, nas quais atualmente são possiveis as seguintes operações:
            - CONNECT user password: Confere os dados informados e realiza a conexão do usuário ao servidor
            - PWD: Devolve ao cliente o caminho atual
            - CHDIR *path*: Muda o diretório para o *path* especificado 
            - GETFILES: Devolve ao cliente todos os arquivos do diretório atual
            - GETDIRS: Devolve ao cliente todos os diretórios do diretório atual
            - EXIT: Finaliza a conexão com o cliente

'''
import logging
import threading
import socket
import os

host = ""
port = 5973
addr = (host, port)
userMain = 'pato'
passwordMain = '3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2'

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
    #variável para verficar se o usuario está autenticado 
    authenticated = False

    d = {'clientip': ip, 'user': port}
    while True:
    
        msg_str = ''
        # Recebe a mensagem e decodifica
        msg_str = connection.recv(1024).decode('utf-8')

        # Iniciar conexão
        if ((msg_str.split())[0] == 'CONNECT'):
            passwordClient = (msg_str.split())[2]
            userClient = (msg_str.split())[1]
            #Log
            logger.info('Protocol info: %s', 'Received CONNECT request', extra=d)
            # Verifica se o usuario está correto
            if (userClient == userMain):
                # Verifica se a senha está correta
                if (passwordClient == passwordMain):
                    # print(msg_str.split()[2])
                    # Log
                    logger.info('Protocol info: %s', 'CONNECT SUCCESS', extra=d)
                    # Envia a mensagem de SUCCESS para o cliente
                    connection.send(('SUCCESS').encode('utf-8'))
                    # Define a variável de autenticação para verdadeiro
                    authenticated = True
                else:
                    # Log
                    logger.info('Protocol info: %s', 'CONNECT ERROR', extra=d)
                    # Envia a mensagem de ERROR para o cliente
                    connection.send(('ERROR').encode('utf-8'))
            else:
                # Log
                logger.info('Protocol info: %s', 'CONNECT ERROR', extra=d)
                # Envia a mensagem de ERROR para o cliente
                connection.send(('ERROR').encode('utf-8'))

        # Verifica se o comando recebi é EXIT
        elif(msg_str == 'EXIT'):
            # Log
            logger.info('Protocol info: %s', 'Received EXIT request', extra=d)
            # Envia a mensagem de conexão encerrada
            connection.send(('Conexão encerrada').encode('utf-8'))
            # Encerra a conexão
            connection.close()
            # Sai do laço de repetição infinito
            authenticated = False
            break

        # Verifica se o comando recebi é PWD e se está autenticado
        elif(authenticated == True and msg_str == "PWD"):
            # Log
            logger.info('Protocol info: %s', 'Received PWD request', extra=d)
            # Guarda em uma variável o caminho atual
            currentPath: os.PathLike = os.getcwd()
            # Envia o caminho atual paro o cliente
            connection.send((currentPath).encode('utf-8'))

        # Verifica se o comando recebi é GETFILES e se está autenticado
        elif((authenticated == True) and (msg_str == "GETFILES")):
            # Log
            logger.info('Protocol info: %s', 'Received GETFILES request', extra=d)
            # Variável que armazena o número de arquivos
            numberFiles = 0
            # Variável que armazena o nome dos arquivos
            listFileName: list[str] = []
            # Variável que armazena o diretório atual
            directory = str(os.getcwd())
            # Váriavel que armazena tudo o que tem no diretório
            files = os.listdir(directory)
            # Percore todos os valores que estão em files
            for fileName in files:
                # Verifica se é arquivo
                if (os.path.isfile(str(directory + '\\' + fileName))):
                    # Incrementa 1 o número de arquivos
                    numberFiles = numberFiles + 1
                    # Adiciona o nome do arquivo na lista
                    listFileName.append(str(fileName))
            # Verifica se o número de arquivo é maior que 0
            if (numberFiles > 0):
                # Envia o número de arquivos para o cliente
                connection.send(str(numberFiles).encode('utf-8'))
                # Envia a lista com o nome dos arquivos para o cliente
                connection.send(str(listFileName).encode('utf-8'))
            # Verifica se o número de arquivos for 0
            else:
                # Envia 0 para o cliente
                connection.send(('0').encode('utf-8'))
            logger.info('Protocol info: %s', 'GETFILES SUCCESS', extra=d)



        # Verifica se o comando recebi é GETDIRS e se está autenticado
        elif(authenticated == True and msg_str == "GETDIRS"):
            # Log
            logger.info('Protocol info: %s', 'Received GETDIRS request', extra=d)
            # Variável que armazena o número de arquivos
            numberFiles = 0
            # Variável que armazena o nome dos diretórios
            listDirName: list[str] = []
            # Variável que armazena o diretório atual
            directory = str(os.getcwd())
            # Váriavel que armazena tudo o que tem no diretório
            files = os.listdir(directory)
            # Percore todos os valores que estão em files
            for dirNames in files:
                # Verifica se é diretório
                if(os.path.isdir(str(directory + '\\' + dirNames))):
                    # Incrementa 1 o número de diretório
                    numberFiles = numberFiles + 1
                    # Adiciona o nome do arquivo na lista
                    listDirName.append(str(dirNames))
            # Verifica se o número de arquivo é maior que 0
            if(numberFiles > 0):
                # Envia o número de diretórios para o cliente
                connection.send(str(numberFiles).encode('utf-8'))
                # Envia a lista com o nome dos arquivos para o cliente
                connection.send(str(listDirName).encode('utf-8'))
            # Verifica se o número de arquivos for 0
            else:
                # Envia 0 para o cliente
                connection.send(('0').encode('utf-8'))
            # Log
            logger.info('Protocol info: %s', 'GETDIRS SUCCESS', extra=d)


        # Altera o diretório atual do sistema
        elif(authenticated == True and (msg_str.split())[0] == "CHDIR"):
            # Log
            logger.info('Protocol info: %s', 'Received CHDIR request', extra=d)
            # Verifica se existe mais de um argumento e se o diretório informado é um diretório
            if ((len(msg_str.split()) > 1) and os.path.isdir((msg_str.split())[1])):
                # Muda o diretório atual
                os.chdir((msg_str.split())[1])
                # Envia mensagem de sucesso
                connection.send("SUCCESS".encode('utf-8'))
                # Log
                logger.info('Protocol info: %s', 'CHDIR SUCCESS', extra=d)
            else:
                # Envia mensagem de erro
                connection.send(('ERROR').encode('utf-8'))
                # Log
                logger.info('Protocol info: %s', 'CHDIR ERROR', extra=d)

        else:
            # Envia mensagem de erro
            connection.send(('ERROR').encode('utf-8'))


def main():
    # Variável que armazena uma lista de threads
    threadList = []

    while True:
        # Limite de 5 conexões
        serverSocket.listen(5)
        # Servidor espera alguem se conectar na porta 5973 está é uma função bloqueante
        (connection, (ip, port)) = serverSocket.accept()
        # Define usuário e a porta para o log
        d = {'clientip': ip, 'user': port}
        # Log
        logger.info('Protocol info: %s', 'connection established', extra=d)

        # Cria e inicia uma thread para cada cliente que chega
        thread = threading.Thread(
            target=threadConnection, args=(ip, port, connection, ))
        thread.start()

        # Adiciona ao vetor de threads
        threadList.append(thread)

    # Aguarda todas as threads serem finalizadas
    for socketThreads in threadList:
        socketThreads.join()

    # Fecha conexão
    serverSocket.close()


main()
