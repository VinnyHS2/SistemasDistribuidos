import socket
import gerenciamentoNotas_pb2
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost", 7000))
LISTAR_ALUNOS = "1"
ALTERAR_NOTA = "2"
ALTERAR_FALTAS = "3"
LISTAR_DISCIPLINAS_CURSO = "4"
LISTAR_DISCIPLINAS_ALUNO = "5"
INSERIR_MATRICULA = "6"

def enviaRequest(opcao, mensagem, size):
    enviaRequestType(opcao)
    clientsocket.send((str(size) + "\n").encode())
    clientsocket.send(mensagem)

def enviaRequestType(opcao):
    requestType = gerenciamentoNotas_pb2.requestType()
    requestType.type = int(opcao)
    # marshalling
    msg = requestType.SerializeToString()
    size = len(msg)
    clientsocket.send((str(size) + "\n").encode())
    clientsocket.send(msg)

def dadosRequisicao(opcao):
    if opcao == LISTAR_ALUNOS:
        request = gerenciamentoNotas_pb2.listarAlunosRequest()
        codigoDisciplina = (input("Digite o código da disciplina: "))
        ano = input("Digite o ano: ")
        semestre = input("Digite o semestre: ")
        if ano.isdigit() and semestre.isdigit() and codigoDisciplina != "" and ano != "" and semestre != "":
            request.codigoDisciplina = codigoDisciplina
            request.ano = int(ano)
            request.semestre = int(semestre)
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = clientsocket.recv(1024)
            size = int(size.decode())
            response = clientsocket.recv(size).decode()
            print('\n=========================\n',
                  response, '\n=========================\n')
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == ALTERAR_NOTA:
        request = gerenciamentoNotas_pb2.alterarNotaRequest()
        ra = input("Digite o RA do aluno: ")
        codigoDisciplina = input("Digite o código da disciplina: ")
        ano = input("Digite o ano da disciplina: ")
        semestre = input("Digite o semestre da disciplina: ")
        nota = input("Digite a nota do aluno: ")
        if ra.isdigit() and ano.isdigit() and semestre.isdigit() and nota.isdigit() and codigoDisciplina != "" and ano != "" and semestre != "" and nota != "" and ra != "":
            request.ra = int(ra)
            request.codigoDisciplina = codigoDisciplina
            request.ano = int(ano)
            request.semestre = int(semestre)
            request.nota = float(nota)
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = clientsocket.recv(1024)
            print(size)
            size = int(size.decode())
            response = clientsocket.recv(size).decode()
            print('\n=========================\n',
                  response, '\n=========================\n')
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == ALTERAR_FALTAS:
        request = gerenciamentoNotas_pb2.alterarFaltasRequest()
        ra = input("Digite o RA do aluno: ")
        codigoDisciplina = input("Digite o código da disciplina: ")
        ano = input("Digite o ano da disciplina: ")
        semestre = input("Digite o semestre da disciplina: ")
        faltas = input("Digite a quantidade de faltas do aluno: ")
        if ra != '' and codigoDisciplina != '' and ano != '' and semestre != '' and faltas != '' and ra.isdigit() and ano.isdigit() and semestre.isdigit() and faltas.isdigit():
            request.ra = int(ra)
            request.codigoDisciplina = codigoDisciplina
            request.ano = int(ano)
            request.semestre = int(semestre)
            request.faltas = int(faltas)
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = clientsocket.recv(4)
            print(size)
            size = int(size.decode())
            response = clientsocket.recv(size).decode()
            print('\n=========================\n',
                  response, '\n=========================\n')
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == LISTAR_DISCIPLINAS_CURSO:
        request = gerenciamentoNotas_pb2.listarDisciplinasCursoRequest()
        codigoCurso = input("Digite o código do curso: ")
        if codigoCurso.isdigit() and codigoCurso != "":
            request.codigoCurso = int(codigoCurso)
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = clientsocket.recv(1024)
            size = int(size.decode())
            response = clientsocket.recv(size).decode()
            print('\n=========================\n',
                  response, '\n=========================\n')
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == LISTAR_DISCIPLINAS_ALUNO:
        request = gerenciamentoNotas_pb2.listarDisciplinasAlunoRequest()
        ra = input("Digite o código do aluno: ")
        ano = input("Digite o ano: ")
        semestre = input("Digite o semestre: ")
        if ra.isdigit() and ano.isdigit() and semestre.isdigit() and ra != '' and ano != '' and semestre != '':
            request.ra = int(ra)
            request.ano = int(ano)
            request.semestre = int(semestre)
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = clientsocket.recv(1024)
            size = int(size.decode())
            response = clientsocket.recv(size).decode()
            print('\n=========================\n',
                  response, '\n=========================\n')
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == INSERIR_MATRICULA:
        request = gerenciamentoNotas_pb2.inserirMatriculaRequest()
        ra = input("Digite o código do aluno: ")
        codigoDisciplina = input("Digite o código da disciplina: ")
        ano = input("Digite o ano da disciplina: ")
        semestre = input("Digite o semestre da disciplina: ")
        if ra.isdigit() and ano.isdigit() and semestre.isdigit() and codigoDisciplina != "" and ano != "" and semestre != "" and ra != "":
            request.matricula.ra = int(ra)
            request.matricula.codigoDisciplina = codigoDisciplina
            request.matricula.ano = int(ano)
            request.matricula.semestre = int(semestre)
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = clientsocket.recv(1024)
            size = int(size.decode())
            response = clientsocket.recv(size).decode()
            print('\n=========================\n',
                  response, '\n=========================\n')
        else:
            print("Algum dos campos não foi preenchido corretamente")
    else:
        print("Opção inválida")

def main():
    print("1 - Listar Alunos")
    print("2 - Alterar Nota")
    print("3 - Alterar Faltas")
    print("4 - Listar Disciplinas do Curso")
    print("5 - Listar Disciplinas do Aluno")
    print("6 - Inserir Matricula")
    while True:
        opcao = input("Digite a opção desejada: ")
        if(opcao.isdigit()):
            dadosRequisicao(opcao)
        else:
            print("Opção inválida")

main()