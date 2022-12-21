op = 3
nomeC = ""
senhaC = ""
while op > 2 :
  print("="*20)
  print("Sistema de log in por um aluno do DEvs(PUCrs)")
  print("[1]-criar conta.")
  print("[2]-login.")
  print("="*20)
  op = int(input("digite uma opção:"))
  print("="*20)
 #opção 1:

  if op == 1:
    print("Criar conta")
    nomeC = str(input("NOME:"))
    senhaC = str(input("SENHA:"))
    print("="*20)
    op = 3
    if senhaC == "" or nomeC == "":
       print('você não digitou a senha ou nome')
       nomeC = ""
       senhaC = ""
       op = 3
  if op == 2:
    print('login')
    LN = str(input("NOME:"))
    LS = str(input("SENHA:"))
    if nomeC == "" or senhaC == "":
      print("Essa conta não existe!")
      op = 3
    elif LN == nomeC and LS == senhaC:
      print("Nome e senha corretos bem vindo, {}!!".format(LN))
      op = 3
    else:
      print("Nome ou senha errados.")
      op = 3