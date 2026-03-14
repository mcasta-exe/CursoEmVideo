def leiadinheiro(msg):
    while True:
        resp = input(msg).strip()

        if resp == "":
            print("Nenhum valor foi informado!")
        elif resp.isalpha():
            print("Digite apenas números!")
        else:
            resp = resp.replace(',', '.')
            return float(resp)



