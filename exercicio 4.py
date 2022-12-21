
P = input("Digite algo: ")
print("INFO:")
print("é apenas espaços? {}".format(P.isspace()))
print("é numerico? {}".format(P.isnumeric()))
print("é alfabetico? {}".format(P.isalpha()))
print("é apenas mauisculo? {}".format(P.isupper()))
print("é minusculo {}".format(P.islower()))
print("é capitalizado? {}".format(P.istitle()))
print("é alfanumerico? {}".format(P.isalnum()))
 
 
#outra meneira e fazer:
#print("é alfanumerico? ",P.isalnum())