/*
    # RPC Servidor #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 03/10/2021
    # Data de modificação: 12/11/2021
    # Descrição: Implementação de um serviço de gerenciamento de notas que deve receber informações via gRPC:
            - LISTAR_ALUNOS: Tenta listar os alunos de uma disciplina com base no código da disciplina, ano e semestre.
            - ALTERAR_NOTA: Tenta alterar a nota de um aluno em uma disciplina com base no código do aluno, código da disciplina, ano e semestre.
            - ALTERAR_FALTAS: Tenta alterar a quantidade de faltas de um aluno com base no código do aluno, código da disciplina, ano e semestre.
            - LISTAR_DISCIPLINAS_CURSO: Tenta listar as disciplinas de um curso com base no código do curso.
            - LISTAR_DISCIPLINAS_ALUNO: Tenta listar os alunos de uma disciplina com base no ra, ano e semestre.
            - INSERIR_MATRICULA: Tenta inserir uma nova matrícula de um aluno em uma disciplina.

*/

import io.grpc.ServerBuilder;
import java.io.IOException;

/**
 *
 * @author Henrique Moura Bini e Vinicius Henrique Soares
 */
public class Server {
    public static void main(String[] args) {
            io.grpc.Server server = ServerBuilder
                    .forPort(7778)
                    .addService(new GerenciadorDeNotasImpl())
                    .build();
            
            
        try {
            server.start();
            System.out.println("Servidor iniciado.");
            server.awaitTermination();
        } catch (IOException | InterruptedException e) {
            System.err.println("Erro: " + e);
        }
        
    }
}
