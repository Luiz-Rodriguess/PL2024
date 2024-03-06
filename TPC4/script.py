import re

def tokenize(line):
    tokenSpecification = [
        ('VAR', r'[a-z]+'),
        ('COMP', r'=|[<>]=?'),
        ('KEYW', r'SELECT|FROM|WHERE'),
        ('SEP', r','),
        ('NUM', r'\d+'),
        ('NEWLINE', r'\n'),
        ('SKIP', r'[ \t]+'),
        ('ERRO', r'.')
    ]
    tokRegex = '|'.join('(?P<%s>%s)' % pair for pair in tokenSpecification)
    found = []
    mo = re.finditer(tokRegex,line)
    for m in mo:
        dic = m.groupdict()
        t = None
        if dic['VAR']:
            t = ('VAR', dic['VAR'])
        elif dic['COMP']:
            t = ('COMP', dic['COMP'])
        elif dic['KEYW']:
            t = ('KEYW', dic['KEYW'])
        elif dic['NUM']:
            t = ('NUM', int(dic['NUM']))
        elif dic['SEP']:
            t = ('SEP', dic['SEP'])
        elif dic['NEWLINE']:
            pass
        elif dic['SKIP']:
            pass
        else :
            t = ('ERRO', m.group())
        if t:
            found.append(t)
    return found


def main():
    with open('example.txt','r') as file:
        for line in file:
            for res in tokenize(line):
                print(res)


if __name__ == '__main__':
    main()