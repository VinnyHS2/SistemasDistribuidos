/*
    # Representação Externa de Dados Servidor #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 03/10/2021
    # Data de modificação: 12/11/2021
    # Descrição: Implementação de um serviço de gerenciamento de notas que deve receber informações via TCP:
            - LISTAR_ALUNOS: Tenta listar os alunos de uma disciplina com base no código da disciplina, ano e semestre.
            - ALTERAR_NOTA: Tenta alterar a nota de um aluno em uma disciplina com base no código do aluno, código da disciplina, ano e semestre.
            - ALTERAR_FALTAS: Tenta alterar a quantidade de faltas de um aluno com base no código do aluno, código da disciplina, ano e semestre.
            - LISTAR_DISCIPLINAS_CURSO: Tenta listar as disciplinas de um curso com base no código do curso.
            - LISTAR_DISCIPLINAS_ALUNO: Tenta listar os alunos de uma disciplina com base no ra, ano e semestre.
            - INSERIR_MATRICULA: Tenta inserir uma nova matrícula de um aluno em uma disciplina.

*/
import java.io.*;
import java.net.*;
import java.sql.*;

public class servidor {
    static final int LISTAR_ALUNOS = 1;
    static final int ALTERAR_NOTA = 2;
    static final int ALTERAR_FALTAS = 3;
    static final int LISTAR_DISCIPLINAS_CURSO = 4;
    static final int LISTAR_DISCIPLINAS_ALUNO = 5;
    static final int INSERIR_MATRICULA = 6;
    
    public static Connection connect() {
        Connection conn = null;

        try {
            // db parameters
            String url = "jdbc:sqlite:../database_com_dados-contrib-Daniel-Farina.db";

            // create a connection to the database
            conn = DriverManager.getConnection(url);

            System.out.println("Conexão com o banco estabelecida com sucesso.");

        } catch (SQLException e) {
            // caso não consiga se conectar
            System.out.println(e.getMessage());
        }

        return conn;
    }

