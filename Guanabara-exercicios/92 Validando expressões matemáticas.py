print(f'{" VALIDANDO EXPRESSOES MATEMÀTICAS ":=^40}')
expr = str(input("Digite a expressão: "))
pilha = []
for simbolo in expr:
    if simbolo == '(':
        pilha.append('(') #cada parentese q abre, vai jogando na pilha
    elif simbolo == ')':
        if len(pilha) > 0: #se o tamanho da pilha, for maior doq 0
            pilha.pop()    #vai remover o parenteses anterior
        else:
            pilha.append(')')                                   #a cada "(" vai adicionar na pilha
            break                                               #a cada ")" vai remover da pilha
if len(pilha) == 0:
    print("Sua expressao esta válida.")                         #se n tiver ")" para fechar na pilha,na msm quantidade, vai dar erro
else:
    print("Sua expressao esta incorreta.")
