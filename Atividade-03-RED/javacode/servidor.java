import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class servidor {
    public static void main(String args[]) {
        
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
                inClient.read(buffer);

                    // realiza o unmarshalling
                p = Gerenciamentodenotas.requisicaoOpt.parseFrom(buffer);
                /* exibenatela */
                System.out.println("−−\n" + p + "−−\n");
            } // while
        } catch (IOException e) {
            System.out.println("Listensocket:" + e.getMessage());
        } // catch
    }// main
}
// class