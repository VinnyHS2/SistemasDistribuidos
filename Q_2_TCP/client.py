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
import socket
import os

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
                # Define commandId
                header[1] = 1
                # Define o tamanho do nome do arquivo
                header[2] = len(fileName)
                # Lista os arquivos do client
                arquivos = os.listdir('./arquivosCliente')

                # Busca o arquivo com o nome especificado
                if(arquivos.__contains__(fileName)):
                    # Verifica se o nome do arquivo está nos parametros
                    if(len(fileName) <= 255):
                        # Envia o cabeçalho de requisição
                        socketClient.send(header + bytearray(fileName.encode())) 
                        #Pega o tamanho do arquivo e coverte em bytes e ordena em big endian
                        fileSize = (os.stat('./arquivosCliente/' + fileName).st_size).to_bytes(4, "big") 
                        #Envia o tamanho do arquivo
                        socketClient.send(fileSize) 
                        #Abre o arquivo no modo leitura binaria
                        fileOpen = open('./arquivosCliente/' + fileName, 'rb') 
                        #Transforma o arquivo em bytes
                        file = fileOpen.read() 
                        # Envia o arquivo
                        socketClient.send(file)
                        # Recebe a confirmação do servidor
                        response = int(socketClient.recv(3)[2])
                        if(response == 1):
                            print("SUCCESS")
                        else:
                            print("ERROR")

                else:
                    print('Arquivo não encontrado')

            elif ((operation.split()[0]) == "DELETE"):
                # Define commandId
                header[1] = 2
                # Define o tamanho do nome do arquivo
                header[2] = len(fileName)
                # Envia o cabeçalho e nome do arquivo
                socketClient.send(header + bytearray(fileName.encode()))
                
                # Recebe a confirmação do servidor
                response = int(socketClient.recv(3)[2])
                if(response == 1):
                    print("SUCCESS")
                else:
                    print("ERROR")

            elif (operation == "GETFILESLIST"):
                # Define o CommandId
                header[1] = 3
                # Como não há nome de arquivo, o tamanho é enviado com 0
                header[2] = 0
                # Envia o cabeçalho
                socketClient.send(header)
                
                # Verifica se o status code é SUCCESS
                if(socketClient.recv(3)[2] == 1):
                    # Recebe a quantidade de arquivos
                    numberFiles = int.from_bytes(socketClient.recv(2), 'big')
                    for _ in range(numberFiles):
                        # Recebe o tamanho do arquivo em bigendian
                        filenameSize = int.from_bytes(socketClient.recv(1), 'big')
                        # Recebe o nome do arquivo
                        print(socketClient.recv(filenameSize).decode())
                else:
                    print("ERROR")
                    
            elif (operation == "GETFILE"):
                # Define o commandId
                header[1] = 4
                # Define o tamanho do nome do arquivo
                header[2] = len(fileName)
                # Envia o cabeçalho e o nome do arquivo
                socketClient.send(header + bytearray(fileName.encode()))
                # Verifica se houve arquivos
                if(socketClient.recv(3)[2] == 1):
                    # Recebe o tamanho do arquivo em bigendian
                    tamanhoArquivo = int.from_bytes(socketClient.recv(4), byteorder='big')
                    # Recebe o arquivo
                    arquivo = b''
                    arquivo = socketClient.recv(tamanhoArquivo)

                    # Salva o arquivo na pasta do client
                    with open('./arquivosCliente/' + fileName, 'w+b') as file:
                        file.write(arquivo)
                    print("SUCCESS")
                else:
                    print('ERROR')



main()
