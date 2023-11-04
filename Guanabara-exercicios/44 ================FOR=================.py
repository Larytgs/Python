print("Contagem de 0 a 10")
for c in range(0, 11):
    print(c)
print("FIM\n")

print("Contagem regressiva")
for c in range(10, 0, -1):
    print(c)
print("FIM\n")

print("Contagem de 0 a 10 pulando de 2 em 2")
for c in range(0, 11, 2):
    print(c)
print("FIM\n")

n = int(input("Digite quantidade de numero: "))
for c in range(0, n+1):
    print(c)
print("FIM\n")

print("Inicio Fim pulando")
i = int(input("Digite o inicio: "))
f = int(input("Digite o fim: "))
p = int(input("Digite os passos: "))
for c in range(i, f, p):
    print(c)
print("FIM\n")

print("Vai repetir a pergunta 3x")
for c in range(0, 3):
    n = int(input("Digite um numero: "))
print("FIM\n")

print("SOMATÒRIO")
s = 0
for c in range(0, 5):
    n = int(input("Digite um numero: "))
    s = s + n
print("O sormatório de todos os numeros da: {}".format(s))