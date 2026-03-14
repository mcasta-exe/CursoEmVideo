tabela = (
    "São Paulo",
    "Bahia",
    "Fluminense",
    "Athlético-PR",
    "Bragantino",
    "Palmeiras",
    "Chapecoense",
    "Mirassol",
    "Coritiba",
    "Flamengo",
    "Botafogo",
    "Corinthians",
    "Grêmio",
    "EC Vitória",
    "Atlético-MG",
    "Internacional",
    "Remo",
    "Vasco da Gama",
    "Santos",
    "Cruzeiro"
)
print("="*40)
print(f"OS 5 PRIMEIROS COLOCADOS SÃO: {tabela[:5]}")
print("="*40)
print(f"OS 4 ÚLTIMOS SÃO: {tabela[-4:]}")
print("="*40)
print(f"OS TIMES EM ORDEM ALFABÉTICA SÃO: {sorted(tabela)} ")
print("="*40)
print (f"O TIME DA CHAPECOENSE ENCONTRA-SE NA {tabela.index('Chapecoense')+1}ª POSIÇÃO")