# Manifesto

## Máquina de vendas

Autor: Luiz Rodrigues, A100700

O programa *vending.py* lê do terminal as instruções que serão dadas à máquina

O ficheiro *stock.py* carrega o dataset no ínicio da execução e salva no fim

O ficheiro *Item.py* possui uma classe que guarda as informações de um item

Para fazer a análise léxica dos inputs foi utilizada o *ply.lex*

As funcionalidades disponíveis incluem:

+ LISTAR - Faz print da lista de itens contidos no stock
+ MOEDA - Permite o utilizador carregar o saldo da máquina
+ SELECIONAR - Permite o utilizador escolher qual o item que quer comprar
+ SALDO - Faz print do saldo atual
+ LOAD - Permite o utilizador aumentar a quantidade de um item
+ REGISTER - Permite o utilizador carregar um novo item que será salvo no ficheiro
+ REMOVE - Retira um item da máquina e apaga a sua entrada do ficheiro
+ INFO - Faz print das funções disponíveis e possui exemplos de utilização
+ SAIR - Termina a execução e devolve o troco do utilizador
