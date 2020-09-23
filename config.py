import psycopg2

class config:
    def __init__(self, dadosconexao):
        self.dadosconexao = dadosconexao

    def setParametros(self):
        self.dadosconexao = "host='localhost' dbname='Northwind' user='postgres' password='root'"
        return self

    def alteraBD(self, stringSQL, valores):
        #iniciar conexão vazio
        conn = None
        try:
            # abrir a conexão
            conexao = psycopg2.connect(config.setParametros(self).dadosconexao)

            # abrir a sessão - a transação começa aqui 
            sessao = conexao.cursor()

            # Executar a remoção na memória RAM
            sessao.execute(stringSQL, valores)

            # Comitar a remoçao - fechar a transação
            conexao.commit()

            # Encerrar a sessão
            sessao.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return "sucesso"

    def consultaBD(self, stringSQL, valores):
        #iniciar conexão vazio
        conn = None
        try:
            # abrir a conexão
            conexao = psycopg2.connect(config.setParametros(self).dadosconexao)

            # abrir a sessão - a transação começa aqui
            sessao = conexao.cursor()

            # Executar a remoção na memória RAM
            sessao.execute(stringSQL, valores)

            # Armazenar os resultados:
            registros = sessao.fetchall()
            colnames = [desc[0] for desc in sessao.description] 

            # Comitar a remoçao - fechar a transação
            conexao.commit()

            # Encerrar a sessão
            sessao.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return (colnames, registros)

    def cadastravendaBD(self, string_SQL_pedido, string_SQL_produto dadospedido, listaprodutos):
