'''
COM232 - BANCO DE DADOS 2

2018005379 - Flávio Mota Gomes
2018000980 - Rafael Antunes Vieira
'''

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
        parametros = ((AsIs(l[1])), int(l[2]), (AsIs(l[0])))
        status = config.alteraBD(config, string_sql, parametros)
        return status


class PedidoM():
    def __init__(self, orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid):
        self.orderid = orderid
        self.customerid = customerid
        self.employeeid = employeeid
        self.orderdate = orderdate
        self.requiredate = requireddate
        self.shippeddate = shippeddate
        self.freight = freight
        self.shipname = shipname
        self.shipaddress = shipaddress
        self.shipcity = shipcity
        self.shipregion = shipregion
        self.shippostalcode = shippostalcode
        self.shipcountry = shipcountry
        self.shipperid = shipperid

    def criaVenda(self, listaValores):
        venda = PedidoM(int(listaValores[0]),
                        str(listaValores[1]),
                        int(listaValores[2]),
                        str(listaValores[3]),
                        str(listaValores[4]),
                        str(listaValores[5]),
                        Decimal(listaValores[6]),
                        str(listaValores[7]),
                        str(listaValores[8]),
                        str(listaValores[9]),
                        str(listaValores[10]),
                        str(listaValores[11]),
                        str(listaValores[12]),
                        str(listaValores[13]))
        return venda

    def consultarelatorio(self, id):
        if (id == -1):
            string_sql = """SELECT * FROM relatorio"""
            registros = config.consultaBD(config, string_sql, [[]])
        else:
            string_sql = """SELECT * FROM relatorio WHERE orderid = %s"""
            registros = config.consultaBD(config, string_sql, [id])
        if(len(registros[1]) == 0):
            registros = None
        return registros

    def cadastraVenda(self, dadospedido, listaprodutos):
        string_SQL_pedido = """INSERT INTO northwind.orders(orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        string_SQL_produto = """INSERT INTO northwind.order_details(orderid, productid, unitprice, quantity, discount) VALUES (%s, %s, %s, %s, %s);"""
        status = config.cadastravendaBD(
            config, string_SQL_pedido, string_SQL_produto, dadospedido, listaprodutos)
        return status

    def alteravenda(self, dadospedido):
        string_sql = """UPDATE northwind.order_details SET quantity = %s WHERE orderid = %s AND productid = %s"""
        parametros = (dadospedido[2], dadospedido[0], dadospedido[1])
        status = config.alteraBD(config, string_sql, parametros)
        return status

    def consultavenda(self, id):
        string_sql = 'SELECT * FROM northwind.orders WHERE orderid = %s;'
        registros = config.consultaBD(config, string_sql, [id])
        if(len(registros[1]) != 0):
            vend = PedidoM.criaVenda(self, registros[1][0])
            return vend
        else:
            return None

    def deletavenda(self, id):
        string_sql = 'DELETE FROM northwind.order_details WHERE orderid = %s;'
        status = config.alteraBD(config, string_sql, [id])
        if status == 'sucesso':
            string_sql_1 = 'DELETE FROM northwind.orders WHERE orderid = %s;'
            status = config.alteraBD(config, string_sql_1, [id])
            return status
        else:
            return None

    def atualizaordemvenda(self, dadospedido):
        string_SQL_venda = """UPDATE northwind.orders SET %s = '%s' WHERE orderid = %s"""
        parametros = ((AsIs(dadospedido[1])), AsIs(dadospedido[2]), int(dadospedido[0]))
        status = config.atualizaordemvendaBD(
            config, string_SQL_venda, parametros)
        return status


class valida():
    def validacustomer(self, customerid):
        string_SQL = """SELECT * FROM northwind.customers WHERE customerid = %s;"""
        status = config.consultaExisteBD(config, string_SQL, [customerid])
        if(status == 0):
            print("Valor não existe no banco. Digite um valor válido.")
        return status

    def validaemployee(self, employeeid):
        string_SQL = """SELECT * FROM northwind.employees WHERE employeeid = %s;"""
        status = config.consultaExisteBD(config, string_SQL, [employeeid])
        if(status == 0):
            print("Valor não existe no banco. Digite um valor válido.")
        return status

    def verificaordem(self, ordem):
        string_SQL = """SELECT * FROM northwind.orders WHERE orderid = %s;"""
        status = config.consultaExisteBD(config, string_SQL, [ordem])
        if(status == 0):
            print("Valor não existe no banco. Digite um valor válido.")
        return status
