expressao = list(input().split())
valor = 0
if(len(expressao) != 3):
    print("ERRO: expressão invalida")
    exit()
def soma(num1, num2):
    return num1 + num2

def dif(num1, num2):
    return num1 - num2

def prod(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 != 0:
        return num1 / num2
try:
    numero1 = float(expressao[0])
    numero2 = float(expressao[2])
    op = expressao[1]
except:
    print("ERROR")
    exit()
def opera(op,numero1,numero2):
    if op == '+':
        valor = soma(numero1, numero2)
        print(valor, end = ' ')
    elif op == '-':
        valor = dif(numero1, numero2)
        print(valor, end = ' ')
    elif op == '*':
        valor = prod(numero1, numero2)
        print(valor, end = ' ')
    elif op == '/':
        if div(numero1,numero2) != None:
            valor = div(numero1, numero2)
            print(valor, end = ' ')
        else:
            print("ERROR")
    else:
        print("use uma operação valida \' + - * / \'")
    return valor
valor = opera(op, numero1, numero2)
while(True):
    expressao = input().split()
    if (len(expressao) != 2):
        print("ERRO: expressão invalida")
        exit()
    op = expressao[0]
    try:
        numero2 = float(expressao[1])
    except:
        print("ERROR")
    valor = opera(op, valor, numero2)
