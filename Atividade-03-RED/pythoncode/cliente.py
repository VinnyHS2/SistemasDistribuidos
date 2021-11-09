import socket
import gerenciamentoNotas_pb2
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost", 7000))
# instanciarepreencheraestrutura
requestType = gerenciamentoNotas_pb2.requestType()
requestType.type = 1
# marshalling
msg = requestType.SerializeToString()
size = len(msg)
clientsocket.send((str(size) + "\n").encode())
clientsocket.send(msg)
clientsocket.close()
