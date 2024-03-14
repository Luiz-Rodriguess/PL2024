import ply.lex as lex
from stock import loadStock, saveStock
from datetime import date
from Item import Item
import re

add = False
total = 0
keepReading = True
stock = loadStock()

infoDict = {'LISTAR' : 'LISTAR - Indica a lista de itens \nLISTAR A23 - Indica a informação de um item específico',
            'MOEDA' : 'MOEDA 1e 50c - Introduz o saldo na máquina',
            'SELECIONAR' : 'SELECIONAR A23 - Escolhe o item',
            'SAIR' : 'SAIR - Devolve o troco e termina a execução',
            'SALDO' : 'SALDO - Indica o saldo atual',
            'LOAD' : 'LOAD A23 4 - Adiciona a quantidade para o produto indicado',
            'REMOVE' : 'REMOVE A23 - Retira o item do ficheiro ',
            'REGISTER' : 'REGISTER A14 "Barra de Cereais" 4 1.2 - Adiciona um novo item ao ficheiro',
            'INFO' : 'INFO - Mostra essa lista\nINFO opt - mostra a informação de uma função específica'
            }

def clear():
    print('\033c',end='')

def calcTroco(saldo):
    troco = []
    
    aux = saldo // 200
    if aux != 0:
        troco.append(f'{aux}x 2e')
    saldo %= 200
    
    aux = saldo // 100
    if aux != 0:
        troco.append(f'{aux}x 1e')
    saldo %= 100
    
    aux = saldo // 50
    if aux != 0:
        troco.append(f'{aux}x 50c')
    saldo %= 50

    aux = saldo // 20
    if aux != 0:
        troco.append(f'{aux}x 20c')
    saldo %= 20

    aux = saldo // 10
    if aux != 0:
        troco.append(f'{aux}x 10c')
    saldo %= 10

    aux = saldo // 5
    if aux != 0:
        troco.append(f'{aux}x 5c')
    saldo %= 5

    aux = saldo // 2
    if aux != 0:
        troco.append(f'{aux}x 2c')
    saldo %= 2

    if saldo != 0:
        troco.append(f'{saldo}x 1c')

    return ', '.join(troco) + '.'
    
def formatSaldo(saldo):
    euros = saldo // 100
    cents = saldo % 100
    value = '0' 
    if euros == 0:
        value = f'{cents}c'
    elif cents == 0:
        value = f'{euros}e'
    else: 
        value = f'{euros}e{cents}c'
    return value

tokens = (
    'LISTAR',
    'MOEDA',
    'MONEY',
    'SELECIONAR',
    'SAIR',
    'SALDO',
    'LOAD',
    'REGISTER',
    'REMOVE',
    'INFO'
)

def t_INFO(t):
    r'INFO(\ [A-Z]+)?'
    clear()
    aux = t.value.split()
    if len(aux) == 2:
        print(infoDict[aux[1]])
    else:
        for info in infoDict.values():
            print(info)
    
    


def t_REMOVE(t):
    r'REMOVE(\ [A-Z]\d+)?'
    aux = t.value.split()
    if (len(aux)) == 2:
        cod = aux.pop()
        global stock
        if cod in stock.keys():
            item = stock.pop(cod)
            print('maq: Removido:', item,sep='\n')
        else:
            print('maq: Produto inexistente')
    else:
        print('maq: Faltam Argumentos - INFO REMOVE para saber mais')

def t_REGISTER(t):
    r'REGISTER(\ [A-Z]\d+)?(\ "[ A-Za-z]+")?(\ \d+)?(\ \d.\d{1,2})?'
    global stock
    info = t.value.split('"')
    if len(info) == 3:
        cod = info[0].split()[1]
        nome = info[1]
        aux = info[2].split()
        quant = int(aux[0])
        preco = float(aux[1])
        if cod not in stock.keys():
            stock[cod] = Item(cod,nome,quant,preco)
            print('maq: Registado:',stock[cod],sep='\n')
        else:
            print('maq: Item já registado, use LOAD para carregar')
    else:
        print('maq: Faltam Argumentos - INFO REGISTER para saber mais')

def t_LOAD(t):
    r'LOAD(\ [A-Z]\d+)?(\ \d+)?'
    info = t.value.split()
    if len(info) == 3:
        item = info[1]
        quant = int(info[2])
        global stock
        if item in stock.keys():
            stock[item].quant += quant
        else:
            print('Not an option')
    else:
        print('maq: Faltam Argumentos - INFO LOAD para saber mais')


def t_SALDO(t):
    r'SALDO'
    global total
    print(f'maq: Saldo = {formatSaldo(total)}')

def t_SELECIONAR(t):
    r'SELECIONAR(\ [A-Z]\d+)?'
    global stock
    global total
    clear()
    aux = t.value.split()
    if len(aux) == 2:
        chosen = t.value.split()[1]
        if chosen in stock.keys():
            if stock[chosen].quant > 0:
                itemPrice = stock[chosen].precoCents
                if total >= itemPrice:
                    stock[chosen].quant -= 1
                    total -= itemPrice
                    print(f'maq: Pode retirar o produto dispensado: "{stock[chosen].nome}"')
                else:
                    print('maq: Saldo insuficiente para realizar o seu pedido',
                        f'maq: Saldo = {formatSaldo(total)} ; Pedido = {formatSaldo(itemPrice)}',sep='\n')
            else:
                print('maq: Produto indisponível')
            
        else:
            print('Not an option')
    else:
        print('maq: Faltam Argumentos - INFO SELECIONAR para saber mais')

t_ignore = ' \t\n'

def t_LISTAR(t):
    r'LISTAR(\ [A-Z]\d+)?'
    cod = 'cod'
    nome = 'nome'
    quant = 'q'
    preco = 'preço'
    clear()
    print('maq:',
          f'{cod} | {nome:^20} | {quant:^3} | {preco}',
          '-------------------------------------',sep='\n')
    global stock
    info = t.value.split()
    if len(info) == 2:
        if info[1] in stock.keys():
            print(stock[info[1]])
        else:
            print('Not an option')
    else:
        for item in stock.values():
            print(item)
    return t

def t_MOEDA(t):
    r'MOEDA'
    global add
    add = True
    return t

def t_MONEY(t):
    r'(2e|1e|50c|20c|10c|5c|2c|1c)(,\ |\ \.)'
    global add
    global total
    if add:
        aux = re.findall(r'\d+',t.value).pop()
        if 'e' in t.value:
            total += int(aux) *100
        elif 'c' in t.value:
            total += int(aux)
    return t

def t_SAIR(t):
    r'SAIR'
    global keepReading
    global total
    clear()
    if total == 0:
        print('maq: Até a próxima')
    else:
        print(f'maq: Pode retirar o troco: {calcTroco(total)}', 'maq: Até a próxima', sep='\n')
        total = 0
    keepReading = False
    return t

def t_error(t):
    print(f'Caractere ilegal {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()

print(f'maq: {date.today()}, Stock Carregado, Estado Atualizado',
       'maq: Bom dia. Estou disponível para atender o seu pedido.',
       'maq: Digite INFO para mais informação',sep='\n')
while keepReading:
    line = input()
    lexer.input(line)

    while tok := lexer.token():
        pass
    add = False

saveStock(stock)
