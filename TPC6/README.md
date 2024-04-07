# Manifesto

## GIC LL(1) para expressões

Autor: Luiz Rodrigues, A100700

O objetivo deste TPC é definir uma gramática independente de contexto para a seguinte linguagem definida na aula teórica.

``` text
? a
b = a * 2 / (27 - 3)
! a + b
c = a * b / (a / b)
```

A gramática deve ser LL(1), deve-se garantir a prioridade das operações e devemos calcular os *look aheads* das regras.

### Definição da Linguagem

``` text
T = {$, '?', '!', '=', '+', '-', '*', '/', '(', ')', id, num}

N = {S, Op, Exp, Termo, Exp2, Fator, Termo2}

S = S

P = {

    S -> Op $                   LA = {'?', '!' , id}

    Op -> '?' id                LA = {'?'}
        | '!' Exp               LA = {'!'}
        | id '=' Exp            LA = {'='}

    Exp -> Termo Exp2           LA = {num, id, '('}

    Exp2 -> '+' Exp             LA = {'+'}
          | '-' Exp             LA = {'-'}
          | &                   LA = {')',$}
    
    Termo -> Fator Termo2       LA = {num, id, '('}

    Termo2 -> '*' Termo         LA = {'*'}
            | '/' Termo         LA = {'/'}
            | &                 LA = {'+', '-', ')', $}
    
    Fator -> num                LA = {num}
           | id                 LA = {id}
           | '(' Exp ')'        LA = {'('}
}
```
