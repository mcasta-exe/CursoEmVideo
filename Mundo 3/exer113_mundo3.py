def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f"\033[1:31mErro, não é um número inteiro!\033[m")
        if ok:
            break
    return valor

def leiafloat(msg):
    while True:
        try:
            resp = str(input(msg)).strip()
            return float(resp)
        except ValueError:
            print(f"\033[1:31mErro! Entrada de dados inválida!\033[m")
        except KeyboardInterrupt:
            print(f"\033[1:31mOperação interrompida pelo usuário.\033[m")


num = leiaint(f"Digite um número inteiro: ")
num_dec = leiafloat(f"Digite um número qualquer: ")
print(f"O valor digitado foi {num} e {num_dec}")