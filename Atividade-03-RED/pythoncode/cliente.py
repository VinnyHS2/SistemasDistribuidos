'''
    # Representação Externa de Dados Cliente #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 03/10/2021
    # Data de modificação: 12/11/2021
    # Descrição: Implementação de um serviço de gerenciamento de notas que deve enviar informações via TCP:
            - LISTAR_ALUNOS (1): Tenta listar os alunos de uma disciplina com base no código da disciplina, ano e semestre.
            - ALTERAR_NOTA (2): Tenta alterar a nota de um aluno em uma disciplina com base no código do aluno, código da disciplina, ano e semestre.
            - ALTERAR_FALTAS (3): Tenta alterar a quantidade de faltas de um aluno com base no código do aluno, código da disciplina, ano e semestre.
            - LISTAR_DISCIPLINAS_CURSO (4): Tenta listar as disciplinas de um curso com base no código do curso.
            - LISTAR_DISCIPLINAS_ALUNO (5): Tenta listar os alunos de uma disciplina com base no ra, ano e semestre.
            - INSERIR_MATRICULA (6): Tenta inserir uma nova matrícula de um aluno em uma disciplina.

'''

import socket
import gerenciamentoNotas_pb2
# Cria um socket TCP
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor
clientsocket.connect(("localhost", 7000))
# Constantes para o tipo de requisição
LISTAR_ALUNOS = "1"
ALTERAR_NOTA = "2"
ALTERAR_FALTAS = "3"
LISTAR_DISCIPLINAS_CURSO = "4"
LISTAR_DISCIPLINAS_ALUNO = "5"
INSERIR_MATRICULA = "6"

# Função para enviar os dados da requisição
def enviaRequest(opcao, mensagem, size):
    enviaRequestType(opcao)
    clientsocket.send((str(size) + "\n").encode())
    clientsocket.send(mensagem)

# Função para enviar o tipo de requisição
def enviaRequestType(opcao):
    # Variável para armazenar o tipo de requisição
    requestType = gerenciamentoNotas_pb2.requestType()
    # Atribui o valor da opção ao tipo de requisição
    requestType.type = int(opcao)
    # marshalling do tipo de requisição
    msg = requestType.SerializeToString()
    # Variavel que armazena o tamanho da mensagem
    size = len(msg)
    # Envia o tamanho da mensagem
    clientsocket.send((str(size) + "\n").encode())
    # Envia a mensagem
    clientsocket.send(msg)

