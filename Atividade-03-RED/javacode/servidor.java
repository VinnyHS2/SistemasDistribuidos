import java.io.*;
import java.net.*;
import java.util.Arrays;
import java.util.Map;

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

            System.out.println("Connection to SQLite has been established.");

        } catch (SQLException e) {
            // caso não consiga se conectar
            System.out.println(e.getMessage());
        }

        return conn;
    }

    public static GerenciamentoNotas.listarAlunosResponse listarAlunos(Connection connection, String codigoDisciplina, int ano, int semestre) {        
        GerenciamentoNotas.listarAlunosResponse.Builder response = GerenciamentoNotas.listarAlunosResponse.newBuilder();
        try{

            Statement statement = connection.createStatement();
            ResultSet rs = statement.executeQuery("SELECT a.* FROM matricula m INNER JOIN aluno a ON (a.ra = m.ra) WHERE '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            if(!rs.isBeforeFirst()){
                response.setMensagem("Não há alunos matriculados nessa disciplina");
                return response.build();
            }
            while(rs.next()){
                int ra = rs.getInt("ra");
                String nome = rs.getString("nome");
                int periodo = rs.getInt("periodo");
                response.addAlunos(GerenciamentoNotas.listarAlunosResponse.Aluno.newBuilder().setNome(nome).setRa(ra).setPeriodo(periodo).build());
            }

        }
        catch(SQLException e){
            response.setMensagem(e.getMessage());
        }
        // response.setAluno("a");
        return response.build();
    }

    public static GerenciamentoNotas.alterarNotaResponse alterarNota(Connection connection, int ra, String codigoDisciplina, int ano, int semestre , float nota) {        
        GerenciamentoNotas.alterarNotaResponse.Builder response = GerenciamentoNotas.alterarNotaResponse.newBuilder();
        try{

            Statement statement = connection.createStatement();
            statement.execute("UPDATE matricula SET nota = " + nota + " WHERE ra =" + ra + " AND cod_disciplina = '" + String.valueOf(codigoDisciplina) + "' AND ano = " + ano + " AND semestre = " + semestre + ";");
            ResultSet rs = statement.executeQuery("SELECT * FROM matricula WHERE ra = " + ra + " AND '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            if(!rs.isBeforeFirst()){
                response.setMensagem("Não há disciplinas cadastradas neste curso");
                return response.build();
            }
            response.setRa(rs.getInt("ra"));
            response.setAno(rs.getInt("ano"));
            response.setSemestre(rs.getInt("semestre"));
            response.setCodigoDisciplina(rs.getString("cod_disciplina"));
            response.setNota(rs.getFloat("nota"));
        }
        catch(SQLException e){
            response.setMensagem(e.getMessage());
        }
        // response.setAluno("a");
        return response.build();
    }

    public static GerenciamentoNotas.alterarFaltasResponse alterarFaltas(Connection connection, int ra, String codigoDisciplina, int ano, int semestre, int faltas) {        
        GerenciamentoNotas.alterarFaltasResponse.Builder response = GerenciamentoNotas.alterarFaltasResponse.newBuilder();
        try{

            Statement statement = connection.createStatement();
            statement.execute("UPDATE matricula SET faltas = " + faltas + " WHERE ra =" + ra + " AND cod_disciplina = '" + String.valueOf(codigoDisciplina) + "' AND ano = " + ano + " AND semestre = " + semestre + ";");
            ResultSet rs = statement.executeQuery("SELECT * FROM matricula WHERE ra = " + ra + " AND '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            if(!rs.isBeforeFirst()){
                response.setMensagem("Não há disciplinas cadastradas neste curso");
                return response.build();
            }
            response.setRa(rs.getInt("ra"));
            response.setAno(rs.getInt("ano"));
            response.setSemestre(rs.getInt("semestre"));
            response.setCodigoDisciplina(rs.getString("cod_disciplina"));
            response.setFaltas(rs.getInt("faltas"));
        }
        catch(SQLException e){
            response.setMensagem(e.getMessage());
        }
        // response.setAluno("a");
        return response.build();
    }

    public static GerenciamentoNotas.listarDisciplinasCursoResponse listarDisciplinasCurso(Connection connection, int codigoCurso) {        
        GerenciamentoNotas.listarDisciplinasCursoResponse.Builder response = GerenciamentoNotas.listarDisciplinasCursoResponse.newBuilder();
        try{

            Statement statement = connection.createStatement();
            ResultSet rs = statement.executeQuery("SELECT * FROM disciplina WHERE " + String.valueOf(codigoCurso) + " = cod_curso;" /*+ ano + " = ano AND " + semestre + " = semestre;"*/);
            if(!rs.isBeforeFirst()){
                response.setMensagem("Não há disciplinas cadastradas neste curso");
                return response.build();
            }
            while(rs.next()){
                String professor = rs.getString("professor");
                String nome = rs.getString("nome");
                String codigo = rs.getString("codigo");
                response.addDisciplinas(GerenciamentoNotas.listarDisciplinasCursoResponse.DisciplinaCurso.newBuilder().setNome(nome).setCodigoDisciplina(codigo).setProfessor(professor).build());
            }

        }
        catch(SQLException e){
            response.setMensagem(e.getMessage());
        }
        // response.setAluno("a");
        return response.build();
    }

    public static GerenciamentoNotas.listarDisciplinasAlunoResponse listarDisciplinasAluno(Connection connection, int ra, int ano, int semestre) {        
        GerenciamentoNotas.listarDisciplinasAlunoResponse.Builder response = GerenciamentoNotas.listarDisciplinasAlunoResponse.newBuilder();
        try{

            Statement statement = connection.createStatement();
            /*Listagem de disciplinas, faltas e notas (RA, nome, nota, faltas) de um aluno informado o ano e semestre.*/ 
            ResultSet rs = statement.executeQuery("SELECT * FROM matricula WHERE " + ra + " = ra AND " + ano + " = ano AND " + semestre + " = semestre;");
            if(!rs.isBeforeFirst()){
                response.setMensagem("Não há disciplinas cadastradas neste curso");
                return response.build();
            }
            while(rs.next()){
                float nota = rs.getFloat("nota");
                String nome = rs.getString("nome");
                int faltas = rs.getInt("faltas");
                response.addDisciplinas(GerenciamentoNotas.listarDisciplinasAlunoResponse.DisciplinaAlunos.newBuilder().setNome(nome).setRa(ra).setNota(nota).setFaltas(faltas).build());
            }

        }
        catch(SQLException e){
            response.setMensagem(e.getMessage());
        }
        // response.setAluno("a");
        return response.build();
    }

    public static GerenciamentoNotas.inserirMatriculaResponse inserirMatricula(Connection connection, int ra,String codigoDisciplina, int ano, int semestre) {        
        GerenciamentoNotas.inserirMatriculaResponse.Builder response = GerenciamentoNotas.inserirMatriculaResponse.newBuilder();
        try{
            // TODO: verificar se o aluno já está matriculado nessa disciplina
            // TODO: verificar se a disciplina existe
            // TODO: verificar se o aluno existe
            Statement statement = connection.createStatement();
            statement.execute("INSERT INTO matricula (ra, cod_disciplina, ano, semestre, nota, faltas) VALUES (" + ra + ", '" + String.valueOf(codigoDisciplina) + "', " + ano + ", " + semestre + ", 0, 0);");
            ResultSet rs = statement.executeQuery("SELECT * FROM matricula WHERE " + ra + " = ra AND '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            if(!rs.isBeforeFirst()){
                response.setMensagem("Não há alunos matriculados nessa disciplina");
                return response.build();
            }
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
        catch(SQLException e){
            response.setMensagem(e.getMessage());
        }
        return response.build();
    }

    public static void main(String args[]) {
        Connection conn = connect();
        try {
            int serverPort = 7000;
            ServerSocket listenSocket = new ServerSocket(serverPort);
            String valueStr;
            int sizeBuffer;
            byte[] buffer;

            // enviar msg
            byte[] msg;
            String responseSize;
            byte[] size;
            while (true) {
                Socket clientSocket = listenSocket.accept();
                // BufferedReader dataaa = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                DataInputStream inClient = new DataInputStream(clientSocket.getInputStream());
                DataOutputStream outClient = new DataOutputStream(clientSocket.getOutputStream());
                valueStr = inClient.readLine();
                sizeBuffer = Integer.valueOf(valueStr);
                buffer = new byte[sizeBuffer];
                long pid = ProcessHandle.current().pid();
                inClient.read(buffer);

                    // realiza o unmarshalling
                GerenciamentoNotas.requestType type = GerenciamentoNotas.requestType.parseFrom(buffer);

                valueStr = inClient.readLine();
                sizeBuffer = Integer.valueOf(valueStr);
                buffer = new byte[sizeBuffer];
                inClient.read(buffer);

                switch (type.getType()) {
                    case LISTAR_ALUNOS:
                        GerenciamentoNotas.listarAlunosRequest request = GerenciamentoNotas.listarAlunosRequest.parseFrom(buffer);
                        GerenciamentoNotas.listarAlunosResponse response = listarAlunos(conn, request.getCodigoDisciplina() , request.getAno(), request.getSemestre());
                        msg = response.toString().getBytes();
                        responseSize = String.valueOf(msg.length) + " \n";
                        outClient.write(responseSize.getBytes());
                        outClient.write(msg);
                        break;
                    case ALTERAR_NOTA:
                        GerenciamentoNotas.alterarNotaRequest alterarNotaRequest = GerenciamentoNotas.alterarNotaRequest.parseFrom(buffer);
                        GerenciamentoNotas.alterarNotaResponse alterarNotaResponse = alterarNota(conn, alterarNotaRequest.getRa(), alterarNotaRequest.getCodigoDisciplina(), alterarNotaRequest.getAno(), alterarNotaRequest.getSemestre(), alterarNotaRequest.getNota());
                        msg = alterarNotaResponse.toString().getBytes();
                        responseSize = String.valueOf(msg.length) + " \n";
                        outClient.write(responseSize.getBytes());
                        outClient.write(msg);
                        break;
                    case ALTERAR_FALTAS:
                        GerenciamentoNotas.alterarFaltasRequest alterarFaltasRequest = GerenciamentoNotas.alterarFaltasRequest.parseFrom(buffer);
                        GerenciamentoNotas.alterarFaltasResponse alterarFaltasResponse = alterarFaltas(conn, alterarFaltasRequest.getRa(), alterarFaltasRequest.getCodigoDisciplina(), alterarFaltasRequest.getAno(), alterarFaltasRequest.getSemestre(), alterarFaltasRequest.getFaltas());
                        msg = alterarFaltasResponse.toString().getBytes();
                        responseSize = String.valueOf(msg.length) + " \n";
                        outClient.write(responseSize.getBytes());
                        outClient.write(msg);
                        break;
                    case LISTAR_DISCIPLINAS_CURSO:
                        GerenciamentoNotas.listarDisciplinasCursoRequest listarDisciplinasCursoRequest = GerenciamentoNotas.listarDisciplinasCursoRequest.parseFrom(buffer);
                        GerenciamentoNotas.listarDisciplinasCursoResponse listarDisciplinasCursoResponse = listarDisciplinasCurso(conn, listarDisciplinasCursoRequest.getCodigoCurso());
                        msg = listarDisciplinasCursoResponse.toString().getBytes();
                        responseSize = String.valueOf(msg.length) + " \n";
                        outClient.write(responseSize.getBytes());
                        outClient.write(msg);
                        break;
                    case LISTAR_DISCIPLINAS_ALUNO:
                        GerenciamentoNotas.listarDisciplinasAlunoRequest listarDisciplinasAlunoRequest = GerenciamentoNotas.listarDisciplinasAlunoRequest.parseFrom(buffer);
                        GerenciamentoNotas.listarDisciplinasAlunoResponse listarDisciplinasAlunoResponse = listarDisciplinasAluno(conn, listarDisciplinasAlunoRequest.getRa(), listarDisciplinasAlunoRequest.getAno(), listarDisciplinasAlunoRequest.getSemestre());
                        msg = listarDisciplinasAlunoResponse.toString().getBytes();
                        responseSize = String.valueOf(msg.length) + " \n";
                        outClient.write(responseSize.getBytes());
                        outClient.write(msg);
                        break;
                    case INSERIR_MATRICULA:
                        GerenciamentoNotas.inserirMatriculaRequest inserirMatriculaRequest = GerenciamentoNotas.inserirMatriculaRequest.parseFrom(buffer);
                        GerenciamentoNotas.inserirMatriculaResponse inserirMatriculaResponse = inserirMatricula(conn, inserirMatriculaRequest.getMatricula().getRa(), inserirMatriculaRequest.getMatricula().getCodigoDisciplina(), inserirMatriculaRequest.getMatricula().getAno(), inserirMatriculaRequest.getMatricula().getSemestre());
                        msg = inserirMatriculaResponse.toString().getBytes();   
                        responseSize = String.valueOf(msg.length) + " \n";
                        outClient.write(responseSize.getBytes());
                        outClient.write(msg);
                        break;
                    default:
                        System.out.println("Nenhum tipo de requisição");
                        break;
                }
                // System.out.println("−−\n" + type + "−−\n");
            } // while
        } catch (IOException e) {
            System.out.println("Listensocket:" + e.getMessage());
        } // catch
    }// main
}
// class