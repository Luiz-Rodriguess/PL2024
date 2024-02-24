# Manifesto

## Somador on/off

Autor: Luiz Rodrigues, A100700

O script encontra cada ocorrência de 'on', 'off', '=' ou um dígito

Foi assumido que as ocorrências das palavras-chave podem estar node meio de uma palavra maior (Ex. p**on**to)

Para encontrar as ocorrências é utilizado um regex com o método findall e depois processa as palavras-chave

Caso encontre 'on' começa a somar os números em um contador, se encontrar um 'off' não adiciona, com encontra um '=' faz-se print para o stdout o valor atual do contador
