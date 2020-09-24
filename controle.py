from view import View
from modelM import ProdutoM
from modelM import PedidoM


class Controle:
    def inicio(self):
        opcao = self.view.inicio()

        while opcao != 0:
            if opcao == 1:
                l = self.view.coletadadosproduto()
                prod = ProdutoM.criaProduto(self, l)
                status = ProdutoM.cadastraProduto(self, prod)
                self.view.imprimeStatus(status)
            if opcao == 2:
                id = self.view.recebecodproduto()
                status = ProdutoM.deletaproduto(self, id)
                self.view.imprimeStatus(status)
            if opcao == 3:
                id = self.view.recebecodproduto()
                prod = ProdutoM.consultaproduto(self, id)
                self.view.imprimeproduto(prod)
            if opcao == 4:
                id = self.view.recebecodproduto()
                prod = ProdutoM.consultaproduto(self, id)
                self.view.imprimeproduto(prod)
                if(prod is not None):
                    l = self.view.coletadadosprodutoupdate(id)
                    status = ProdutoM.atualizaproduto(self, l)
                    self.view.imprimeStatus(status)
            if opcao == 5:
                id = self.view.recebecodproduto()
                l = PedidoM.consultarelatorio(self, id)
                self.view.imprimeRelatorio(l)
            if opcao == 6:
                l = self.view.coletadadospedido()
                p = self.view.coletaprodutospedido(l[0])
                status = PedidoM.cadastraVenda(self, l, p)
                self.view.imprimeStatus(status)
            if opcao == 7:
                l = self.view.coletadadospedidoupdate()
                status = PedidoM.alteravenda(self, l)
                self.view.imprimeStatus(status)
            if opcao == 8:
                id = self.view.recebecodvenda()
                prod = PedidoM.consultavenda(self, id)
                self.view.imprimevenda(prod)
            if opcao == 9:
                print("aaa")
            if opcao == 10:
                id = self.view.recebecodvenda()
                status = PedidoM.deletavenda(self, id)
                self.view.imprimeStatus(status)
            opcao = self.view.menu()

    def __init__(self):
        self.view = View()


if __name__ == '__main__':
    main = Controle()
    main.inicio()
