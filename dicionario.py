def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def calcular(operacao, a, b):
    if operacao == "+":
        return somar(a, b)
    elif operacao == "-":
        return subtrair(a, b)
    elif operacao == "*":
        return multiplicar(a, b)
    elif operacao == "/":
        return dividir(a, b)
    else:
        return "Operação inválida"

while True:
    operacao = input("Digite a operação (+, -, *, /) ou 'sair': ")
    if operacao == "sair" or "Sair":
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = calcular(operacao, num1, num2)
    print("Resultado:", resultado)

print("Programa encerrado.")