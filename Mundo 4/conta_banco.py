class ContaBancaria:

    def __init__(self, id, titular, saldo = 0):
        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return (f" O ID da conta é: {self.id}\n"
                f" O Titular é: {self.titular}\n"
                f" Saldo na conta: R$ {self.saldo:.2f}").replace('.', ',')

    def depositar(self, valor):
        self.saldo += valor
        print(f" Depósito de R$ {valor:.2f}".replace('.',','), end='')
        print(f" na conta {self.id}")

    def sacar(self, retirada):
        if retirada > self.saldo:
            print(f" O saque de R$ {retirada:.2f} ultrapassa o saldo na conta. SAQUE NEGADO!")
        else:
            self.saldo -= retirada
            print(f" Saque de R$ {self.saldo:.2f}".replace('.',','), end ='')
            print(f" realizado com sucesso!")


c1 = ContaBancaria(112, "Matheus")
c1.depositar(1000)
c1.sacar(10000)
print(c1)