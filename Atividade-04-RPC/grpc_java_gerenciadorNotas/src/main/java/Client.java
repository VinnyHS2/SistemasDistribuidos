
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;


/**
 *
 * @author rodrigo
 */
public class Client {
    public static void main(String[] args) {
        ManagedChannel channel = ManagedChannelBuilder
                .forAddress("localhost", 7778)
                .usePlaintext()
                .build();
        
        GerenciadorDeNotasGrpc.GerenciadorDeNotasBlockingStub stub = 
                GerenciadorDeNotasGrpc.newBlockingStub(channel);
        
        ListarAlunosRequest request = ListarAlunosRequest
                .newBuilder()
                .setCodigoDisciplina("1")
                .setAno(1)
                .setSemestre(1)
                .build();
        
        // chamada remota
        ListarAlunosResponse reply = stub.listarAlunos(request);
        
        System.out.println("Resposta: " + reply.getMensagem());
        channel.shutdown();
    }
}
