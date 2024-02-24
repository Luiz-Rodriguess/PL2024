import re

def handle(calculator):
    mode = False
    total = 0
    for item in calculator:
        if item == 'on':
            mode = True
        elif item == 'off':
            mode = False
        elif item == '=':
            print(f'Current sum = {total}')
        else:
            if mode:
                total += int(item)


def main():
    calculator = []
    with open('file.txt','r') as file:
        for line in file:
            for keyword in re.findall(r'(on)|(off)|(\d+)|(=)',line,re.I):
                for match in keyword:
                    if match:
                        calculator.append(match.lower())

    handle(calculator)
if __name__ == '__main__':
    main()