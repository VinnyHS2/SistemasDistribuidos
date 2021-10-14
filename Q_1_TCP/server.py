'''
    # Questão 1 - TCP Servidor #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 12/10/2021
    # Data de modificação: 12/10/2021
    # Descrição:
        Faz o processamento de mensagens recebidas do cliente, nas quais atualmente são possiveis as seguintes operações:
            - CONNECT user, password: Confere os dados informados e realiza a conexão do usuário ao servidor
            - PWD: Devolve ao cliente o caminho atual
            - CHDIR *path*: Muda o diretório para o *path* especificado 
            - GETFILES: Devolve ao cliente todos os arquivos do diretório atual
            - GETDIRS: Devolve ao cliente todos os diretórios do diretório atual
            - EXIT: Finaliza a conexão com o cliente

'''
import threading
import socket
from datetime import date, datetime
import os
import hashlib

host = ""
port = 5973
addr = (host, port)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(addr)

comandos = "######## BitServer ########\n;EXIT: finaliza a conexão com o servidor;TIME: retorna a hora do sistema;DATE: retorna a data do sistema;FILES: retorna os arquivos da pasta compartilhada;HELP: lista os comandos;DOWN 'nomeArquivo': faz o download de um arquivo;"

'''
### programa(ip, port, con) ###
# Metodo que executa as requisições do cliente
# Params: 
    - Ip: ip do cliente
    - Port: porta que o cliente se conectou
    - Conexao: a conexao realizada
'''


def programa(ip, port, connection):
    while True:

        # Recebe a mensagem
        msg = connection.recv(1024)

        # Decodifica a mensagem
        msg_str = msg.decode('utf-8')

        # Notifica servidor sobre a saída do cliente
        if(msg_str == 'EXIT'):
            print('Cliente com o ip: ', ip, ', na porta: ',
                  port, ', foi desconectado!')
            break

        # Mostra os comandos do servidor
        if(msg_str == 'HELP'):
            connection.send(comandos.encode('utf-8'))
            print(serverSocket.recv(1024).decode('utf-8'))

        # Comandos Nosso
        # Mostrar caminho atual OK
        if(msg_str == "PWD"):
            currentPath: os.PathLike = os.getcwd()
            print(currentPath)
            connection.send((currentPath).encode('utf-8'))

        # Iniciar conexão
        if((msg_str.split())[0] == 'CONNECT'):
            connection.send('server' + msg_str.encode('utf-8'))

        # Todos os arquivos
        if(msg_str == "GETFILES"):
            quantidade = 0
            diretorios: list[str] = []
            diretorio = str(os.getcwd())
            arquivos = os.listdir(diretorio)
            print('Creio que esses sejam os arquivos', arquivos)
            for arquivo in arquivos:
                if (os.path.isfile(str(diretorio + '\\' + arquivo))):
                    quantidade = quantidade + 1
                    diretorios.append(str(arquivo))
            if (quantidade > 0):
                connection.send(str(quantidade).encode('utf-8'))
                for dir in diretorios:
                    print(dir)
                    connection.sendall(dir.encode('utf-8'))
            else:
                connection.send(
                    ('Nenhum diretorio encontrado').encode('utf-8'))

        # Todos os diretórios
        if(msg_str == "GETDIRS"):
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
                for dir in diretorios:
                    print(dir)
                    connection.sendall(dir.encode('utf-8'))
            else:
                connection.send(('Nenhum diretorio encontrado').encode('utf-8'))





        # Alterar o diretório parcialmente #TODO: Falar quando o diretório não existe ou criar depende
        if((msg_str.split())[0] == "CHDIR"):
            os.chdir((msg_str.split())[1])
            response = 'diretório alterado com sucesso'
            connection.send(response.encode('utf-8'))



'''
### main() ###
# Metodo que realiza a conexão do cliente
# Params: 
    - none
'''

def hashStr(value):
    return hashlib.sha512(value.encode('utf-8')).hexdigest()

def check_secure_val(hashRecived, password):
    if hashStr(password) == hashRecived:
        return True
    else:
        return False

def main():
    vetorThreads = []

    while 1:
        # Limite de 20 conexões
        serverSocket.listen(20)
        # Servidor escuta as conexões
        # if(!autenticado == True):
        #     (connection, (ip,port) ) = serverSocket.accept()
        #     print('ERROR')
        #     serverSocket.close()
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
