'''
    # Questão 1 - TCP Cliente #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 12/10/2021
    # Data de modificação: 12/10/2021
    # Descrição: Envia mensagens para um servidor com uma das seguintes opções:
            - CONNECT user, password: Tenta realizar a conexão com servidor
            - PWD: Exibe caminho atual
            - CHDIR *path*: Muda o diretório para o *path* especificado 
            - GETFILES: Exibe todos os arquivos do diretório atual
            - GETDIRS: Exibe todos os diretórios do diretório atual
            - EXIT: Finaliza a conexão com o servidor

'''
import socket
import hashlib

ip = "127.0.0.1"
port = 5973

#Variavel contendo o ip e a porta
addr = (ip, port)
#Cria um socket do tipo TCP os parametros AF_INET e SOCK_STREAM definem
#qual a familia de endereços será utilizada e qual o tipo de socket
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketClient.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                        1)  #Permite o reuso de endereços ips
socketClient.connect(
    addr
)  #Realiza a conexão do socket utilizando o ip e a porta definidos anteriormente
'''
### main() ###
# Metodo que pega a operação do cliente, e aguarda
# a resposta do servidor.
# Params: 
    - none
'''


def main():
    connected = False
    while True:
        operation = input("> ")
        operationFormated = ''

        if len(operation.split()) > 1:
            for index, operations in enumerate(operation.split()):
                if index == 0:
                    operationFormated = operations.upper()
                else:
                    operationFormated = operationFormated + ' ' + operations
        else:
            operationFormated = operation.upper()
        if (len(operationFormated) > 0):
            if ((operationFormated.split())[0] == "CONNECT"):
                senhaHash = hashlib.sha512(
                    operationFormated[2].encode('utf-8')).hexdigest()
                operationFormated = (operationFormated.split())[0] + ' ' + (
                    operationFormated.split())[1] + ' ' + senhaHash
                socketClient.send(operationFormated.encode('utf-8'))
                print(socketClient.recv(1024).decode('utf-8'))
                connected = True
            elif (operationFormated == "EXIT"):
                socketClient.send(operationFormated.encode('utf-8'))
                print(socketClient.recv(1024).decode('utf-8'))
                socketClient.close()
                break

            if (connected and (operationFormated.split())[0] != "CONNECT"):
                if (operationFormated == "HELP"):
                    socketClient.send(operationFormated.encode('utf-8'))
                    operations = socketClient.recv(1024).decode('utf-8')
                    for operations in operations.split(';'):
                        print(operations)

                elif (operationFormated == "GETFILES"):
                    socketClient.send(operationFormated.encode('utf-8'))
                    position = 0
                    listFiles = []
                    numberFiles = int(socketClient.recv(1024).decode('utf-8'))
                    print('Quantidade de arquivos: ', numberFiles)
                    if numberFiles > 0:
                        print("Arquivos: ")
                        files = socketClient.recv(1024).decode('utf-8')
                        listFiles = files.removeprefix('[').removesuffix(
                            ']').split(', ')
                        for fileNames in listFiles:
                            print(
                                fileNames.removeprefix("'").removesuffix("'"))
                    else:
                        print("O diretorio atual não contém nenhum arquivo")

                elif (operationFormated == "GETDIRS"):
                    socketClient.send(operationFormated.encode('utf-8'))
                    position = 0
                    listDir = []
                    numberDir = int(socketClient.recv(1024).decode('utf-8'))
                    print('Quantidade de diretórios: ', numberDir)

                    if numberDir > 0:
                        print("Diretórios: ")
                        dirs = socketClient.recv(1024).decode('utf-8')
                        listDir = dirs.removeprefix('[').removesuffix(
                            ']').split(', ')
                        for dirNames in listDir:
                            print(dirNames.removeprefix("'").removesuffix("'"))

                    else:
                        print("O diretorio atual não contém nenhuma pasta")

                else:
                    socketClient.send(operationFormated.encode('utf-8'))
                    print(socketClient.recv(1024).decode('utf-8'))


main()
