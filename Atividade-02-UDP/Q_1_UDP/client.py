'''
    # Questão 2 - UDP CLIENT #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 23/10/2021
    # Data de modificação: 27/10/2021
    # Descrição: O programa é um chat P2P, no qual 2 clientes se conectam via socket e enviam mensagem entre si.
    As mensagem enviadas serão enviadas com um cabeçalho seguindo o seguinte formato:
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |               Tipo de mensagem: 1 byte                |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |               Tamanho do apelido: 1 byte              |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |               Apelido: 1 - 64 bytes                   |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |               Tamanho da mensagem: 1 byte             |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |               Conteúdo da Mensagem: 0 - 255 byte      |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''

import socket
import sys
import emoji
import re
from emoji.core import emoji_count
import threading

ip = "127.0.0.1"
ports = [9898, 8989]

#Cria um socket do tipo TCP os parametros AF_INET e SOCK_DGRAM definem
#qual a familia de endereços será utilizada e qual o tipo de socket
socketClientReceive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClientSend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# #Permite o reuso de endereços ips
# socketClient.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  
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
def mensageReceive(ip, port):
    # 
    socketClientReceive.bind((ip, int(port)))
    while True:
        # Recebe a mensagem do chat
        mensage, ipAddress = socketClientReceive.recvfrom(322)
        print('')
        # Atribui o tipo de mensagem para a variável mensageType
        mensageType = int(mensage[0])
        # Atribui o tamanho do nickname para a variável nickSize
        nickSize = int(mensage[1])
        # Atribui o nick do cliente para a variável nick
        nick = mensage[2:nickSize+2].decode()
        # Atribui o tamanho da mensagem para a variável mensageSize
        mensageSize = mensage[nickSize+2]
        mensagePosition = int(nickSize + 3)
        # Atribui a mensagem para a variável mensageContent
        mensageContent = mensage[mensagePosition : (mensagePosition + mensageSize)].decode()
        # Verifica se a mensagem é do tipo ECHO
        if mensageType == 4:
            mensageType = 1
            # Formata a mensagem para reenviar
            mensage = (mensageType.to_bytes(1,'big') + nickSize.to_bytes(1,'big') + nick.encode() + mensageSize.to_bytes(1,'big') + mensageContent.encode())
            # Envia a mensagem
            socketClientReceive.sendto(mensage, ipAddress)
        # Verifica se a mensagem possui emojis
        elif mensageType == 3:
            print(nick + ' has sent a link: ' + mensageContent)
        # Verifica se a mensagem é uma url
        elif mensageType == 2:
            print(nick + ' said: ' + emoji.emojize(mensageContent))
        # Verifica se a mensagem é do tipo normal
        else:
            print(nick + ' said: ' + mensageContent)
# Função para enviar mensagens
def mensageSend(ip, port):
    addr = ip, port
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
            # Formata a mensagem para enviar
            mensage = (mensageType.to_bytes(1,'big') + nicknameSize.to_bytes(1,'big') + nickname.encode() + mensageSize.to_bytes(1,'big') + mensage.encode())
            # Envia a mensagem
            socketClientSend.sendto(mensage, addr)

def main():
    
    idx = sys.argv[1]

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
        # Cria um thread para receber mensagens do chat e enviar mensagens
        # Verifica se o id do cliente é 1
        if(idx == "1"):
            print("You are connected to the chat")
            threading.Thread(target=mensageReceive, args=(ip, ports[1])).start()
            threading.Thread(target=mensageSend, args=(ip, ports[0])).start()
        # Verifica se o id do cliente é 2
        elif(idx == "2"):
            print("You are connected to the chat2")
            threading.Thread(target=mensageReceive, args=(ip, ports[0])).start()
            threading.Thread(target=mensageSend, args=(ip, ports[1])).start()

    except:
        #Retornamos uma mensagem de erro caso não seja possível criar a thread
        print("ERRO: Erro ao criar thread!")

main()
