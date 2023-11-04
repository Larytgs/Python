lista = []
pos = 0
for c in range(0, 5):
    n = (int(input("Digite um valor: ")))
    if c == 0 or n > lista[len(lista)-1]: # n > lista[-1]
        lista.append(n) #se o numero for maior q o ultimo elemento
        print("Adicionado no final da lista.")
    else:
        while pos < len(lista):
            if n <= lista[pos]: #se o n for menor ou igual da lista
                lista.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1
print("="*30)
print(f"Os valores digitados em ordem foram {lista}")