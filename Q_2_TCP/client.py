'''
    # Questão 1 - TCP Cliente #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 17/10/2021
    # Data de modificação: 17/10/2021
    # Descrição: Envia mensagens para um servidor com uma das seguintes opções:
        - ADDFILE: adiciona um arquivo novo.
        - DELETE: remove um arquivo existente.
        - GETFILESLIST: retorna uma lista com o nome dos arquivos.
        - GETFILE: faz download de um arquivo.

'''
from array import array
import socket
import os

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
    while True:
        header = bytearray(3)
        header[0] = 1
        inputClient = input("> ")
        operation = ''

        if len(inputClient.split()) > 1:
            fileName = inputClient.split()[1]
            operation = inputClient.split()[0].upper()
        else:
            operation = inputClient.upper()
        if (len(operation) > 0):
            if (operation == "ADDFILE"):
                header[1] = 1
                header[2] = len(fileName)
                arquivos = os.listdir('./arquivosCliente')
                if(arquivos.__contains__(fileName)):
                    if(len(fileName) <= 255):
                        socketClient.send(header + bytearray(fileName.encode())) # Envia o cabeçalho de requisição
                        fileSize = (os.stat('./arquivosCliente/' + fileName).st_size).to_bytes(4, "big") #Pega o tamanho do arquivo e coverte em bytes e ordena em big endian
                        socketClient.send(fileSize) #Envia o tamanho do arquivo
                        file = open('./arquivosCliente/' + fileName, 'rb') #Abre o arquivo
                        byte = file.read(1)
                        while byte != b'': #Envia o arquivo byte a byte
                            socketClient.send(byte)
                            byte = file.read(1)
                        print(socketClient.recv(1024))
                else:
                    print('Arquivo não encontrado')


            elif ((operation.split()[0]) == "DELETE"):
                header[1] = 2
                header[2] = len(fileName)
                socketClient.send(header + bytearray(fileName.encode()))
                
                print(socketClient.recv(1024))

            elif (operation == "GETFILESLIST"):
                print('fudeo')
                header[1] = 3
                header[2] = 0
                socketClient.send(header)
                
                print(socketClient.recv(1024))
                print(socketClient.recv(1024))



main()
