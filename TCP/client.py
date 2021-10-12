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

ip = "127.0.0.1"
port = 5973

addr = (ip, port) 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    pass
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(addr)

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
            entrada[2] = entrada.encode('sha-512')

        # Envia mensagem
        s.send(entrada.encode('utf-8'))
        
        # Lista os comandos
        
        #TODO: fazer switch case

        if(entrada == "HELP"):
            comandos = s.recv(1024).decode('utf-8')
            for comandos in comandos.split(';'):
                print(comandos)

        # Envia a mensagem e fecha a conexão
        if(entrada == "EXIT"):
            s.close()
            break
        
        if(entrada == "PWD"):
            print(s.recv(1024).decode('utf-8'))

        if((entrada.split())[0] == "CONNECT"):
            print(s.recv(1024).decode('utf-8'))
        
        if(entrada == "GETFILES"):
            #TODO: listar os arquivos da forma correta
            print(s.recv(1024).decode('utf-8'))
        
        if(entrada == "GETDIRS"):
            print(s.recv(1024).decode('utf-8'))

        if((entrada.split())[0] == "CHDIR"):
            print(s.recv(1024).decode('utf-8'))
main()
