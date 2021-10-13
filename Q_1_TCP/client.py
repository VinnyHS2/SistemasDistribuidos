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

addr = (ip, port) 
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
socketClient.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketClient.connect(addr)

'''
### main() ###
# Metodo que pega a entrada do cliente, e aguarda
# a resposta do servidor.
# Params: 
    - none
'''
def main():
    while True:
        comando = input("> ")
        entrada = ''

        # formatacao do primeiro comando para maiusculo
        if len(comando.split()) > 1:
            for index, comandos in enumerate(comando.split()):
                if index == 0:
                    entrada = comandos.upper()
                else:
                    entrada = entrada + ' ' + comandos
        else:
            entrada = comando.upper()

        if((entrada.split())[0] == "CONNECT"):
            #TODO codificar a senha para sha-512
            # print("entrada completa:", entrada)
            # print("entrada posição 2:", entrada.split()[2])
            senhaHash = hashlib.sha512(entrada[2].encode('utf-8')).hexdigest()
            entrada = (entrada.split())[0] + ' ' + (entrada.split())[1] + ' ' + senhaHash
            print("entrada completa:", entrada)
            
        # Envia mensagem
        socketClient.send(entrada.encode('utf-8'))
        
        # Lista os comandos
        if(entrada == "HELP"):
            comandos = socketClient.recv(1024).decode('utf-8')
            for comandos in comandos.split(';'):
                print(comandos)

        # Envia a mensagem e fecha a conexão
        if(entrada == "EXIT"):
            socketClient.close()
            break
        
        if(entrada == "PWD"):
            print(socketClient.recv(1024).decode('utf-8'))

        if((entrada.split())[0] == "CONNECT"):
            print(socketClient.recv(1024).decode('utf-8'))
        
        if(entrada == "GETFILES"):
            #TODO: listar os arquivos da forma correta
            print(socketClient.recv(1024).decode('utf-8'))
        
        if(entrada == "GETDIRS"):
            print(socketClient.recv(1024).decode('utf-8'))

        if((entrada.split())[0] == "CHDIR"):
            print('oi')
            # print(socketClient.recv(1024).decode('utf-8'))
main()
