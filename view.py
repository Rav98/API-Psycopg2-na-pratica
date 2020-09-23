from decimal import *
from model import OrderDetails
from datetime import datetime


class View():
    def inicio(self):
        return self.menu()

    def menu(self):
        print("ATIVIDADE PRATICA - MENU")
        print("Digite 1 para CADASTRAR PRODUTO")
        print("Digite 2 para DELETAR PRODUTO")
        print("Digite 3 para CONSULTAR PRODUTO")
        print("Digite 4 para ALTERAR PRODUTO")
        print("Digite 5 para CUNSULTAR RELATORIO DE PRODUTO")
        print("Digite 6 para CADASTRAR VENDA")
        print("Digite 7 para ALTERAR A QUANTIDADE DE PRODUTOS VENDIDOS")
        print("Digite 8 para SAIR")
        opcao = int(input("Opção escolhida:"))
        return opcao

    def coletadadosproduto(self):
        productid = input("Digite o ID do produto: ")
        productname = input("Digite o nome do produto: ")
        supplierid = input("Digite o identificador do fornecedor: ")
        categoryid = input("Digite o ID da categoria: ")
        quantityperunit = input(
            "Digite a quantidade de produto por embalagem: ")
        unitprice = input("Digite o preço do produto: ")
        unitsinslock = input("Digite a quantidade de unidades no estoque")
        unitsonorder = input(
            "Digite a quantidade de unidades disponiveis para venda: ")
        reorderlevel = input("Digite nivel do produto: ")
        discontinued = input("O produto está descontinuado?")
        valores = [productid, productname, supplierid, categoryid, quantityperunit,
                   unitprice, unitsinslock, unitsonorder, reorderlevel, discontinued]
        return valores

    def coletadadosprodutoupdate(self, id):
        atributos = {1: 'productname', 2: 'supplierid', 3: 'categoryid', 4: 'quantityperunit',
                     5: 'unitprice', 6: ' unitsinslock', 7: 'unitsonorder', 8: 'reorderlevel', 9: 'discontinued'}
        print("Digite:")
        print("1 para nome do produto")
        print("2 para identificador do fornecedor")
        print("3 para identificador da categoria")
        print("4 para quantidade de produto por embalagem")
        print("5 para preço unitario")
        print("6 para quantidade de produto no estoque")
        print("7 para quantidade de produto disponivel para venda")
        print("8 para nivel do produto")
        print("9 para descontinuado")
        campo = int(input())
        valor = input("Digite o novo valor para o atributo: ")
        if((campo == 2) or (campo == 3) or (campo == 5) or (campo == 6) or (campo == 7) or (campo == 8)):
            int(valor)
        elif(campo == 4):
            Decimal(valor)
        return(id, atributos[campo], valor)

    def recebecodproduto(self):
        productid = int(input("Digite o identificador do produto"))
        return productid

    def recebecodpedido(self):
        pedidoid = int(input("Digite o identificador do pedido"))
        return pedidoid

    def imprimeproduto(self, prod):
        if(prod is not None):
            print("ID : ", prod.id)
            print("Nome : ", prod.nome)
            print("Categoria : ", prod.categoria)
            print("Quantidade por embalagem: ", prod.quantidadeEmbalagem)
            print("Preço Unitario :", prod.precoUnitario)
            print("Estoque: ", prod.estoque)
            print("Disponiveis para venda:", prod.vendas)
            print("Nivel:", prod.nivel)
            print("Descontinuado:", prod.descontinuado)
        else:
            print("Consulta vazia!")

    def imprimeRelatorio(self, registros):
        if(registros is not None):
            colunas = registros[0]
            dados = registros[1]
            print("A consulta retornou", len(dados), "registros")
            for i in dados:
                print(colunas[0], ":", i[0])
                print(colunas[1], ":", i[1])
                print(colunas[2], ":", i[2])
                print(colunas[3], ":", i[3])
                print(colunas[4], ":", i[4])
                print(colunas[5], ":", i[5])
        else:
            print("A consulta não retornou dados!")

    def coletadadospedido(self):
        orderid = input("Digite o identificador do pedido: ")
        customerid = input("Digite o identificador do cleinte: ")
        enployerid = input("Digite o identificador do funcionario: ")
        orderdate = input("Digite a data do pedido (AAAA-MM-DD): ")
        requireddate = input(
            "Digite a data do fechamento do pedido (AAAA-MM-DD): ")
        shippeddate = input("Digite a data do envio do pedido (AAAA-MM-DD): ")
        freight = input("Digite o valor do frete: ")
        shipname = input("Digite o local do envio: ")
        shipaddress = input("Digite o endereço: ")
        shipcity = input("Digite a cidade do envio: ")
        shipregion = input("Digite o região do envio:")
        shipcountry = input("Digite o pais: ")
        shippostalcode = input("Digite o CEP: ")
        shipperid = input("Digite o id do endereço de envio: ")
        year, month, day = map(int, orderdate.split('-'))
        orderdate = datetime.datetime(year, month, day)
        year, month, day = map(int, requireddate.split('-'))
        requireddate = datetime.datetime(year, month, day)
        year, month, day = map(int, shippeddate.split('-'))
        pedido = (int(orderid), int(customerid), int(enployerid), int(orderdate), int(requireddate), int(shippeddate), int(freight), int(
            shipname), int(shipaddress), int(shipcity), int(shipregion), int(shipcountry), int(shippostalcode), int(shipperid))
        return pedido

    def coletaprodutospedido(self, orderid):
        i = 1
        listaProdutos = []
        while i != -1:
            print("Informe os produtos para o pedido ", orderid, " : ")
            productid = input("Digite o ID do produto: ")
            unitprice = input("Digite valor do produto: ")
            quntity = input("Digite a quantidade comprada: ")
            discount = input("Digite o valor do desconto: ")
            produtoPedido = OrderDetails(int(orderid), int(
                productid), int(unitprice), int(quntity), int(discount))
            listaProdutos.append(produtoPedido)
            i = int(input(
                "Deseja continuar cadastrar produtos para para esse pedido? (-1 para não | 1 para sim)"))
        return listaProdutos

    def coletadadospedidoupdate(self):
        pedidoid = int(input("Digite o código do pedido: "))
        productid = int(input("Digite o identificador do produto: "))
        quantidade = int(input("Digite a quantidade vendida: "))
        return [pedidoid, productid, quantidade]

    def imprimeStatus(self, status):
        if(status == "SUCESSO"):
            print("COMANDO EXECUTADO NO BANCO DE DADOS!!!")
        else:
            print(status)
