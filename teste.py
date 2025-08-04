#1- Questão:  
nome=input("Informe o seu nome: ")
idade=input("Informe a sua idade: ")
bebida=input("Qual a sua bebida favorita? ")
 
print("Esté {}, ele tem {} anos e sua bebida favorita é {} ".format(nome,idade,bebida))
 
#2- Questão: 
num1= 4.5
num2= 10
num3=  20
total= num1+ num2+ num3
 
print("A compra total foi de R${} ".format(total))
 
#3- Questão: 
livro = input("Informe o nome do seu livro: ")
paginas = (input("Informe a quantidade de páginas desse livro: "))
tempo = float(paginas)/ 10
print("Você irá terminar o livro {} em {} dias".format(livro, tempo))
 
#4- Questão 
nomeLista=input("Informe o nome da sua lista musical: ")
numeroMusicas=float(input("Informe o numero de musicas na sua playlist: "))
tempoMedio=float(input("Informe o tempo médio: "))
duraçao=float(tempoMedio*numeroMusicas)
print(duraçao)
 