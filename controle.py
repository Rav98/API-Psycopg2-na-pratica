from view import View
from modelM import ProdutoM
from modelM import PedidoM


class Controle:
    def inicio(self):
        opcao = self.view.inicio()

        while opcao != 8:
            if opcao == 1:
                l = self.view.coletadadosproduto()
                prod = ProdutoM.criaProduto(l)
                status = ProdutoM.cadastraProduto(prod)
                self.view.imprimeStatus(status)
            if opcao == 2:
                id = self.view.recebecodproduto()
                status = ProdutoM.deletaproduto(id)
                self.view.imprimeStatus(status)
            if opcao == 3:
                id = self.view.recebecodproduto()
                prod = ProdutoM.consultaproduto(id)
                self.view.imprimeProduto(prod)
            if opcao == 4:
                id = self.view.recebecodproduto()
                prod = ProdutoM.consultaproduto(id)
                self.view.imprimeProduto(prod)
                if(prod is not None):
                    l = self.view.coletadadosprodutoupdate()
                    status = ProdutoM.atualizaproduto(l)
                    self.view.imprimeProduto(status)
            if opcao == 5:
                id = self.view.recebecodproduto()
                l = PedidoM.consultarelatorio(id)
                self.view.imprimeRelatorio(l)
            if opcao == 6:
                l = self.view.coletadadospedido()
                p = self.view.coletaprodutospedido(l[0])
                status = PedidoM.cadastraVenda(l, p)
                self.view.imprimeStatus(status)
            if opcao == 7:
                l = self.view.coletadadosprodutoupdate()
                status = PedidoM.alteraVenda(l)
                self.view.imprimeStatus(status)
            opcao = self.view.menu()

    def __init__(self):
        self.view = View()


if __name__ == '__main__':
    main = Controle()
    main.inicio()
