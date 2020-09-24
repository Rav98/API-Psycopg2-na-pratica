'''
COM232 - BANCO DE DADOS 2

2018005379 - Flávio Mota Gomes
2018000980 - Rafael Antunes Vieira
'''

from decimal import *
from modelM import *
from model import *
from datetime import datetime
import modelM


class View():
    def inicio(self):
        return self.menu()

    def menu(self):
        print("=====================ATIVIDADE PRATICA - MENU=====================")
        print("| -> Menu Produto                                                |")
        print("|    -> Digite 1 para CADASTRAR PRODUTO                          |")
        print("|    -> Digite 2 para DELETAR PRODUTO                            |")
        print("|    -> Digite 3 para CONSULTAR PRODUTO                          |")
        print("|    -> Digite 4 para ALTERAR PRODUTO                            |")
        print("|    -> Digite 5 para CONSULTAR RELATORIO DE PEDIDOS             |")
        print("|    -> Digite 6 para ALTERAR A QUANTIDADE DE PRODUTOS VENDIDOS  |")
        print("| -> Menu Ordem                                                  |")
        print("|    -> Digite 7 para CADASTRAR ORDEM                            |")
        print("|    -> Digite 8 para CONSULTAR ORDEM                            |")
        print("|    -> Digite 9 para ALTERAR ORDEM                              |")
        print("|    -> Digite 10 para APAGAR ORDEM                              |")
        print("| -> Digite 0 para SAIR                                          |")
        print("==================================================================")
        opcao = int(input("Opção escolhida: "))
        return opcao

    def coletadadosproduto(self):
        productid = input("Digite o ID do produto: ")
        productname = input("Digite o nome do produto: ")
        supplierid = input("Digite o identificador do fornecedor: ")
        categoryid = input("Digite o ID da categoria: ")
        quantityperunit = input(
            "Digite a quantidade de produto por embalagem: ")
        unitprice = input("Digite o preço do produto: ")
        unitsinstock = input("Digite a quantidade de unidades no estoque: ")
        unitsonorder = input(
            "Digite a quantidade de unidades disponiveis para venda: ")
        reorderlevel = input("Digite nivel do produto: ")
        discontinued = input("O produto está descontinuado? ")
        valores = [productid, productname, supplierid, categoryid, quantityperunit,
                   unitprice, unitsinstock, unitsonorder, reorderlevel, discontinued]
        return valores

    def coletadadosprodutoupdate(self, id):
        atributos = {1: 'productname', 2: 'supplierid', 3: 'categoryid', 4: 'quantityperunit',
                     5: 'unitprice', 6: ' unitsinslock', 7: 'unitsonorder', 8: 'reorderlevel', 9: 'discontinued'}
        print("\nDigite:")
        print("1 para nome do produto")
        print("2 para identificador do fornecedor")
        print("3 para identificador da categoria")
        print("4 para quantidade de produto por embalagem")
        print("5 para preço unitario")
        print("6 para quantidade de produto no estoque")
        print("7 para quantidade de produto disponivel para venda")
        print("8 para nivel do produto")
        print("9 para descontinuado\n")
        campo = int(input())
        valor = input("\nDigite o novo valor para o atributo: ")
        if((campo == 2) or (campo == 3) or (campo == 6) or (campo == 7) or (campo == 8)):
            int(valor)
        elif(campo == 4):
            Decimal(valor)
        return(id, atributos[campo], valor)

    def recebecodproduto(self):
        productid = int(input("Digite o identificador do produto: "))
        return productid

    def recebecodpedido(self):
        productid = int(input("Digite o identificador do pedido: "))
        return productid

    def recebecodvenda(self):
        vendaid = int(input("Digite o identificador da venda: "))
        return vendaid

    def recebecodpedido(self):
        pedidoid = int(input("Digite o identificador do pedido: "))
        return pedidoid

    def imprimeproduto(self, prod):
        if(prod is not None):
            print(prod)
            print("\nID: ", prod.id)
            print("Nome: ", prod.nome)
            print("Fornecedor: ", prod.fornecedor)
            print("Categoria: ", prod.categoria)
            print("Quantidade & embalagem: ", prod.quantidadeEmbalagem)
            print("Preço Unitario: ", prod.precoUnitario)
            print("Estoque: ", prod.estoque)
            print("Disponiveis para venda: ", prod.vendas)
            print("Nivel: ", prod.nivel)
            print("Descontinuado: ", prod.descontinuado)
        else:
            print("Consulta vazia")

    def imprimevenda(self, venda):
        if(venda is not None):
            print("\nID do pedido: ", venda.orderid)
            print("Cliente: ", venda.customerid)
            print("Funcionario: ", venda.employeeid)
            print("Data do pedido: ", venda.orderdate)
            print("Data do fechamento: ", venda.requiredate)
            print("Data do envio: ", venda.shippeddate)
            print("Valor do frete: ", venda.freight)
            print("Local de envio: ", venda.shipname)
            print("Endereço: ", venda.shipaddress)
            print("Cidade: ", venda.shipcity)
            print("Regiao: ", venda.shipregion)
            print("País: ", venda.shipcountry)
            print("CEP: ", venda.shippostalcode)
            print("ID do endereço de envio: ", venda.shipperid)
        else:
            print("Consulta vazia")

    def imprimeRelatorio(self, registros):
        if(registros is not None):
            colunas = registros[0]
            dados = registros[1]
            print("\n\nDados: ")
            print("A consulta retornou", len(dados), "registros")
            for i in dados:
                print(colunas[0], ": ", i[0])
                print(colunas[1], ": ", i[1])
                print(colunas[2], ": ", i[2])
                print(colunas[3], ": ", i[3])
                print(colunas[4], ": ", i[4])
        else:
            print("A consulta não retornou dados")

    def coletadadospedido(self):
        orderid = input("\nDigite o identificador do pedido: ")

        # Validação customerid
        valorcustomerid = 0
        while valorcustomerid == 0:
            customerid = input(
                "Digite o identificador do cliente (identificador é string de cliente que já existe): ")
            valorcustomerid = valida.validacustomer(self, customerid)

        # Validação employeeid
        valorfunc = 0
        while valorfunc == 0:
            enployerid = input("Digite o identificador do funcionario: ")
            valorfunc = valida.validaemployee(self, enployerid)

        orderdate = input("Digite a data do pedido (AAAA-MM-DD): ")
        requireddate = input(
            "Digite a data do fechamento do pedido (AAAA-MM-DD): ")
        shippeddate = input("Digite a data do envio do pedido (AAAA-MM-DD): ")
        freight = input("Digite o valor do frete: ")
        shipname = input("Digite o local do envio: ")
        shipaddress = input("Digite o endereço: ")
        shipcity = input("Digite a cidade do envio: ")
        shipregion = input("Digite o região do envio: ")
        shipcountry = input("Digite o pais: ")
        shippostalcode = input("Digite o CEP: ")
        shipperid = input("Digite o id do endereço de envio: ")
        year, month, day = map(int, orderdate.split('-'))
        orderdate = datetime(year, month, day)
        year, month, day = map(int, requireddate.split('-'))
        requireddate = datetime(year, month, day)
        year, month, day = map(int, shippeddate.split('-'))
        shippeddate = datetime(year, month, day)
        pedido = (int(orderid), customerid, int(enployerid), orderdate, requireddate, shippeddate, Decimal(freight),
                  shipname, shipaddress, shipcity, shipregion, shipcountry, shippostalcode, int(shipperid))
        return pedido

    def coletaprodutospedido(self, orderid):
        i = 1
        listaProdutos = []
        while i != -1:
            print("\nInforme os produtos para o pedido ", orderid, ": ")
            productid = input("Digite o ID do produto: ")
            unitprice = input("Digite valor do produto: ")
            quntity = input("Digite a quantidade comprada: ")
            discount = input("Digite o valor do desconto: ")
            produtoPedido = OrderDetails(int(orderid), int(productid), Decimal(
                unitprice), int(quntity), Decimal(discount))
            listaProdutos.append(produtoPedido)
            i = int(input(
                "Deseja continuar cadastrar produtos para para esse pedido? (-1 para não | 1 para sim): "))
        return listaProdutos

    def coletadadospedidoupdate(self):
        pedidoid = int(input("Digite o código do pedido: "))
        productid = int(input("Digite o identificador do produto: "))
        quantidade = int(input("Digite a quantidade vendida: "))
        return [pedidoid, productid, quantidade]

    def imprimeStatus(self, status):
        if(status == "sucesso"):
            print("\nCOMANDO EXECUTADO NO BANCO DE DADOS!!!")
        else:
            print(status)

    def coletadadosordemupdate(self):
        atributos = {1: 'orderdate', 2: 'requireddate', 3: 'shippeddate', 4: 'freight',
                     5: 'shipname', 6: ' shipaddress', 7: 'shipcity', 8: 'shipregion', 9: 'shipcountry', 10: 'shippostalcode', 11: 'shipperid', 12: 'customerid', 13: 'employeeid'}

        print("\nDigite:")
        print("Digite 1 para alterar a  data do pedido (AAAA-MM-DD)")
        print("Digite 2 para alterar data do fechamento do pedido (AAAA-MM-DD)")
        print("Digite 3 para alterar data do envio do pedido (AAAA-MM-DD)")
        print("Digite 4 para alterar valor do frete")
        print("Digite 5 para alterar local do envio")
        print("Digite 6 para alterar o endereço")
        print("Digite 7 para alterar a cidade do envio")
        print("Digite 8 para alterar a região do envio")
        print("Digite 9 para alterar o pais")
        print("Digite 10 para alterar o CEP")
        print("Digite 11 para alterar o ID do endereço de envio")
        print("Digite 12 para alterar o consumidor")
        print("Digite 13 para alterar o funcionario")

        campo = int(input())

        # Verificar se a ordem existe
        verificaordem = 0
        while verificaordem == 0:
            valor_ordem = input("Digite o ID da ordem da venda: ")
            verificaordem = valida.verificaordem(self, valor_ordem)

        # Para alterar o identificador do cliente, é necessario que ele exista. Portanto, fazemos a validacao:
        if(campo == 12):
            valorcustomerid = 0
            while valorcustomerid == 0:
                valor = input(
                    "Digite o novo identificador do cliente (identificador é string de cliente que já existe): ")
                valorcustomerid = valida.validacustomer(self, valor)

        # Para alterar o identificador do funcionario, é necessario que ele exista. Portanto, fazemos a validacao:
        elif(campo == 13):
            valorfunc = 0
            while valorfunc == 0:
                valor = input("Digite o novo identificador do funcionario: ")
                valorfunc = valida.validaemployee(self, valor)
        else:
            valor = input("Digite o novo valor para o atributo: ")
            if(campo == 1 or campo == 2 or campo == 3):
                year, month, day = map(int, valor.split('-'))
                valor = datetime(year, month, day)

            elif(campo == 4):
                Decimal(valor)

        return (valor_ordem, atributos[campo], valor)
