print('='*30)
print("CHECK OUT PRODUTOS")
print('='*30)
soma = 0
cont_p = 0
mais_barato_preco = 0
mais_barato_nome =''

while True:
    nome_produto = str(input("QUAL O NOME DO PRODUTO? "))
    preco_produto = float(input("QUANTO CUSTA O PRODUTO? R$ "))
    if preco_produto > 1000:
        cont_p += 1
    soma += preco_produto

    if mais_barato_preco == 0 or preco_produto < mais_barato_preco:
        mais_barato_preco = preco_produto
        mais_barato_nome = nome_produto

    a = str(input("DESEJA CONTINUAR O CADASTRO? [Sim/Não] ")).upper().strip()
    if a[0] == 'N':
        break

print('='*30)
print("LISTA DE COMPRAS")
print("="*30)
print(f"O TOTAL GASTO FOI DE R$ {soma:.2f}")
print(f"A QUANTIDADE DE ITENS ACIMA DE 1000 REAIS FOI DE {cont_p} ITEN(S)")
print(f"O PRODUTO MAIS BARATO FOI O/A {mais_barato_nome.upper()} E CUSTOU R$ {mais_barato_preco:.2f}")