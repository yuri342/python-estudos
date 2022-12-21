from math import sqrt


n = float(input("Digite um numero: "))
print("[1]-multiplicação.")
print("[2]-divisão.")
print("[3]-Potencia.")
op = int(input("digite uma função: "))


if op == 1:
    print("multiplicação:")
    m = float(input("digite um numero: {} x ".format(n)))
    print("{} x {} = {}".format(n,m,n*m))

if op == 2:
    print("divisão:")
    d = float(input("digite um numero: {} / ".format(n)))
    print("{} / {} = {}".format(n,d,n/d))

elif op == 3:
    print("Potencia:")
    p = float(input("digite um numero: {}^".format(n)))
    print("{} ^ {} = {}".format(n,p,n**p))
