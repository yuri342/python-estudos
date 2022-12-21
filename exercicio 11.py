a = float(input("digite a altura da parede: "))
L = float(input("digite a largura da parede: "))
#a cada dois metros quadrados precisa de um litro de tinta para pintar
p = L*a
print("Sua parede tem a dimensão de {}x{} e sua area é de {}m2, vai ser necessario {}L de tinta.".format(L,a,p,p/2))