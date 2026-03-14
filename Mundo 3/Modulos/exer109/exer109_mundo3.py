import moeda

valor = float(input(f"Digite o preço: R$ "))
print(f" O preço com aumento de 10% fica {moeda.aumentar(valor, True)}")
print(f" O preço com desconto de 15% fica {moeda.diminuir(valor, True)}")
print(f" O dobro é: {moeda.dobro(valor, True)}")
print(f" A metade é: {moeda.metade(valor, True)}")