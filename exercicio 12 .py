p = float(input("digite o preço do produto;R$"))
d = 5/100 * p
print("o preço original é {}R$, mas com descontor de 5% é R${:.2f}.".format(p,p-d))