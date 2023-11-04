num = (int(input("Digite o primeiro numero: ")),
       int(input("Digite o segundo numero: ")),
       int(input("Digite o terceiro numero: ")),
       int(input("Digite o quarto numero: ")))
print(f"Voce digitou os valores {num}")
print(f"O valor 9 aparece {num.count(9)} vezes")

if 3 in num:
       print(f"O valor 3 apareceu na {num.index(3)+1} posição") #o +1, serve para começar a contagem no 1
else:
       print("O numeor 3 nao foi digitado em nenhuma posição.")

print(f"Os numeros pares foram ",end='')
for n in num:
       if n % 2 == 0:
              print(n, end='-')
