class User():
    def __init__(self, login, senha, nome):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.active_tokens = []
        self.carrinho = Carrinho()

    def _clearTokens(self):
        self.active_tokens = []

    def authenticate(self, login, senha):
        return (self.login == login and self.senha == senha)

    def activateToken(self, token):
        self.active_tokens.append(token)

    def checkToken(self, token):
        return token in self.active_tokens


class Produto():
    def __init__(self, id, nome, preco, descricao):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def get(self):
        return {
            'id':self.id,
            'nome':self.nome,
            'preco':self.preco,
            'descricao':self.descricao
        }

class Carrinho():
    def __init__(self):
        self.produtos = dict()

    def addProduto(self, Produto):
        if self.produtos.get(Produto.id):
            self.produtos[Produto.id] += 1
        else:
            self.produtos[Produto.id] = 1 
        return self

    def removeProduto(self, Produto):
        try:
            del self.produtos[Produto.id]
            return self
        except Exception:
            return False