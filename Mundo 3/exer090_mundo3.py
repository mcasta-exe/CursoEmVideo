dados = dict()

dados['nome'] = str(input("Digite o nome do aluno(a): "))
dados['media'] = float(input("Digite a media do aluno(a): "))

if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'

print(f"O nome do aluno(a) é {dados['nome']}")
print(f"Sua média foi {dados['media']}")
print(f"O aluno {dados['nome']} foi {dados['situação']}")
