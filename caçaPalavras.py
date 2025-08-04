import random

palavras = ["PRINT", "RUN", "SAVE", "OPON", "RETURN", "BREAK", "CONTINUE", "IMPORT"]
tamanho = 12

grade = [[random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(tamanho)] for _ in range(tamanho)]

def inserir_palavras(grade, palavras):
    for palavra in palavras:
        palavra = palavra.upper()
        linha = random.randint(0, tamanho - 1)
        col_ini = random.randint(0, tamanho - len(palavra))
        for i in range(len(palavra)):
            grade[linha][col_ini + i] = palavra[i]

inserir_palavras(grade, palavras)
print("=== Caça-Palavras ===")
for linha in grade:
    print(" ".join(linha))

print("\nEncontre estas palavras:")
for palavra in palavras:
    print(f"- {palavra.capitalize()}")
