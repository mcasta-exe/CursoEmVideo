def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano

    if idade < 16:
        return f"Com {idade} anos, você não pode votar."
    elif 16 <= idade < 18 or idade >= 70:
        return f"Com {idade} anos, o voto é opcional."
    else:
        return f"Com {idade} anos, o voto é obrigatório."

nasc = int(input("Digite seu ano te nascimento: "))
print(voto(nasc))


