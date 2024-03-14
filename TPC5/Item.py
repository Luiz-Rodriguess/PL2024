class Item:
    def __init__(self,id,nome,quant,preco):
        self.id = id
        self.nome = nome
        self.quant = quant
        self.preco = preco
        self.precoCents = int(preco*100)
    
    def __str__(self):
        return f'{self.id} | {self.nome:^20} | {self.quant:^3} | {self.preco}'
    
    def toDict(self):
        return {"cod": self.id,
                "nome": self.nome, 
                "quant": self.quant, 
                "preco": self.preco }
    