def somar_tupla(tupla_numeros):
  soma = 0
  for numero in tupla_numeros:
    soma += numero
  return soma
tupla1 = (1, 2, 3, 4, 5)
resultado1 = somar_tupla(tupla1)
print("A soma dos elementos da tupla {} é: {}".format(tupla1,resultado1))

tupla2 = (-10, 20, -5, 15)
resultado2 = somar_tupla(tupla2)
print(f"A soma dos elementos da tupla {tupla2} é: {resultado2}")

tupla3 = (10,)
resultado3 = somar_tupla(tupla3)
print(f"A soma dos elementos da tupla {tupla3} é: {resultado3}")

tupla4 = ()
resultado4 = somar_tupla(tupla4)
print(f"A soma dos elementos da tupla {tupla4} é: {resultado4}")