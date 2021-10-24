'''
    # Questão 2 - UDP CLIENT #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 24/10/2021
    # Data de modificação: 24/10/2021
    # Descrição:
        Envia um arquivo para o servidor sem confirmação de resposta, 
        apenas fazendo envio de um checksum para o servidor confirmar
        que o arquivo foi enviado corretamente

    # cabeçalho requisição:
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |               TamanhoDoArquivo: 4 byte                |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |               Nome Do Arquivo: 1020 bytes             |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    - Para cada quantidade de envio:
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |               Arquivo em bytes: 1024 bytes            |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    - No ultimo envio é enviado o checksum do arquivo
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                   checksum: 1 byte                    |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

'''

import math
import socket
from tqdm import tqdm
import hashlib
import os
import tkinter
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from tkinter import filedialog
from os import environ

ip = "127.0.0.1"
port = 5973

#Variavel contendo o ip e a porta
addr = (ip, port)
#Cria um socket do tipo TCP os parametros AF_INET e SOCK_DGRAM definem
#qual a familia de endereços será utilizada e qual o tipo de socket
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Permite o reuso de endereços ips
socketClient.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  


#Variaveis globais para remover warnings da biblioteca PyQt5
environ["QT_DEVICE_PIXEL_RATIO"] = "0"
environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
environ["QT_SCREEN_SCALE_FACTORS"] = "1"
environ["QT_SCALE_FACTOR"] = "1"

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedSize(501, 153)

############################## Cria a tela ########################################
    def initUI(self):
        text = 'Selecione um arquivo'
        self.setWindowTitle('Atividade-UDP-Q-2')
        self.pbar = QProgressBar(self)
        self.label = QLabel(self)
        self.label.setText(text)
        self.label.setFont(QFont('Helvetica Neue', 11))

        self.input = QLineEdit(self)
        self.input.setPlaceholderText('Selecione um arquivo')
        self.input.setToolTip('Selecione um arquivo')

        button = QPushButton('Buscar', self)
        button.setToolTip('Clique para buscar o arquivo')
        button.clicked.connect(self.buscar)

        button2 = QPushButton('Enviar', self)
        button2.setToolTip('Clique para enviar o arquivo')
        # Chama o metodo para o envio do arquivo
        button2.clicked.connect(lambda: send(self.file, self.filename, self.pbar))

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.input, 2, 0)
        layout.addWidget(button, 2, 1)
        layout.addWidget(button2, 5, 0)
        layout.addWidget(self.pbar, 6, 0)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

######################################################

    # Função para buscar o arquivo
    def buscar(self):
        # Inicia o Tkinter
        searchFile = tkinter.Tk()
        # Abre a janela para escolher o arquivo
        origin = filedialog.askopenfilename()
        # Finaliza o Tkinter
        searchFile.destroy()
        # Altera o texto da interface para o caminho do arquivo
        self.input.setText(origin)
        # Salva o caminho do arquivo na variável
        self.file = origin
        # Salva o nome do arquivo
        self.filename = os.path.basename(origin)

def send(file, filename: str, pbar):
    # Calcula e converte 
    filesize = int.to_bytes((os.stat(file).st_size), 4, 'big')
    # Envia o cabeçado
    socketClient.sendto((filesize + filename.encode()), addr)
    # Calcula a quantidade de pacotes a ser enviado
    numberOfPackets = math.ceil((os.stat(file).st_size) / 1024)
    # Abre o arquivo
    fileOpened = open(file, 'rb')
    # Cria o checksum
    checksumLocal = hashlib.sha1(fileOpened.read()).hexdigest()
    # Volta para o começo do arquivo
    fileOpened.seek(0)
    # Enquanto houver pacotes, será impedido de continuar
    print('Tentando enviar')
    progressTotal = (1/numberOfPackets*100)
    progress = 0
    while(numberOfPackets > 0):
        # Lê o pacote
        data = fileOpened.read(1024)
        # Faz o envio do pacote para o servidor
        print(' ',end='')
        pbar.setValue(math.ceil(progress) + 1)
        progress += progressTotal
        socketClient.sendto(data, addr)
        
        # Iteração do número de pacotes
        numberOfPackets -= 1
    # Envia o checksum
    socketClient.sendto(checksumLocal.encode(), addr)
    # Fecha o Arquivo
    fileOpened.close()

def main():
    # Inicia a janela
    app = QApplication(sys.argv)
    window = Janela()
    window.show()
    app.exec_()


main()
