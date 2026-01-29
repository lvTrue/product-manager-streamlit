from persistencia import salvar_dados, carregar_dados

class SistemaCadastro:
    def __init__(self):
        self.lista_produtos = []
        
    def salvar(self):
        salvar_dados(self.lista_produtos)
        
    def add_produto(self, produto):
        for prod in self.lista_produtos:
            if prod["nome"] == produto.nome:
                return False
        self.lista_produtos.append(produto.listar_json())
        self.salvar()
        return True
    
    def remover_produto(self, nome):
        for prod in self.lista_produtos:
            if prod["nome"] == nome:
                self.lista_produtos.remove(prod)
                return True
        return False
    
    def editar_produto(self, nome):
        for prod in self.lista_produtos:
            if prod["nome"] == nome:
                return prod
        return None
    