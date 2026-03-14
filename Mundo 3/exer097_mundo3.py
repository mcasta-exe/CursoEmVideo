def escreva(msg):
    tam = len(msg) + 4
    print(f"~"*tam)
    print(msg.center(tam))
    print(f"~"*tam)


escreva("TESTE DE FUNÇÕES")
escreva("TAMANHO MAIOR")
escreva("MENOR")

