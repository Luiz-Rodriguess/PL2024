modalidades = []
res = {}
res['aptos'] = 0
res['inaptos'] = 0
ages = {}

def validate(line):
    flag = True    
    arguments = line.split(',')

    if arguments[8] not in modalidades:
        modalidades.append(arguments[8])

    if arguments[-1] == 'true':
        res['aptos'] += 1
    else: 
        res['inaptos'] += 1
    
    ageRange = int(arguments[5]) // 5
    key = f'[{ageRange*5}-{ageRange*5+4}]'

    athleteName = f'{arguments[3]} {arguments[4]}'

    if key not in ages :
        ages[key] = [athleteName]
    else:
        ages[key].append(athleteName)
    
    return flag

def parse(filepath):
    totalTests = 0 

    with open(filepath,"r") as file:

        file.readline()

        for linha in file:
            totalTests += 1
            linha = linha.strip()
            validate(linha)

    modalidades.sort()
    return totalTests

def writeSolutions(totalTests):
    with open("modalidades.txt",'w') as file:
        length = len(modalidades)
        file.write('[ ')
        for index,modalidade in enumerate(modalidades):
            file.write(f'{modalidade}')
            if (index != length -1):
                file.write(', ')
        file.write(' ]')

    with open("aptidões.txt",'w') as file:
        for key,value in res.items():
            file.write(f'{key} : {round(value/totalTests * 100,2)}% ')

    with open("faixaEtária.txt",'w') as file:
        for key,value in ages.items():
            file.write(f'{key} : [ ')
            length = len(value)
            for index,name in enumerate(value):
                file.write(f'{name}')
                if (index != length -1):
                    file.write(', ')
            file.write(' ]\n')

filepath = 'emd.csv'
totalTests = parse(filepath)

writeSolutions(totalTests)
