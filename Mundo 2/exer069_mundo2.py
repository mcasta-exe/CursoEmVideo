cont_i = 0
cont_h = 0
cont_m = 0
while True:
    print("="*30)
    print("CADASTRO DE PESSOAS")
    print("="*30)
#################### IDADE
    i = int(input("Digite sua idade: "))
    if i > 18:
        cont_i += 1
################# SEXO
    s = str(input("Digite seu sexo [M/F]: ")).upper().strip()
    if s not in "MF":
        print("SEXO INVÁLIDO")
    if s == "M":
        cont_h += 1
    if s == "F" and i < 20:
        cont_m += 1
############# CONTINUE
    p = str(input("DESEJA CONTINUAR? [S/N] ")).upper().strip()
    if p == "N":
        break

print(f"A quantidade de pessoas registradas com mais de 18 anos foi de {cont_i}")
print(f"A quantidade de HOMENS cadastrados foi de {cont_h}")
print(f"A quantidade de MULHERES abaixo de 20 anos foi de {cont_m}")