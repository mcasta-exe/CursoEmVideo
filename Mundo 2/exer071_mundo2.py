print('='*30)
print("SAQUE DE CÉDULAS".center(30))
print('='*30)

v = int(input("QUAL O VALOR DO SAQUE? R$ "))

# RESTOS DA DIVISÃO
d50 = v % 50
d20 = d50 % 20
d10 = d20 % 10
d1 = d10 % 1

# CÉDULAS
c50 = v // 50 #CÉDULAS DE 50 REAIS
c20 = d50 // 20 #CÉDULAS DE 20 REAIS
c10 = d20 // 10 #CÉDULAS DE 10 REAIS
c1 = d10 // 1 #CÉDULAS DE 1 REAIS

print(f"TOTAL DE {c50} CÉDULAS DE 50 REAIS")
print(f"TOTAL DE {c20} CÉDULAS DE 20 REAIS")
print(f"TOTAL DE {c10} CÉDULAS DE 10 REAIS")
print(f"TOTAL DE {c1} CÉDULAS DE 1 REAL")
print('='*30)
print("FIM DA OPERAÇÃO".center(30))
print('='*30)
