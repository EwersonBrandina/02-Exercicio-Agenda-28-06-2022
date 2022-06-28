from class_produto import *
class Estoque:
    
    def __init__(self):
        self.listaProdutos = []
    
    def salvar_produtos(self):
        self.listaProdutos.append(Produto())
    
    def listar_produtos(self):
        x=input('1 - Todos.\n2 - Por Cod.\n3 - Por Nome.\n')
        if x == '1':
            for i in range(len(self.listaProdutos)):
                print('Código: ', self.listaProdutos[i].cod,
                'Nome: ', self.listaProdutos[i].nome,
                'Fabricante: ', self.listaProdutos[i].fabricante,
                'Quantidade: ', self.listaProdutos[i].quantidade)
        if x == '2':
            in_cod=input('Insira o código do produto.\n: ')
            for i in range(len(self.listaProdutos)):
                if self.listaProdutos[i].cod == in_cod:
                    print('Código: ', self.listaProdutos[i].cod,
                    'Nome: ', self.listaProdutos[i].nome,
                    'Fabricante: ', self.listaProdutos[i].fabricante,
                    'Quantidade: ', self.listaProdutos[i].quantidade)
                else:
                    for i in range(len(self.listaProdutos)):
                        print('Código: ', self.listaProdutos[i].cod,
                        'Nome: ', self.listaProdutos[i].nome,
                        'Fabricante: ', self.listaProdutos[i].fabricante,
                        'Quantidade: ', self.listaProdutos[i].quantidade)
        if x == '3':
            in_nome=input('Insira o nome do produto.\n: ')
            for i in range(len(self.listaProdutos)):
                if self.listaProdutos[i].nome == in_nome:
                    print('Código: ', self.listaProdutos[i].cod,
                    'Nome: ', self.listaProdutos[i].nome,
                    'Fabricante: ', self.listaProdutos[i].fabricante,
                    'Quantidade: ', self.listaProdutos[i].quantidade)
    def alterar_produtos(self):
        for i in range(len(self.listaProdutos)):
                print('Código: ', self.listaProdutos[i].cod,
                'Nome: ', self.listaProdutos[i].nome,
                'Fabricante: ', self.listaProdutos[i].fabricante,
                'Quantidade: ', self.listaProdutos[i].quantidade)
        in_cod=input('Insira o código do produto.\n: ')
        for i in range(len(self.listaProdutos)):
            if self.listaProdutos[i].cod == in_cod:
                self.listaProdutos[i].nome=input('Insira aqui o novo nome.\n: ')