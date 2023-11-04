from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input("Nome: "))
nascimento = int(input("Ano de nascimento: "))
cadastro['idade'] = datetime.now().year - nascimento
cadastro['carteira'] = int(input("Carteira de Trabalho (0 não tem): "))
if cadastro['carteira'] != 0:
    cadastro['contrato'] = int(input("Ano de contratação: "))
    cadastro['salario'] = float(input("Salário: R$"))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contrato'] + 40) - datetime.now().year)
print("="*20)                                                               #anos de contribuição
for k, v in cadastro.items():
    print(f" -{k:.<16} tem o valor  {v}")
