def linha():
    print("-" * 75)

class Livro:
    ct=0
    @classmethod

    def get_qtd_livro(cls):
        return cls.ct
    
    def __init__(self, titulo, autor, paginas, preco=0.0):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.paginas = paginas
        Livro.ct += 1
        lis_livro.append(Livro.ct)
        lis_livro.append(self)
        

    def get_titulo(self):
        return self.titulo
    
    def set_preco(self, novo_preco):
        if novo_preco != 0:
            self.preco = novo_preco
        else:
            print("Valor inválido")

    def get_autor(self):
        return self.autor
    
    def get_paginas(self):
        return self.paginas

    def get_preco(self):
        return self.preco
    
    def aumenta_preco(self, valor_aumento):
        self.preco += valor_aumento
    
    def aumento_porcentagem(self, valor_aumento_pct):
        self.preco += valor_aumento_pct / 100 * self.preco
        
    def aumenta_paginas(self, qtd_pag):
        self.paginas += qtd_pag

    def ler_lista(lista):
        ct = 0
        for i in lista:
            ct += 1
            if ct // 5 == 0:
                linha()
            print(i)

    def mostra_dados(self):
        return f"Titulo: {self.get_titulo()}\nAutor: {self.get_autor()}\nPáginas: {self.get_paginas()}\nPreço: {self.get_preco()}"
    
    def __str__(self):
        return f"Titulo: {self.get_titulo()}\nAutor: {self.get_autor()}\nPáginas: {self.get_paginas()}\nPreço: {self.get_preco()}"
    
if __name__ == '__main__':
    lis_livro = []
    livro1 = Livro("Caio Boudens e a lenda do bardo peregrino", "Caio Boudens", 300, 500)
    # print(livro1.mostra_dados())
    livro2 = Livro("Guto o bravo VS Ender Dragon - O Livro", "Guto", 235)
    livro1.aumenta_preco(0)
    livro1.aumento_porcentagem(10)
    livro2.aumenta_paginas(50)    
    # print(Livro.get_qtd_livro())
    Livro.ler_lista(lis_livro)

