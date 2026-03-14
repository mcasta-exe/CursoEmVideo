lista =()
lista_p = ()
for c in range(1,5):
    n1 = int(input("Digite um número: "))
    lista += (n1,)
    if n1 % 2 == 0:
        lista_p += (n1,)
print(lista)
print(f"O valor 9 apareceu {lista.count(9)} vezes")
if 3 in lista:
    print(f"O primeiro valor 3 foi digitado na {lista.index(3)+1}ª posição")
else:
    print("O valor 3 não foi inserido na lista!")
print(f"O números pares foram {sorted(lista_p)}")