# Função para receber os dados da requisição do cliente e enviá los para o servidor
def dadosRequisicao(opcao):
    if opcao == LISTAR_ALUNOS:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.listarAlunosRequest()
        # Recebe os dados da requisição
        codigoDisciplina = (input("Digite o código da disciplina: "))
        ano = input("Digite o ano: ")
        semestre = input("Digite o semestre: ")
        # Verifica se os dados da requisição são válidos
        if ano.isdigit() and semestre.isdigit() and codigoDisciplina != "" and ano != "" and semestre != "":
            request.codigoDisciplina = codigoDisciplina
            request.ano = int(ano)
            request.semestre = int(semestre)
            # Envia os dados da requisição para o servidor
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = ''
            # Recebe o tamanho da mensagem
            while True:
                size += clientsocket.recv(1).decode()
                if size.endswith('\n'):
                    break
            size = int(size)
            # Recebe a mensagem
            response = clientsocket.recv(size)
            # Unmarshalling da mensagem
            responseParsed = gerenciamentoNotas_pb2.listarAlunosResponse()
            responseParsed.ParseFromString(response)
            # Verifica se a requisição foi bem sucedida
            if responseParsed.mensagem != "":
                # Imprime os dados da resposta
                print(responseParsed.mensagem)
            else:
                # Imprime os dados da resposta
                for aluno in responseParsed.alunos:
                    print(aluno, end="")
                    print("===========================")
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == ALTERAR_NOTA:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.alterarNotaRequest()
        # Recebe os dados da requisição
        ra = input("Digite o RA do aluno: ")
        codigoDisciplina = input("Digite o código da disciplina: ")
        ano = input("Digite o ano da disciplina: ")
        semestre = input("Digite o semestre da disciplina: ")
        nota = input("Digite a nota do aluno: ")
        # Verifica se os dados da requisição são válidos
        if ra.isdigit() and ano.isdigit() and semestre.isdigit() and nota.isdigit() and codigoDisciplina != "" and ano != "" and semestre != "" and nota != "" and ra != "":
            request.ra = int(ra)
            request.codigoDisciplina = codigoDisciplina
            request.ano = int(ano)
            request.semestre = int(semestre)
            request.nota = float(nota)
            # Envia os dados da requisição para o servidor
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = ''
            # Recebe o tamanho da mensagem
            while True:
                size += clientsocket.recv(1).decode()
                if size.endswith('\n'):
                    break
            size = int(size)
            # Recebe a mensagem
            response = clientsocket.recv(size)
            # Unmarshalling da mensagem
            responseParsed = gerenciamentoNotas_pb2.alterarNotaResponse()
            responseParsed.ParseFromString(response)
            # Verifica se a requisição foi bem sucedida
            if responseParsed.mensagem != "":
                # Imprime os dados da resposta
                print(responseParsed.mensagem)
            else:
                # Imprime os dados da resposta
                print("Ra: " + str(responseParsed.ra) + "\nCodigo da Disciplina:" + str(responseParsed.codigoDisciplina) + "\nAno: " + str(responseParsed.ano) + "\nSemestre: " + str(responseParsed.semestre) + "\nNota: " + str(responseParsed.nota))
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == ALTERAR_FALTAS:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.alterarFaltasRequest()
        # Recebe os dados da requisição
        ra = input("Digite o RA do aluno: ")
        codigoDisciplina = input("Digite o código da disciplina: ")
        ano = input("Digite o ano da disciplina: ")
        semestre = input("Digite o semestre da disciplina: ")
        faltas = input("Digite a quantidade de faltas do aluno: ")
        # Verifica se os dados da requisição são válidos
        if ra != '' and codigoDisciplina != '' and ano != '' and semestre != '' and faltas != '' and ra.isdigit() and ano.isdigit() and semestre.isdigit() and faltas.isdigit():
            request.ra = int(ra)
            request.codigoDisciplina = codigoDisciplina
            request.ano = int(ano)
            request.semestre = int(semestre)
            request.faltas = int(faltas)
            # Envia os dados da requisição para o servidor
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = ''
            # Recebe o tamanho da mensagem
            while True:
                size += clientsocket.recv(1).decode()
                if size.endswith('\n'):
                    break
            size = int(size)
            # Recebe a mensagem
            response = clientsocket.recv(size)
            # Unmarshalling da mensagem
            responseParsed = gerenciamentoNotas_pb2.alterarFaltasResponse()
            responseParsed.ParseFromString(response)
            # Verifica se a requisição foi bem sucedida
            if responseParsed.mensagem != "":
                print(responseParsed.mensagem)
            else:
                print("Ra: " + str(responseParsed.ra) + "\nCodigo da Disciplina:" + str(responseParsed.codigoDisciplina) + "\nAno: " + str(responseParsed.ano) + "\nSemestre: " + str(responseParsed.semestre) + "\nFaltas: " + str(responseParsed.faltas))
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == LISTAR_DISCIPLINAS_CURSO:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.listarDisciplinasCursoRequest()
        # Recebe os dados da requisição
        codigoCurso = input("Digite o código do curso: ")
        # Verifica se os dados da requisição são válidos
        if codigoCurso.isdigit() and codigoCurso != "":
            request.codigoCurso = int(codigoCurso)
            # Envia os dados da requisição para o servidor
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = ''
            # Recebe o tamanho da mensagem
            while True:
                size += clientsocket.recv(1).decode()
                if size.endswith('\n'):
                    break
            size = int(size)
            # Recebe a mensagem
            response = clientsocket.recv(size)  
            # Unmarshalling da mensagem
            responseParsed = gerenciamentoNotas_pb2.listarDisciplinasCursoResponse()
            responseParsed.ParseFromString(response)
            # Verifica se a requisição foi bem sucedida
            if responseParsed.mensagem != "":
                print(responseParsed.mensagem)
            else:
                # Imprime os dados da resposta
                for i in range(len(responseParsed.disciplinas)):
                    print("Código da Disciplina: " + str(responseParsed.disciplinas[i].codigoDisciplina) + "\nNome: " + str(responseParsed.disciplinas[i].nome) + "\nProfessor: " + str(responseParsed.disciplinas[i].professor))
                    print("===========================")
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == LISTAR_DISCIPLINAS_ALUNO:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.listarDisciplinasAlunoRequest()
        # Recebe os dados da requisição
        ra = input("Digite o RA do aluno: ")
        ano = input("Digite o ano: ")
        semestre = input("Digite o semestre: ")
        # Verifica se os dados da requisição são válidos
        if ra.isdigit() and ano.isdigit() and semestre.isdigit() and ra != '' and ano != '' and semestre != '':
            request.ra = int(ra)
            request.ano = int(ano)
            request.semestre = int(semestre)
            # Envia os dados da requisição para o servidor
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = ''
            # Recebe o tamanho da mensagem
            while True:
                size += clientsocket.recv(1).decode()
                if size.endswith('\n'):
                    break
            size = int(size)
            # Recebe a mensagem
            response = clientsocket.recv(size)
            # Unmarshalling da mensagem
            responseParsed = gerenciamentoNotas_pb2.listarDisciplinasAlunoResponse()
            responseParsed.ParseFromString(response)
            # Verifica se a requisição foi bem sucedida
            if responseParsed.mensagem != "":
                print(responseParsed.mensagem)
            else:
                # Imprime os dados da resposta
                for i in range(len(responseParsed.disciplinas)):
                        print("Ra: " + str(responseParsed.disciplinas[i].ra) + "\nCódigo da Disciplina: " + str(responseParsed.disciplinas[i].codigoDisciplina) + "\nNota: " + str(responseParsed.disciplinas[i].nota) + "\nFaltas: " + str(responseParsed.disciplinas[i].faltas))
                        print("===========================")
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == INSERIR_MATRICULA:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.inserirMatriculaRequest()
        # Recebe os dados da requisição
        ra = input("Digite o código do aluno: ")
        codigoDisciplina = input("Digite o código da disciplina: ")
        ano = input("Digite o ano da disciplina: ")
        semestre = input("Digite o semestre da disciplina: ")
        # Verifica se os dados da requisição são válidos
        if ra.isdigit() and ano.isdigit() and semestre.isdigit() and codigoDisciplina != "" and ano != "" and semestre != "" and ra != "":
            request.matricula.ra = int(ra)
            request.matricula.codigoDisciplina = codigoDisciplina
            request.matricula.ano = int(ano)
            request.matricula.semestre = int(semestre)
            # Envia os dados da requisição para o servidor
            enviaRequest(opcao, request.SerializeToString(), len(request.SerializeToString()))
            size = ''
            # Recebe o tamanho da mensagem
            while True:
                size += clientsocket.recv(1).decode()
                if size.endswith('\n'):
                    break
            size = int(size)
            # Recebe a mensagem
            response = clientsocket.recv(size)
            # Unmarshalling da mensagem
            responseParsed = gerenciamentoNotas_pb2.inserirMatriculaResponse()
            responseParsed.ParseFromString(response)
            # Verifica se a requisição foi bem sucedida
            if responseParsed.mensagem:
                print(responseParsed.mensagem)
            else:
                print("Ra: " + str(responseParsed.matricula.ra) + "\nCodigo da Disciplina:" + str(responseParsed.matricula.codigoDisciplina) + "\nAno: " + str(responseParsed.matricula.ano) + "\nSemestre: " + str(responseParsed.matricula.semestre))
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
    # Recebe a opção do usuário
    while True:
        opcao = input("Digite a opção desejada: ")
        # Verifica se a opção é válida
        if(opcao.isdigit()):
            dadosRequisicao(opcao)
        else:
            print("Opção inválida")

main()
