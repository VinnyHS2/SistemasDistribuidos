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
from genericpath import isdir
import threading
import socket
from datetime import date, datetime
import os
import hashlib

host = ""
port = 5973
addr = (host, port)
userMain = 'pato'
passwordMain = '6b3b006aa3a86286c359a6d243d62a61e46f0c5f7d1db587faa26fbe72718eaee33f774af164e3ba790d4ae4136a25dc993d3246f7be6691fa7346d0be0f1a71'

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(addr)

commands = "######## BitServer ########\n;CONNECT user password: Confere os dados informados e realiza a conexão do usuário ao servidor; PWD: Devolve ao cliente o caminho atual'; CHDIR *path*: Muda o diretório para o *path* especificado; GETFILES: Devolve ao cliente todos os arquivos do diretório atual; GETDIRS: Devolve ao cliente todos os diretórios do diretório atual; EXIT: Finaliza a conexão com o cliente;"

'''
### programa(ip, port, con) ###
# Metodo que executa as requisições do cliente
# Params: 
    - Ip: ip do cliente
    - Port: porta que o cliente se conectou
    - Conexao: a conexao realizada
'''


def programa(ip, port, connection):

    authenticated = False

    while True:

        # Recebe a mensagem
        msg = connection.recv(1024)

        # Decodifica a mensagem
        msg_str = msg.decode('utf-8')

        # Iniciar conexão
        if ((msg_str.split())[0] == 'CONNECT'):
            if ((msg_str.split())[1] == userMain):
                if ((msg_str.split())[2] == passwordMain):
                    connection.send(('SUCCESS').encode('utf-8'))
                    authenticated = True
                    break
            else:
                connection.send(('ERROR').encode('utf-8'))

        elif (msg_str == 'EXIT'):
            print('Cliente com o ip: ', ip, ', na porta: ',port, ', foi desconectado!')
            connection.send(('Conexão encerrada').encode('utf-8'))
            connection.close()
            break

        else:
            print('aoku')
            connection.send(('ERROR').encode('utf-8'))


    while authenticated == True:

        # Recebe a mensagem
        msgNova = connection.recv(1024)
        print(msgNova)
        # Decodifica a mensagem
        msg_str = msgNova.decode('utf-8')

        # Notifica servidor sobre a saída do cliente
        if(msg_str == 'EXIT'):
            print('Cliente com o ip: ', ip, ', na porta: ',
                  port, ', foi desconectado!')
            connection.send(('Conexão encerrada').encode('utf-8'))
            connection.close()
            break

        # Mostra os comandos do servidor
        elif(msg_str == 'HELP'):
            connection.send(commands.encode('utf-8'))

        # Comandos Nosso
        # Mostrar caminho atual OK
        elif(msg_str == "PWD"):
            currentPath: os.PathLike = os.getcwd()
            print(currentPath)
            connection.send((currentPath).encode('utf-8'))

        # Todos os arquivos
        elif(msg_str == "GETFILES"):
            numberFiles = 0
            dirs: list[str] = []
            directory = str(os.getcwd())
            files = os.listdir(directory)
            print('Creio que esses sejam os arquivos', files)
            for nameFile in files:
                if (os.path.isfile(str(directory + '\\' + nameFile))):
                    numberFiles = numberFiles + 1
                    dirs.append(str(nameFile))
            if (numberFiles > 0):
                connection.send(str(numberFiles).encode('utf-8'))
                connection.send(str(dirs).encode('utf-8'))
            else:
                connection.send(
                    ('Nenhum diretorio encontrado').encode('utf-8'))

        # Todos os diretórios
        elif(msg_str == "GETDIRS"):
            quantidade = 0
            diretorios: list[str] = []
            diretorio = str(os.getcwd())
            arquivos = os.listdir(diretorio)
            print('Creio que esses sejam os arquivos', arquivos)
            for arquivo in arquivos:
                if(os.path.isdir(str(diretorio + '\\' + arquivo))):
                    quantidade = quantidade + 1
                    diretorios.append(str(arquivo))
            if(quantidade > 0):
                connection.send(str(quantidade).encode('utf-8'))
                connection.send(str(diretorios).encode('utf-8'))
            else:
                connection.send(('Nenhum diretorio encontrado').encode('utf-8'))





        # Alterar o diretório parcialmente #TODO: Falar quando o diretório não existe ou criar depende
        elif((msg_str.split())[0] == "CHDIR"):
            if ((len(msg_str.split()) > 1) and os.path.isdir((msg_str.split())[1])):
                os.chdir((msg_str.split())[1])
                connection.send("SUCCESS".encode('utf-8'))
            else:
                connection.send(('ERROR').encode('utf-8'))

        else:
            print('aoksu')
            connection.send(('ERROR').encode('utf-8'))


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
        print('Sessão com o cliente: ', ip,
              ', na porta: ', port, ', foi estabelecida!')

        # Cria e inicia uma thread para cada cliente que chega
        thread = threading.Thread(
            target=programa, args=(ip, port, connection, ))
        thread.start()

        # Adiciona ao vetor de threads
        vetorThreads.append(thread)

    # Aguarda todas as threads serem finalizadas
    for socketThreads in vetorThreads:
        socketThreads.join()

    # Fecha conexao
    serverSocket.close()


main()
