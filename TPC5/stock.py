import json
from Item import Item

def loadStock():
    dataset = None
    stock = {}
    with open('stock.json','r') as file:
        dataset = json.load(file)
    
    for item in dataset['stock']:
        newItem = Item(item['cod'],item['nome'],item['quant'],item['preco'])
        stock[newItem.id] = newItem
    return stock

def saveStock(stock):
    dataset = {'stock':[]}
    with open('stock.json','w') as file:
        for item in stock.values():
            dataset['stock'].append(item.toDict())
        json.dump(dataset,file,indent=2)