    // LISTA ALUNOS DE UMA DISCIPLINA
    public static GerenciamentoNotas.listarAlunosResponse listarAlunos(Connection connection, String codigoDisciplina, int ano, int semestre) {        
        GerenciamentoNotas.listarAlunosResponse.Builder response = GerenciamentoNotas.listarAlunosResponse.newBuilder();
        try{
            // cria um statement para realizar a consulta
            Statement statement = connection.createStatement();
            // busca todos os alunos matriculados na disciplina
            ResultSet rs = statement.executeQuery("SELECT a.* FROM matricula m INNER JOIN aluno a ON (a.ra = m.ra) WHERE '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // caso não encontre nenhum aluno
            if(!rs.isBeforeFirst()){
                response.setMensagem("Não há alunos matriculados nessa disciplina");
                return response.build();
            }
            // cria um objeto para a resposta
            while(rs.next()){
                int ra = rs.getInt("ra");
                String nome = rs.getString("nome");
                int periodo = rs.getInt("periodo");
                response.addAlunos(GerenciamentoNotas.listarAlunosResponse.Aluno.newBuilder().setNome(nome).setRa(ra).setPeriodo(periodo).build());
            }

        }
        // caso ocorra um erro
        catch(SQLException e){
            response.setMensagem(e.getMessage());
        }
        return response.build();
    }

    // ALTERA A NOTA DO ALUNO
    public static GerenciamentoNotas.alterarNotaResponse alterarNota(Connection connection, int ra, String codigoDisciplina, int ano, int semestre , float nota) {        
        GerenciamentoNotas.alterarNotaResponse.Builder response = GerenciamentoNotas.alterarNotaResponse.newBuilder();
        // tneta executar
        try{
            // cria um statement para realizar a consulta
            Statement statement = connection.createStatement();
            // verifica se o aluno está matriculado na disciplina
            ResultSet rs = statement.executeQuery("SELECT * FROM matricula WHERE ra = " + ra + " AND '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // caso não esteja matriculado
            if(!rs.isBeforeFirst()){
                response.setMensagem("O aluno não foi encontrado na disciplina informada");
                return response.build();
            }
            // atualiza a nota
            statement.execute("UPDATE matricula SET nota = " + nota + " WHERE ra =" + ra + " AND cod_disciplina = '" + String.valueOf(codigoDisciplina) + "' AND ano = " + ano + " AND semestre = " + semestre + ";");
            // busca novamente a nota para retornar o aluno com a nota atualizada
            rs = statement.executeQuery("SELECT * FROM matricula WHERE ra = " + ra + " AND '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // cria um objeto para a resposta
            response.setRa(rs.getInt("ra"));
            response.setAno(rs.getInt("ano"));
            response.setSemestre(rs.getInt("semestre"));
            response.setCodigoDisciplina(rs.getString("cod_disciplina"));
            response.setNota(rs.getFloat("nota"));
        }
        // caso ocorra um erro
        catch(SQLException e){
            response.setMensagem(e.getMessage());
        }
        return response.build();
    }

    // ALTERA AS FALTAS DO ALUNO
    public static GerenciamentoNotas.alterarFaltasResponse alterarFaltas(Connection connection, int ra, String codigoDisciplina, int ano, int semestre, int faltas) {        
        GerenciamentoNotas.alterarFaltasResponse.Builder response = GerenciamentoNotas.alterarFaltasResponse.newBuilder();
        // tenta executar
        try{
            // cria um statement para realizar a consulta
            Statement statement = connection.createStatement();
            // verificar se o aluno está matriculado na disciplina
            ResultSet rs = statement.executeQuery("SELECT * FROM matricula WHERE ra = " + ra + " AND '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // caso não esteja, retornar mensagem de erro
            if(!rs.isBeforeFirst()){
                response.setMensagem("O aluno não foi encontrado na disciplina informada");
                return response.build();
            }
            // atualiza as faltas
            statement.execute("UPDATE matricula SET faltas = " + faltas + " WHERE ra =" + ra + " AND cod_disciplina = '" + String.valueOf(codigoDisciplina) + "' AND ano = " + ano + " AND semestre = " + semestre + ";");
            // busca novamente a nota para retornar o aluno com as faltas atualizadas
            rs = statement.executeQuery("SELECT * FROM matricula WHERE ra = " + ra + " AND '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // cria o objeto response
            response.setRa(rs.getInt("ra"));
            response.setAno(rs.getInt("ano"));
            response.setSemestre(rs.getInt("semestre"));
            response.setCodigoDisciplina(rs.getString("cod_disciplina"));
            response.setFaltas(rs.getInt("faltas"));
        }
        // caso ocorra um erro
        catch(SQLException e){
            response.setMensagem(e.getMessage());
        }
        return response.build();
    }

    // LISTA AS DISCIPLINAS DE UM CURSO
    public static GerenciamentoNotas.listarDisciplinasCursoResponse listarDisciplinasCurso(Connection connection, int codigoCurso) {        
        // cria um builder para a resposta
        GerenciamentoNotas.listarDisciplinasCursoResponse.Builder response = GerenciamentoNotas.listarDisciplinasCursoResponse.newBuilder();
        try{
            // cria um statement
            Statement statement = connection.createStatement();
            // busca as disciplinas de um curso
            ResultSet rs = statement.executeQuery("SELECT * FROM disciplina WHERE " + String.valueOf(codigoCurso) + " = cod_curso;");
            // verificar se foi encontrado alguma disciplina
            if(!rs.isBeforeFirst()){
                response.setMensagem("Não foi encontrada nenhuma disciplina para o curso informado");
                return response.build();
            }
            // cria um objeto para a resposta
            while(rs.next()){
                String professor = rs.getString("professor");
                String nome = rs.getString("nome");
                String codigo = rs.getString("codigo");
                response.addDisciplinas(GerenciamentoNotas.listarDisciplinasCursoResponse.DisciplinaCurso.newBuilder().setNome(nome).setCodigoDisciplina(codigo).setProfessor(professor).build());
            }

        }
        // caso ocorra algum erro
        catch(SQLException e){
            response.setMensagem(e.getMessage());
        }
        // response.setAluno("a");
        return response.build();
    }

    // LISTA AS DISCIPLINAS DE UM ALUNO
    public static GerenciamentoNotas.listarDisciplinasAlunoResponse listarDisciplinasAluno(Connection connection, int ra, int ano, int semestre) {     
        // cria um builder para a resposta   
        GerenciamentoNotas.listarDisciplinasAlunoResponse.Builder response = GerenciamentoNotas.listarDisciplinasAlunoResponse.newBuilder();
        // tenta executar
        try{
            // cria um statement 
            Statement statement = connection.createStatement();
            // busca as disciplinas do aluno com base no ra e ano e semestre
            ResultSet rs = statement.executeQuery("SELECT * FROM matricula WHERE " + ra + " = ra AND " + ano + " = ano AND " + semestre + " = semestre;");
            // se não houver nenhum resultado
            if(!rs.isBeforeFirst()){
                // define a mensagem de erro
                response.setMensagem("O aluno informado não está cadastrado em nenhuma disciplina no ano e semetre informados");
                return response.build();
            }
            // cria um objeto para a resposta /* enfase na diferença entre add e set */
            while(rs.next()){
                String codigoDisciplinaResult = rs.getString("cod_disciplina");
                float nota = rs.getFloat("nota");
                int faltas = rs.getInt("faltas");
                response.addDisciplinas(GerenciamentoNotas.listarDisciplinasAlunoResponse.DisciplinaAlunos.newBuilder().setRa(ra).setCodigoDisciplina(codigoDisciplinaResult).setNota(nota).setFaltas(faltas).build());
            }

        }
        // caso ocorra algum erro, define a mensagem de erro
        catch(SQLException e){
            response.setMensagem(e.getMessage());
        }
        // response.setAluno("a");
        return response.build();
    }

    // INSERE UMA MATRICULA
    public static GerenciamentoNotas.inserirMatriculaResponse inserirMatricula(Connection connection, int ra,String codigoDisciplina, int ano, int semestre) {
        //cria um builder para a resposta 
        GerenciamentoNotas.inserirMatriculaResponse.Builder response = GerenciamentoNotas.inserirMatriculaResponse.newBuilder();
        // tenta executar
        try{
            // cria um statement
            Statement statement = connection.createStatement();
            // verifica se a disciplina existe
            ResultSet rs = statement.executeQuery("SELECT * FROM disciplina WHERE '" + String.valueOf(codigoDisciplina) + "' = codigo;");
            // caso não encontre a disciplina, retorna mensagem de erro
            if(!rs.isBeforeFirst()){
                // define a mensagem de erro
                response.setMensagem("A disciplina informada não existe");
                return response.build();
            }

            // verifica se o aluno existe
            rs = statement.executeQuery("SELECT * FROM aluno WHERE " + ra + " = ra;");
            // caso não exista, define a mensagem de erro
            if(!rs.isBeforeFirst()){
                // define a mensagem de erro
                response.setMensagem("O aluno informado não existe");
                return response.build();
            }

            // verifica se o aluno já está matriculado na disciplina
            rs = statement.executeQuery("SELECT * FROM matricula WHERE " + ra + " = ra AND '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // caso esteja matriculado, retorna mensagem de erro
            if(rs.isBeforeFirst()){
                // define a mensagem de erro
                response.setMensagem("O aluno já está matriculado nessa disciplina");
                return response.build();
            }

            // executa a inserção na tabela matricula
            statement.execute("INSERT INTO matricula (ra, cod_disciplina, ano, semestre, nota, faltas) VALUES (" + ra + ", '" + String.valueOf(codigoDisciplina) + "', " + ano + ", " + semestre + ", 0, 0);");
            // executa a query para verificar se a matricula foi inserida
            rs = statement.executeQuery("SELECT * FROM matricula WHERE " + ra + " = ra AND '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // verifica se a resposta é vazia
            if(!rs.isBeforeFirst()){
                // define a mensagem de erro
                response.setMensagem("Não foi possível realizar a matrícula");
                return response.build();
            }
            // cria o objeto de resposta
            while(rs.next()){
                int raResult = rs.getInt("ra");
                int anoResult = rs.getInt("ano");
                int semestreResult = rs.getInt("semestre");
                String codigoDisciplinaResult = rs.getString("cod_disciplina");
                float notaResult = rs.getFloat("nota");
                int faltasResult = rs.getInt("faltas");
                response.setMatricula(GerenciamentoNotas.Matricula.newBuilder().setRa(raResult).setAno(anoResult).setSemestre(semestreResult).setCodigoDisciplina(codigoDisciplinaResult).setNota(notaResult).setFaltas(faltasResult).build());
            }

        }
        // caso ocorra algum erro, define a mensagem de erro
        catch(SQLException e){
            // mostrar a mensagem de erro
            response.setMensagem(e.getMessage());
        }
        return response.build();
    }

    public static void main(String args[]) {
        // cria conexão com o banco de dados
        Connection conn = connect();
        // tenta executar 
        try {
            // define a porta do servidor
            int serverPort = 7000;
            // Cria um socket do tipo SERVER
            ServerSocket listenSocket = new ServerSocket(serverPort);
            // Váriveis para o recebimento de mensagens
            String valueStr;
            int sizeBuffer;
            byte[] buffer;

            // Váriaveis para o envio de mensagens
            byte[] msg;
            String responseSize;
            byte[] size;
            // aceita conexão com o socket nas portas definidas anteriormente
            Socket clientSocket = listenSocket.accept();
            // cria uma coneção com o client para receber mensagens do cliente 
            DataInputStream inClient = new DataInputStream(clientSocket.getInputStream());
            // cria uma coneção com o client para enviar mensagens para o cliente 
            DataOutputStream outClient = new DataOutputStream(clientSocket.getOutputStream());
            while (true) {
                // recebe o tamanho do buffer
                valueStr = inClient.readLine();
                // converte o tamanho do buffer para inteiro
                sizeBuffer = Integer.valueOf(valueStr);
                // cria o buffer com o tamanho da mensagem
                buffer = new byte[sizeBuffer];
                // faz a leitura do buffer
                inClient.read(buffer);

                // realiza o unmarshalling
                GerenciamentoNotas.requestType type = GerenciamentoNotas.requestType.parseFrom(buffer);

                // recebe o tamanho do buffer
                valueStr = inClient.readLine();
                // converte o tamanho do buffer para inteiro
                sizeBuffer = Integer.valueOf(valueStr);
                // cria o buffer com o tamanho da mensagem
                buffer = new byte[sizeBuffer];
                // faz a leitura do buffer
                inClient.read(buffer);

                switch (type.getType()) {
                    case LISTAR_ALUNOS:
                        // recebe o request e faz o unmarshalling
                        GerenciamentoNotas.listarAlunosRequest request = GerenciamentoNotas.listarAlunosRequest.parseFrom(buffer);
                        // chama a função para listar os alunos
                        GerenciamentoNotas.listarAlunosResponse response = listarAlunos(conn, request.getCodigoDisciplina() , request.getAno(), request.getSemestre());
                        // converte o resultado da função para bytes
                        msg = response.toByteArray();
                        // obtem o tamanho do resultado e converte para string
                        responseSize = String.valueOf(msg.length) + "\n";
                        // envia o tamanho do resultado em bytes
                        outClient.write(responseSize.getBytes());
                        // envia o resultado em bytes
                        outClient.write(msg);
                        break;
                    case ALTERAR_NOTA:
                        // recebe o request e faz o unmarshalling
                        GerenciamentoNotas.alterarNotaRequest alterarNotaRequest = GerenciamentoNotas.alterarNotaRequest.parseFrom(buffer);
                        // chama a função que altera a nota de um aluno
                        GerenciamentoNotas.alterarNotaResponse alterarNotaResponse = alterarNota(conn, alterarNotaRequest.getRa(), alterarNotaRequest.getCodigoDisciplina(), alterarNotaRequest.getAno(), alterarNotaRequest.getSemestre(), alterarNotaRequest.getNota());
                        // converte o resultado da função para bytes
                        msg = alterarNotaResponse.toByteArray();
                        // obtem o tamanho do resultado e converte para string
                        responseSize = String.valueOf(msg.length) + "\n";
                        // envia o tamanho do resultado em bytes
                        outClient.write(responseSize.getBytes());
                        // envia o resultado em bytes
                        outClient.write(msg);
                        break;
                    case ALTERAR_FALTAS:
                        // recebe o request e faz o unmarshalling
                        GerenciamentoNotas.alterarFaltasRequest alterarFaltasRequest = GerenciamentoNotas.alterarFaltasRequest.parseFrom(buffer);
                        // chama a função que altera as faltas de um aluno
                        GerenciamentoNotas.alterarFaltasResponse alterarFaltasResponse = alterarFaltas(conn, alterarFaltasRequest.getRa(), alterarFaltasRequest.getCodigoDisciplina(), alterarFaltasRequest.getAno(), alterarFaltasRequest.getSemestre(), alterarFaltasRequest.getFaltas());
                        // converte o resultado da função para bytes
                        msg = alterarFaltasResponse.toByteArray();
                        // obtem o tamanho do resultado e converte para string
                        responseSize = String.valueOf(msg.length) + "\n";
                        // envia o tamanho do resultado em bytes
                        outClient.write(responseSize.getBytes());
                        // envia o resultado em bytes
                        outClient.write(msg);
                        break;
                    case LISTAR_DISCIPLINAS_CURSO:
                        // recebe o request e faz o unmarshalling
                        GerenciamentoNotas.listarDisciplinasCursoRequest listarDisciplinasCursoRequest = GerenciamentoNotas.listarDisciplinasCursoRequest.parseFrom(buffer);
                        // chama a função que faz a listagem de disciplinas do curso
                        GerenciamentoNotas.listarDisciplinasCursoResponse listarDisciplinasCursoResponse = listarDisciplinasCurso(conn, listarDisciplinasCursoRequest.getCodigoCurso());
                        // converte o resultado da função para bytes
                        msg = listarDisciplinasCursoResponse.toByteArray();
                        // obtem o tamanho do resultado e converte para string
                        responseSize = String.valueOf(msg.length) + "\n";
                        // envia o tamanho do resultado em bytes
                        outClient.write(responseSize.getBytes());
                        // envia o resultado em bytes
                        outClient.write(msg);
                        break;
                    case LISTAR_DISCIPLINAS_ALUNO:
                        // recebe o request e faz o unmarshalling
                        GerenciamentoNotas.listarDisciplinasAlunoRequest listarDisciplinasAlunoRequest = GerenciamentoNotas.listarDisciplinasAlunoRequest.parseFrom(buffer);
                        // chama a função que faz a listagem de disciplinas do aluno
                        GerenciamentoNotas.listarDisciplinasAlunoResponse listarDisciplinasAlunoResponse = listarDisciplinasAluno(conn, listarDisciplinasAlunoRequest.getRa(), listarDisciplinasAlunoRequest.getAno(), listarDisciplinasAlunoRequest.getSemestre());
                        // converte o resultado da função para bytes
                        msg = listarDisciplinasAlunoResponse.toByteArray();
                        // obtem o tamanho do array de bytes e converte para string
                        responseSize = String.valueOf(msg.length) + "\n";
                        // envia o tamanho da resposta em bytes
                        outClient.write(responseSize.getBytes());
                        // envia a resposta em bytes
                        outClient.write(msg);
                        break;
                    case INSERIR_MATRICULA:
                        // recebe o request e faz o unmarshalling
                        GerenciamentoNotas.inserirMatriculaRequest inserirMatriculaRequest = GerenciamentoNotas.inserirMatriculaRequest.parseFrom(buffer);
                        // chama a função de inserir matrícula
                        GerenciamentoNotas.inserirMatriculaResponse inserirMatriculaResponse = inserirMatricula(conn, inserirMatriculaRequest.getMatricula().getRa(), inserirMatriculaRequest.getMatricula().getCodigoDisciplina(), inserirMatriculaRequest.getMatricula().getAno(), inserirMatriculaRequest.getMatricula().getSemestre());
                        // converte o resultado da função para bytes
                        msg = inserirMatriculaResponse.toByteArray();
                        // obtem o tamanho do array de bytes e converte para string
                        responseSize = String.valueOf(msg.length) + "\n";
                        // envia o tamanho da resposta em bytes
                        outClient.write(responseSize.getBytes());
                        // envia a resposta em bytes
                        outClient.write(msg);
                        break;
                    default:
                        // Tipo de requisição não encontrado
                        System.out.println("Nenhum tipo de requisição");
                        break;
                }
            } // while
        } catch (IOException e) {
            // Mostra o erro
            System.out.println("Listensocket:" + e.getMessage());
        } // catch
    }// main
}
// class