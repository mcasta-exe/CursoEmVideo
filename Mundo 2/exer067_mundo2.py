while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    print('='*30)
    if n < 0:
        break
    print(f" {n} x 1 = {n * 1}\n"
          f" {n} x 2 = {n * 2}\n"
          f" {n} x 3 = {n * 3}\n"
          f" {n} x 4 = {n * 4}\n"
          f" {n} x 5 = {n * 5}\n"
          f" {n} x 6 = {n * 6}\n"
          f" {n} x 7 = {n * 7}\n"
          f" {n} x 8 = {n * 8}\n"
          f" {n} x 9 = {n * 9}\n"
          f" {n} x 10 = {n * 10}"
          )
    print('=' * 30)

print("Programa finalizado com sucesso!")
print('=' * 30)
