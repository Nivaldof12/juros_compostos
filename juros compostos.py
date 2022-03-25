import matplotlib.pyplot as plt

valor_inicial = int(input("Digite o seu capital inicial: R$ "))
rendimento = float(input("Digite o seu rendimento mensal, exemplo(5.4 é = 0.54): ")) / 1000
periodo = int(input("Digite o tempo que vai investir em meses: "))
aporte = int(input("Digite o aporte mensal: R$ "))
x = []
y = []

print("Valor inicial:R${}".format(valor_inicial))
print("Rendimento por período:{}%".format(rendimento * 100))
print("Total de períodos:{}".format(periodo))
print("Aporte por mês:{}".format(aporte))

for i in range(1, periodo + 1):
    montante = (valor_inicial * (1 + rendimento) ** i) + (aporte * ((1 + rendimento) ** i - 1)) / rendimento
    print("Após {} períodos, o montante será de R${:.2f}".format(i, montante))
    x.append(i)
    y.append(montante)
plt.plot(x, y)
plt.show()