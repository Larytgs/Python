print("MUDAR COR") #  \033[ m
print("\033[4;31;44mOla mundo!\033[m")
print("\033[7;30;41mOla mundo!\033[m")
print("\033[4;36;42mOla mundo!\033[m")

a = 8
b = 10
print("\nOs valores sao \033[31;47m{}\033[m e \033[33;44m{}\033[m!!!".format(a,b))

nome = input("\nQual o seu nome? ")
num = int(input("Qual sua idade? "))
city = str(input("Mora onde? "))
print("Prazer em te conhecer \033[31;45m{}\033[m!".format(nome))
print("Minha idade é \033[7;31;40m{}\033[m".format(num))
print("Moro em {}{}{}".format('\033[4;46m', city, '\033[m'))



