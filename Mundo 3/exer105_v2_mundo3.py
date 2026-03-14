def notas(*valores, sit=False):
    total = len(valores)
    maior = max(valores)
    menor = min(valores)
    media = (sum(valores)/total)
    dados = {
        'total': total,
        'maior': maior,
        'menor': menor,
        'media': media}

    if sit:
        if media >= 7:
            dados["situação"] = "boa"
        elif media >= 5:
            dados["situação"] = "razoável"
        else:
            dados["situação"] = "ruim"

    return dados

resp = notas(5,3,8,9,0, sit = True)
print(resp)