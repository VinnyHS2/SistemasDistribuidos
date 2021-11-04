import socket
import gerenciamentoNotas_pb2
clientsocket = socket.socket(socket.AFINET, socket.SOCKSTREAM)
clientsocket.connect(("localhost", 7000))
# instanciarepreencheraestrutura
person = gerenciamentoNotas_pb2.Person()
person.id = 234
person.name = "RodrigoCampiolo"
person.email = "rcampiolo@ibest.com.br"
# marshalling
msg = person.SerializeToString()
size = len(msg)
clientsocket.send((str(size) + "\n").encode())
clientsocket.send(msg)
clientsocket.close()
