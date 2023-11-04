from time import sleep
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
maior = 0
opçao = 0
while opçao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opçao = int(input(">>>>>>Qual é a sua opçao? "))
    if opçao == 1:
        soma = num1 + num2
        print("A soma entre {} e {} da: {}".format(num1, num2, soma))
    elif opçao == 2:
        multiplicaçao = num1 * num2
        print("O resultado de {}X{} da: {}".format(num1, num2, multiplicaçao))
    elif opçao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print("Entre {} e {} o numero maior digitado foi {}".format(num1, num2, maior))
    elif opçao == 4:
        print("Informa os numeros novamente.")
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
    elif opçao == 5:
        print("FINALIZANDO...")
    else:
        print("Opção INVALIDA. Tente novamente.")
    print("=" * 30)
    sleep(2)
print("Fim do programa.")
