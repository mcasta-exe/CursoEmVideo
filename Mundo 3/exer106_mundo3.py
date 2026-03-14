# Não fiz com cores

c = ('\033[m',   # 0 limpa
     '\033[31m', # 1 vermelho
     '\033[32m', # 2 verde
     '\033[34m', # 3 azul
     '\033[33m') # 4 amarelo

def ajuda_int(f_b):
    linha(f'acessando o manual do comando {fun_bib}',3)
    print(f'{c[4]}', end='')
    return help(f_b)


def linha(msg, cor = 0):
    global c
    tam = len(msg) + 2
    print(f'{c[cor]}', end='')
    print('-'*tam)
    print(f'{msg:^{tam}}')
    print('-'*tam)
    print(f'{c[0]}', end='')

while True:
    linha(f'AJUDA INTERATIVA DO PYTHON', 2)
    fun_bib = str(input('escolha uma função ou biblioteca:')).strip()
    if fun_bib == 'fim':
        break
    else:
        ajuda_int(fun_bib)
linha(f'<<<encerrado>>>', 1)