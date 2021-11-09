import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

import java.sql.*;

public class servidor {
    static final int LISTAR_ALUNOS = 1;
    static final int ALTERAR_NOTA = 2;
    static final int ALTERAR_FALTAS = 3;
    static final int LISTAR_DISCIPLINAS_CURSO = 4;
    static final int LISTAR_DISCIPLINAS_ALUNO = 5;
    static final int INSERIR_DISCIPLINA = 6;
    
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

    public static GerenciamentoNotas.listarAlunosResponse.Builder listarAlunos(/*String codigoDisciplina, int ano, int semestre*/) {        
        GerenciamentoNotas.listarAlunosResponse.Builder response = GerenciamentoNotas.listarAlunosResponse.newBuilder();

        String codigoDisciplina = "LQ34B";
        int ano = 2019;
        int semestre = 3;

        try{

            Statement statement = connect().createStatement();
            ResultSet rs = statement.executeQuery("SELECT a.* FROM matricula m INNER JOIN aluno a ON (a.ra = m.ra) WHERE '" + String.valueOf(codigoDisciplina) + "' = cod_disciplina ;" /*+ ano + " = ano AND " + semestre + " = semestre;"*/);
            if(!rs.isBeforeFirst()){
                response.setMensagem("Não há alunos matriculados nessa disciplina");
                return response;
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
        return response;
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
            String msgSize;
            byte[] size;
            while (true) {
                Socket clientSocket = listenSocket.accept();
                // BufferedReader dataaa = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                DataInputStream inClient = new DataInputStream(clientSocket.getInputStream());
                valueStr = inClient.readLine();
                sizeBuffer = Integer.valueOf(valueStr);
                buffer = new byte[sizeBuffer];
                long pid = ProcessHandle.current().pid();
                inClient.read(buffer);

                    // realiza o unmarshalling
                GerenciamentoNotas.requestType type = GerenciamentoNotas.requestType.parseFrom(buffer);
                /* exibenatela */
                switch (type.getType()) {
                    case LISTAR_ALUNOS:
                        System.out.println(listarAlunos());
                        break;
                    case ALTERAR_NOTA:
                        System.out.println("Alterar nota");
                        break;
                    case ALTERAR_FALTAS:
                        System.out.println("Alterar faltas");
                        break;
                    case LISTAR_DISCIPLINAS_CURSO:
                        System.out.println("Listar disciplinas do curso");
                        break;
                    case LISTAR_DISCIPLINAS_ALUNO:
                        System.out.println("Listar disciplinas do aluno");
                        break;
                    case INSERIR_DISCIPLINA:
                        System.out.println("Inserir disciplina");
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