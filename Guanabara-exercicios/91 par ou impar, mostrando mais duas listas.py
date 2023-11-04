num = []
par = list()
impar = list()
while True:
    num.append(int(input("Digite um numero: ")))
    resp = str(input("Quer continuar? (S/N) ")).upper().strip()
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print("="*40)
print(f"Lista completa: {num}")
print(f"Lista PAR: {par}")
print(f"Lista IMPAR {impar}")