nome = str(input("Qual é o seu nome? ")).strip().capitalize()
if nome == 'Laryssa':
    print("Que nome lindo voce tem!")
elif nome == 'Matheus' or nome == "Sara" or nome == 'Giullia':
    print("Seu nome é familiar!")
elif nome == 'Maria' or nome == 'Juliana' or nome == 'Ana' or nome == 'Vitoria':
    print("Belo nome feminino.")
elif nome == 'Gustavo' or nome == 'Joao' or nome == 'Vitor' or nome == 'Leonardo':
    print("Belo nome masculino.")
else:
    print("Seu nome é bem comum.")
print("Tenha um bom dia {}!".format(nome))