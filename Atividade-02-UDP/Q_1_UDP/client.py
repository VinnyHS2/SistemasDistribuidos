import socket
import emoji
import re
from emoji.core import emoji_count
import threading

ip = "127.0.0.1"
port = 5973

#Variavel contendo o ip e a porta
addr = (ip, port)
#Cria um socket do tipo TCP os parametros AF_INET e SOCK_DGRAM definem
#qual a familia de endereços será utilizada e qual o tipo de socket
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Permite o reuso de endereços ips
socketClient.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  
#Realiza a conexão do socket utilizando o ip e a porta definidos anteriormente
socketClient.connect(addr)  
#Função para verificar se uma mensagem é uma url
def isUrl(url):
    #Regex para verificar se a mensagem é uma url
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// ou https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #dominio...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...ou ip
        r'(?::\d+)?' # porta opicional
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url)

#Função para receber mensagens
def mensageReceive(mensage: bytes):
    # socket.bind((ip, int(port)))
    # while True:
        # mensage, ipAddress = socketClient.recvfrom(322)
        mensageType = int(mensage[0])
        nickSize = int(mensage[1])
        nick = mensage[2:nickSize+2].decode()
        mensageSize = mensage[nickSize+2]
        mensagePosition = int(nickSize + 3)
        mensageContent = mensage[mensagePosition : (mensagePosition + mensageSize)].decode()
        if mensageType == 4:
            print("pidgeon")
            # socketClient.sendto(mensageContent.encode(), ipAddress)
        elif mensageType == 3:
            print(nick + ' has sent a link: ' + mensageContent)
        elif mensageType == 2:
            print(nick + ' said: ' + emoji.emojize(mensageContent))
        else:
            print(nick + ' said: ' + mensageContent)
# Função para enviar mensagens
def mensageSend(ip, port):
    while True:
        #Recebe a mensagem do cliente
        mensage = input("Type you mensage: ")
        # Atribui o tipo de mensagem para 1
        mensageType = 1
        # Atribui o tamanho da mensagem para a variável mensageSize
        mensageSize= len(mensage.encode())
        # Atribui o tamanho do nickname para a variável nickSize
        nicknameSize= len(nickname.encode())
        # Verifica se a mensagem é menor do que 255 bytes
        if len(mensage.encode()) > 255:
            print("Mensage too long")
        else:
            # Verifica se a mensagem possui emojis
            if(emoji_count(emoji.emojize(mensage)) > 0):
                mensageType = 2
            # Verifica se a mensagem é uma url
            if(isUrl(mensage) != None):
                mensageType = 3
            # Verifica se a mensagem é do tipo ECHO
            if(mensage.find("ECHO") == 0):
                mensageType = 4
            
            print((str(mensageType) + str(nicknameSize) + nickname + str(mensageSize) + mensage).encode())
            mensage = (mensageType.to_bytes(1,'big') + nicknameSize.to_bytes(1,'big') + nickname.encode() + mensageSize.to_bytes(1,'big') + mensage.encode())
            mensageReceive(mensage)
            # print(emoji.emojize(mensage))
            # socketClient.send(mensage.encode())
            # if mensageType == 4:
                # massage, ipAddress = socketClient.recvfrom(322)
                # print(massage.decode())

def main():
    # while True:
    #Recebe a mensagem do cliente
    global nickname
    while True:
        # Recebe o nickname do cliente
        nickname = input("Type your nickname: ")
        # Verifica se o nickname é menor do que 64 bytes
        if len(nickname.encode()) > 64:
            print("Nickname too long")
        # Verifica se o nickname é vazio
        elif len(nickname.encode()) < 1:
            print("Nickname too short")
        else:
            break
    try:
        #Declaração das threads utilizadas para enviar e receber mensagens
        enviarThread = threading.Thread(target=mensageSend, args=(ip, port))
        # receberThread = threading.Thread(target=mensageReceive, args=(ip_cliente, port_cliente, ))

        #Criamos uma thread para enviar e receber as mensagens
        enviarThread.start()
        # receberThread.start()
    except:
        #Retornamos uma mensagem de erro caso não seja possível criar a thread
        print("ERRO: Erro ao criar thread!")

main()

