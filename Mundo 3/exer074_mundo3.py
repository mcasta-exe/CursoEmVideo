import random
while True:
    n1 = random.randint(0,1000)
    n2 = random.randint(0,1000)
    n3 = random.randint(0,1000)
    n4 = random.randint(0,1000)
    n5 = random.randint(0,1000)
    tabela = (n1,n2,n3,n4,n5)
    break

print(f"Os números aleatórios gerados foram {tabela}")
print(f" O maior número foi {max(tabela)}")
print(f" O menor número foi {min(tabela)}")