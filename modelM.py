import psycopg2
from decimal import *
from config import config
from psycopg2.extensions import AsIs
from datetime import datetime


class ProdutoM():
    def __init__(self, productid, productname, supplierid, categoryid, quantityperunit, unitprice, unitsinstock, unitsonorder, reorderlevel, discontinued):
        self.id = productid
        self.nome = productname
        self.fornecedor = supplierid
        self.categoria = categoryid
        self.quantidadeEmbalagem = quantityperunit
        self.precoUnitario = unitprice
        self.estoque = unitsinstock
        self.vendas = unitsonorder
        self.nivel = reorderlevel
        self.descontinuado = discontinued

    def criaProduto(self, listaValores):
        produto = ProdutoM(int(listaValores[0]), str(listaValores[1]), int(listaValores[2]), int(listaValores[3]),
                           str(listaValores[4]), Decimal(listaValores[5]),
                           int(listaValores[6]), int(listaValores[7]), int(listaValores[8]), str(listaValores[9]))
        return produto

    def cadastraProduto(self, produto):
        string_sql = 'INSERT INTO northwind.products (productid, productname, supplierid, categoryid, quantityperunit, unitprice, ' \
                     'unitsinstock, unitsonorder, reorderlevel, discontinued) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        novo_registro = (produto.id, produto.nome, produto.fornecedor, produto.categoria, produto.quantidadeEmbalagem,
                         produto.precoUnitario, produto.estoque, produto.vendas, produto.nivel, produto.descontinuado)
        status = config.alteraBD(config, string_sql, novo_registro)
        return status

    def deletaproduto(self, id):
        string_sql = 'DELETE FROM northwind.products WHERE productid = %s;'
        status = config.alteraBD(config, string_sql, [id])
        return status

    def consultaproduto(self, id):
        string_sql = 'SELECT * FROM northwind.products WHERE productid = %s;'
        registros = config.consultaBD(config, string_sql, [id])
        if(len(registros[1]) != 0):
            prod = ProdutoM.criaProduto(self, registros[1][0])
            return prod
        else:
            return None

    def atualizaproduto(self, l):
        string_sql = """UPDATE northwind.products SET %s = %s WHERE productid = %s"""
        parametros = ((AsIs(l[1])), int(l[2]), int(l[0]))
        status = config.alteraBD(config, string_sql, parametros)
        return status


class PedidoM():
    def consultarelatorio(self, id):
        if (id == -1):
            string_sql = """SELECT * FROM northwind.relatorio"""
            registros = config.consultaBD(config, string_sql, [[]])
        else:
            string_sql = """SELECT * FROM northwind.relatorio WHERE numpedido = %s"""
            registros = config.consultaBD(config, string_sql, [id])
        if(len(registros[1]) == 0):
            registros = None
        return registros

    def cadastravendas(self, dadospedido, listaprodutos):
        dadospedido = [258952, 2, 2, datetime(2020, 9, 21, 0, 0), datetime(
            2020, 9, 22, 0, 0), datetime(2020, 9, 23, 0, 0), Decimal('36'), 'abc', ]
        string_SQL_pedido = """INSERT INTO northwind.orders(orderid, customerid, empoyerid, overdate, requiredate, shippeddate, freight, shipname) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
        string_SQL_produto = """INSERT INTO northwind.order_details(orderid, productid, unitprice, quantity, discount) VALUES (%s, %s, %s, %s, %s);"""
        status = config.cadastravendaBD(
            config, string_SQL_pedido, string_SQL_produto, dadospedido, listaprodutos)
        return status

    def alteravenda(self, dadospedido):
        string_sql = """UPDATE northwind.order_details SET quantity = %s WHERE orderid = %s AND productid = %s"""
        parametros = (dadospedido[2], dadospedido[0], dadospedido[1])
        status = config.alteraBD(config, string_sql, parametros)
        return status
