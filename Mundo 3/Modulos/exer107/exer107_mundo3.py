import moeda

valor = float(input("Digite o preço: R$ "))
print(f" O preço com aumento de 10% fica R$ {moeda.aumentar(valor):.2f}")
print(f" O preço com desconto de 15% fica R$ {moeda.diminuir(valor):.2f}")
print(f" O dobro é: R$ {moeda.dobro(valor):.2f}")
print(f" A metade é: R$ {moeda.metade(valor):.2f}")