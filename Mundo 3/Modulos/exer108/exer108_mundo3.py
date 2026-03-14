import moeda

valor = float(input(f"Digite o preço: R$ "))
print(f" O preço com aumento de 10% fica {moeda.moeda(moeda.aumentar(valor))}")
print(f" O preço com desconto de 15% fica {moeda.moeda(moeda.diminuir(valor))}")
print(f" O dobro é: {moeda.moeda(moeda.dobro(valor))}")
print(f" A metade é: {moeda.moeda(moeda.metade(valor))}")