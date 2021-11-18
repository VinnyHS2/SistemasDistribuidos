Compilar e executar:
    Para compilar o servidor 
    - mvn compile
	Para iniciar o servidor:
	- mvn exec:java -D"exec.mainClass"="Server"
	Para compilar o cliente:
	- python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. gerenciamentoNotas.proto
	Para iniciar o cliente:
	- python3 client.py

Bibliotecas python
  - grpc:	  Esta biblioteca permite o uso de funções para o uso do grpc
Bibliotecas Java
  - java.io:  Esta biblioteca permite o uso de funções para a realização de entrada e saída
  - java.sql: Esta biblioteca permite o uso de funções para a realização de conexões com o banco de dados SQLite

Exemplos de uso: 
	Listar todos as disciplinas de um curso
  		Após compilar e executar o programa digite no terminal do cliente:
		- Digite 4 para selecionar a opção de listagem de disciplinas de um curso
		- Em seguida digite o código do curso:
		Após enviar o terminal do cliente irá exibir a todas as disciplinas de um curso, caso ocorra algum erro ele irá exibir uma
        mensagem detalhando o erro.

	Alterar nota de um aluno matriculado em uma disciplina
  		Após compilar e executar o programa digite no terminal do cliente:
		- Digite 2 para selecionar a opção de alterar nota.
		- Em seguida digite o RA do aluno.
		- Em seguida digite o código da disciplina.
		- Em seguida digite o ano da disciplina.
		- Em seguida digite o semestre.
		- Em seguida digite a nota do aluno.
		Após enviar o terminal do cliente irá exibir as informações do aluno contendo a nova nota, caso ocorra algum erro ele irá exibir uma
        mensagem detalhando o erro.

