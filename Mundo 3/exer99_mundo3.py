from time import sleep

def maior(*num):
    cont = maior = 0
    print(f" Você digitou os valores: ", end = '')
    for valor in num:
        print(f" {valor}", end  = ' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    cont += 1
    print()
    print(f" Ao todo são {len(num)} números")
    print(f" O maior entre eles é {maior}")
    print('='*40)

maior(1,2,3,4,5,6,7,8,9)
maior(37,4,89,26,71,77)
maior(26,27,9,55,45)
maior()
