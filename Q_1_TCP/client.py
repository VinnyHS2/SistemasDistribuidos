'''
    # Questão 1 - TCP Cliente #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 12/10/2021
    # Data de modificação: 20/10/2021
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
#Permite o reuso de endereços ips
socketClient.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  
#Realiza a conexão do socket utilizando o ip e a porta definidos anteriormente
socketClient.connect(addr)  

def main():
    connected = False
    while True:
        operation = input("> ")
        operationFormated = ''
        # Verifica se a operação é vazia
        if (len(operation) > 0):
            # Formata a operação
            operationFormated = operation.split()[0].upper() + operation[len(operation.split()[0]):]
            # Verifica se o comando enviado tem mais de 2 argumentos e se é o connect
            if (len(operationFormated.split()) > 2 and (operationFormated.split())[0] == "CONNECT"):
                # Criptografa a senha
                senhaHash = hashlib.sha512(operationFormated.split()[2].encode('utf-8')).hexdigest()
                # Prepara a requisição para o servidor
                operationFormated = (operationFormated.split())[0] + ' ' + (operationFormated.split())[1] + ' ' + senhaHash
                # Envia o comando para o servidor
                socketClient.send(operationFormated.encode('utf-8'))
                # Recebe a resposta do servidor
                response = socketClient.recv(1024).decode('utf-8')
                # Verifica a resposta do servidor para autenticar
                if(response == 'SUCCESS'):
                    connected = True
                # Mostra a resposta do servidor
                print(response)
            elif (operationFormated == "EXIT"):
                # Envia o comando para o servidor
                socketClient.send(operationFormated.encode('utf-8'))
                # Mostra a resposta do servidor
                print(socketClient.recv(1024).decode('utf-8'))
                # Finaliza a conexão com o socket
                socketClient.close()
                break

            # Verifica se o client está conectado e se o comando enviado não é "Connect"
            if (connected and (operationFormated.split())[0] != "CONNECT"):
                if (operationFormated == "GETFILES"):
                    # Envia a operação para o servidor
                    socketClient.send(operationFormated.encode('utf-8'))
                    listFiles = []
                    # Recebe a quantidade de arquivos encontrados
                    numberFiles = int(socketClient.recv(1024).decode('utf-8'))
                    print('Quantidade de arquivos: ', numberFiles)
                    if numberFiles > 0:
                        print("Arquivos: ")
                        # Recebe todos os arquivos
                        files = socketClient.recv(1024).decode('utf-8')
                        # Remove os separadores
                        listFiles = files.removeprefix('[').removesuffix(
                            ']').split(', ')
                        # Passa por todos os arquivos recebidos
                        for fileNames in listFiles:
                            print(fileNames.removeprefix("'").removesuffix("'"))
                    else:
                        print("O diretorio atual não contém nenhum arquivo")

                elif (operationFormated == "GETDIRS"):
                    # Envia a operação para o servidor
                    socketClient.send(operationFormated.encode('utf-8'))
                    listDir = []
                    # Recebe a quantidade de diretórios
                    numberDir = int(socketClient.recv(1024).decode('utf-8'))
                    print('Quantidade de diretórios: ', numberDir)

                    if numberDir > 0:
                        print("Diretórios: ")
                        # Recebe a resposta do servidor
                        dirs = socketClient.recv(1024).decode('utf-8')
                        # Remove os separadores
                        listDir = dirs.removeprefix('[').removesuffix(
                            ']').split(', ')
                        # Passa por todos os diretórios recebidos
                        for dirNames in listDir:
                            # Formata o que foi recebido
                            print(dirNames.removeprefix("'").removesuffix("'"))

                    else:
                        print("O diretorio atual não contém nenhuma pasta")

                else:
                    # Envia a operação para o servidor
                    socketClient.send(operationFormated.encode('utf-8'))
                    # Mostra a mensagem do servidor
                    print(socketClient.recv(1024).decode('utf-8'))


main()
