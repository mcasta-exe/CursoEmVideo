import random
print('=' * 30)
print("BEM VINDO AO JOGO DE PAR OU ÍMPAR!")
print('=' * 30)
cont = 0
while True:
    n = int(input("Para começar preciso que você digite um número: "))
    s = str(input("Você quer PAR ou IMPAR [P/I]? ")).upper().strip()
    machine = random.randint(0,10)
    soma = n + machine
    if s not in "PI":
        print("ENTRADA INVÁLIDA!")
        continue
    if s == "P":
        print("VOCÊ ESCOLHEU PAR! "
              "ENTÃO EU SEREI IMPAR!")
    elif s == "I":
        print("VOCÊ ESCOLHEU ÍMPAR!"
              "ENTÃO EU SEREI PAR!")
    print(f"O número que eu escolhi foi {machine}!")
    print(f"A soma de {n} e {machine} é {soma}!")
    if soma % 2 == 0:
        print("UM NÚMERO PAR!")
        if s == "P":
            print("PARABÉNS, VOCÊ GANHOU!")
            print("VAMOS DE NOVO?")
            cont += 1
        else:
            print("EU VENCI! BOA SORTE NA PRÓXIMA!")
            break
    else:
        print ("UM NÚMERO ÍMPAR!")
        if s == "I":
            print("PARABÉNS VOCÊ GANHOU!")
            print("VAMOS DE NOVO?")
            cont += 1
        else:
            print("EU VENCI! BOA SORTE NA PRÓXIMA!")
            break
print(f"\033[1:32mVOCÊ VENCEU {cont} VEZES CONSECUTIVAS!")