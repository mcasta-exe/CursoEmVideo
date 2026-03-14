import math
n = (float(input("Digite o valor do ângulo que deseja saber a função trigonométrica: ")))
sen = math.sin(math.radians(n))
co = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print (" O valor do seno é: {:.2f}".format(sen))
print (" O valor do cosseno é {:.2f}".format(co))
print (" O valor da tangente é {:.2f}".format(tan))