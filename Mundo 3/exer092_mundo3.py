from datetime import datetime

dados = {'nome': str(input('Digite seu nome: ').capitalize()),
         'carteira': int(input('Digite o valor da carteira (0 para não possui): ')),
         }

nasc = int(input('Digite o ano em que você nasceu: '))

dados['idade'] = datetime.now().year - nasc

if dados['carteira'] != 0:
    dados['contratação'] = int(input("Ano da primeira contratação: "))
    dados['salario'] = float(input(f"Digite seu primeiro salário: "))
    dados['aposentadoria'] = dados['contratação'] - nasc + 35

print(dados.items())
for k, v in dados.items():
    print(f" {k} recebe o valor de {v}")





