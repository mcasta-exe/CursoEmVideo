def notas(*valores, sit=False):
    total = len(valores)
    maior = menor = valores[0]
    for valor in valores[1:]:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    media = (sum(valores)/total)
    dados = {'total': total, 'maior': maior, 'menor':menor, 'média':media}

    if sit:
        if media >= 7:
            dados["situação"] = "boa"
        elif media >= 5:
            dados["situação"] = "razoável"
        else:
            dados["situação"] = "ruim"

    return dados


resp = notas(5, 3, 8, 9, 0, sit=True)
print(resp)