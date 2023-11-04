while True:
    num = int(input("Quer ver a tabuada de qual numero? "))
    print("=-" * 20)
    if num < 0:  # se o numero for negativo, pare
        break
    for c in range(1, 11):
        print(f"{num} X {c:2} = {num*c}")
    print("=-"*15)
print("Programa tabuada ENCERRADO. Volte Sempre!")