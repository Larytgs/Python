nome = idade = sexo = 0
tot18 = tothomem = totmulhermenos20 = 0
while True:
    print("=-" * 20)
    print("{:=^40}".format(' \033[35mCADASTRE UMA PESSOA\033[m '))
    print("=-"*10)
    nome = str(input("Qual o seu nome? ").strip())
    idade = int(input("Sua idade: "))
    sexo = ' '
    while sexo not in 'FfMm':
        sexo = str(input("Seu sexo [F/M]: ")).strip().upper()[0]
        print("=-"*10)
        if sexo == 'M':
            tothomem += 1
        if sexo in 'F' and idade < 20:
            totmulhermenos20 += 1
        if idade >= 18:
            tot18 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("\033[31mQuer contiuar? [S/N]\033[m ")).strip().upper()[0]
    if continuar == 'N':
        break
print("=-"*20)
print(f"Total de pessoas com mais de 18 anos: {tot18}.")
print(f"Ao todo temos {tothomem} homens cadastrados.")
print(f"E temos {totmulhermenos20} mulheres com menos de 20 anos.")