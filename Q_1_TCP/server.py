'''
    # Questão 1 - TCP Servidor #
    # Autores: Henrique Moura Bini e Vinicius Henrique Soares
    # Data de criação: 12/10/2021
    # Data de modificação: 12/10/2021
    # Descrição:
        Faz o processamento de mensagens recebidas do cliente, nas quais atualmente são possiveis as seguintes operações:
            - CONNECT user, password: Confere os dados informados e realiza a conexão do usuário ao servidor
            - PWD: Devolve ao cliente o caminho atual
            - CHDIR *path*: Muda o diretório para o *path* especificado 
            - GETFILES: Devolve ao cliente todos os arquivos do diretório atual
            - GETDIRS: Devolve ao cliente todos os diretórios do diretório atual
            - EXIT: Finaliza a conexão com o cliente

'''
