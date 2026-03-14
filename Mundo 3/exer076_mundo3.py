tabela = ()
while True:
    produto = str(input("Digite o nome do produto: ")).strip().upper()
    valor = float(input("Digite o valor do produto: "))
    p = str(input("DESEJA ADICIONAR MAIS ITENS? [S/N] ")).strip().upper()
    tabela += (produto, valor, )
    if p in "Nn":
        break

print('='*40)
print("LISTA DE ITENS".center(40))
print("="*40)
for c in range (0, len(tabela),2):
    print(f"{tabela[c]:.<30} R$ {tabela[c+1]:.2f}")
print("-"*40)