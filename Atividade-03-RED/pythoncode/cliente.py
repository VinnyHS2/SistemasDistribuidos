import socket
import gerenciamentoNotas_pb2
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost", 7000))
# instanciarepreencheraestrutura
# requestType = gerenciamentoNotas_pb2.requestType()
# requestType.type = 1
# # marshalling
# msg = requestType.SerializeToString()
# size = len(msg)
# clientsocket.send((str(size) + "\n").encode())
# clientsocket.send(msg)
# LISTAR_ALUNOS = 1
# ALTERAR_NOTA = 2
# ALTERAR_FALTAS = 3
# LISTAR_DISCIPLINAS_CURSO = 4
# LISTAR_DISCIPLINAS_ALUNO = 5
# INSERIR_MATRICULA = 6

def enviaDados(opcao):
    pass

def dadosRequisicao(opcao):
    requestType = gerenciamentoNotas_pb2.requestType()
    requestType.type = opcao
    # marshalling
    msg = requestType.SerializeToString()
    size = len(msg)
    clientsocket.send((str(size) + "\n").encode())
    clientsocket.send(msg)
    if opcao == 1:
        request = gerenciamentoNotas_pb2.listarAlunosRequest()
        request.codigoDisciplina = (input("Digite o código da disciplina: "))
        request.ano = int(input("Digite o ano: "))
        request.semestre = int(input("Digite o semestre: "))
        msg = request.SerializeToString()
        size = len(msg)
        clientsocket.send((str(size) + "\n").encode())
        clientsocket.send(msg)
        # clientsocket.send(msg.SerializeToString())
        # recebo a resposta
        size = int(clientsocket.recv(4).decode())
        response = clientsocket.recv(size).decode()
        # response = response.parseFromString(response)
        # mostro na tela
        print('\n=========================\n',
              response, '\n=========================\n')

    elif opcao == 2:
        request = gerenciamentoNotas_pb2.alterarNotaRequest()
        request.ra = int(input("Digite o RA do aluno: "))
        request.codigoDisciplina = input("Digite o código da disciplina: ")
        request.ano = int(input("Digite o ano da disciplina: "))
        request.periodo = int(input("Digite o periodo da disciplina: "))
        request.nota = float(input("Digite a nota do aluno: "))
        msg = request.SerializeToString()
        size = len(msg)
        clientsocket.send((str(size) + "\n").encode())
        clientsocket.send(msg)
        # clientsocket.send(msg.SerializeToString())
        # recebo a resposta
        size = int(clientsocket.recv(4).decode())
        response = gerenciamentoNotas_pb2.alterarNotaResponse()
        response = clientsocket.recv(size).decode()
        # response = response.parseFromString(response)
        # mostro na tela
        print('\n=========================\n',
              response, '\n=========================\n')

    elif opcao == 3:
        request = gerenciamentoNotas_pb2.alterarFaltasRequest()
        request.ra = int(input("Digite o RA do aluno: "))
        request.codigoDisciplina = input("Digite o código da disciplina: ")
        request.ano = int(input("Digite o ano da disciplina: "))
        request.periodo = int(input("Digite o periodo da disciplina: "))
        request.faltas = int(input("Digite a quantidade de faltas do aluno: "))
        msg = request.SerializeToString()
        size = len(msg)
        clientsocket.send((str(size) + "\n").encode())
        clientsocket.send(msg)
        # clientsocket.send(msg.SerializeToString())
        # recebo a resposta
        size = int(clientsocket.recv(4).decode())
        response = gerenciamentoNotas_pb2.alterarFaltasResponse()
        response = clientsocket.recv(size).decode()
        # response = response.parseFromString(response)
        # mostro na tela
        print('\n=========================\n',
              response, '\n=========================\n')

    elif opcao == 4:
        request = gerenciamentoNotas_pb2.listarDisciplinasCursoRequest()
        request.ra = int(input("Digite o código do curso: "))
        msg = request.SerializeToString()
        size = len(msg)
        clientsocket.send((str(size) + "\n").encode())
        clientsocket.send(msg)
        