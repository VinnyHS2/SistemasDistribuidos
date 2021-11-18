'''
    # RPC Cliente #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 15/11/2021
    # Data de modificação: 18/11/2021
    # Descrição: Implementação de um serviço de gerenciamento de notas que deve enviar informações via gRPC:
            - LISTAR_ALUNOS (1): Tenta listar os alunos de uma disciplina com base no código da disciplina, ano e semestre.
            - ALTERAR_NOTA (2): Tenta alterar a nota de um aluno em uma disciplina com base no código do aluno, código da disciplina, ano e semestre.
            - ALTERAR_FALTAS (3): Tenta alterar a quantidade de faltas de um aluno com base no código do aluno, código da disciplina, ano e semestre.
            - LISTAR_DISCIPLINAS_CURSO (4): Tenta listar as disciplinas de um curso com base no código do curso.
            - LISTAR_DISCIPLINAS_ALUNO (5): Tenta listar os alunos de uma disciplina com base no ra, ano e semestre.
            - INSERIR_MATRICULA (6): Tenta inserir uma nova matrícula de um aluno em uma disciplina.

'''

import grpc

import gerenciamentoNotas_pb2_grpc
import gerenciamentoNotas_pb2

channel = grpc.insecure_channel('localhost:7778')
stub = gerenciamentoNotas_pb2_grpc.GerenciadorDeNotasStub(channel)

# Constantes para o tipo de requisição
LISTAR_ALUNOS = "1"
ALTERAR_NOTA = "2"
ALTERAR_FALTAS = "3"
LISTAR_DISCIPLINAS_CURSO = "4"
LISTAR_DISCIPLINAS_ALUNO = "5"
INSERIR_MATRICULA = "6"


# Função para receber os dados da requisição do cliente e enviá los para o servidor
def dadosRequisicao(opcao):
    if opcao == LISTAR_ALUNOS:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.ListarAlunosRequest()
        # Recebe os dados da requisição
        codigoDisciplina = (input("Digite o código da disciplina: "))
        ano = input("Digite o ano: ")
        semestre = input("Digite o semestre: ")
        # Verifica se os dados da requisição são válidos
        if ano.isdigit() and semestre.isdigit() and codigoDisciplina != "" and ano != "" and semestre != "":
            request.codigoDisciplina = codigoDisciplina
            request.ano = int(ano)
            request.semestre = int(semestre)
            # Envia os dados da requisição para o servidor e recebe a resposta
            response = stub.ListarAlunos(request)
            # Verifica se a requisição foi bem sucedida
            if response.mensagem != "":
                # Imprime os dados da resposta
                print(response.mensagem)
            else:
                # Imprime os dados da resposta
                for aluno in response.alunos:
                    print(aluno, end="")
                    print("===========================")
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == ALTERAR_NOTA:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.AlterarNotaRequest()
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
            # Envia os dados da requisição para o servidor e recebe a resposta
            response = stub.AlterarNota(request)
            # Verifica se a requisição foi bem sucedida
            if response.mensagem != "":
                # Imprime os dados da resposta
                print(response.mensagem)
            else:
                # Imprime os dados da resposta
                print("Ra: " + str(response.ra) + "\nCodigo da Disciplina:" + str(response.codigoDisciplina) + "\nAno: " + str(response.ano) + "\nSemestre: " + str(response.semestre) + "\nNota: " + str(response.nota))
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == ALTERAR_FALTAS:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.AlterarFaltasRequest()
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
            # Envia os dados da requisição para o servidor e recebe a resposta
            response = stub.AlterarFaltas(request)
            # Verifica se a requisição foi bem sucedida
            if response.mensagem != "":
                print(response.mensagem)
            else:
                print("Ra: " + str(response.ra) + "\nCodigo da Disciplina:" + str(response.codigoDisciplina) + "\nAno: " + str(response.ano) + "\nSemestre: " + str(response.semestre) + "\nFaltas: " + str(response.faltas))
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == LISTAR_DISCIPLINAS_CURSO:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.ListarDisciplinasCursoRequest()
        # Recebe os dados da requisição
        codigoCurso = input("Digite o código do curso: ")
        # Verifica se os dados da requisição são válidos
        if codigoCurso.isdigit() and codigoCurso != "":
            request.codigoCurso = int(codigoCurso)
            # Envia os dados da requisição para o servidor e recebe a resposta
            response = stub.ListarDisciplinasCurso(request)
            # Verifica se a requisição foi bem sucedida
            if response.mensagem != "":
                print(response.mensagem)
            else:
                # Imprime os dados da resposta
                for i in range(len(response.disciplinas)):
                    print("Código da Disciplina: " + str(response.disciplinas[i].codigoDisciplina) + "\nNome: " + str(response.disciplinas[i].nome) + "\nProfessor: " + str(response.disciplinas[i].professor))
                    print("===========================")
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == LISTAR_DISCIPLINAS_ALUNO:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.ListarDisciplinasAlunoRequest()
        # Recebe os dados da requisição
        ra = input("Digite o RA do aluno: ")
        ano = input("Digite o ano: ")
        semestre = input("Digite o semestre: ")
        # Verifica se os dados da requisição são válidos
        if ra.isdigit() and ano.isdigit() and semestre.isdigit() and ra != '' and ano != '' and semestre != '':
            request.ra = int(ra)
            request.ano = int(ano)
            request.semestre = int(semestre)
            # Envia os dados da requisição para o servidor e recebe a resposta
            response = stub.ListarDisciplinasAluno(request)
            # Verifica se a requisição foi bem sucedida
            if response.mensagem != "":
                print(response.mensagem)
            else:
                # Imprime os dados da resposta
                for i in range(len(response.disciplinas)):
                        print("Ra: " + str(response.disciplinas[i].ra) + "\nCódigo da Disciplina: " + str(response.disciplinas[i].codigoDisciplina) + "\nNota: " + str(response.disciplinas[i].nota) + "\nFaltas: " + str(response.disciplinas[i].faltas))
                        print("===========================")
        else:
            print("Algum dos campos não foi preenchido corretamente")

    elif opcao == INSERIR_MATRICULA:
        # Variável para armazenar os dados da requisição
        request = gerenciamentoNotas_pb2.InserirMatriculaRequest()
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
            # Envia os dados da requisição para o servidor e recebe a resposta
            response = stub.InserirMatricula(request)
            # Verifica se a requisição foi bem sucedida
            if response.mensagem != "":
                print(response.mensagem)
            else:
                print("Ra: " + str(response.matricula.ra) + "\nCodigo da Disciplina:" + str(response.matricula.codigoDisciplina) + "\nAno: " + str(response.matricula.ano) + "\nSemestre: " + str(response.matricula.semestre))
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
