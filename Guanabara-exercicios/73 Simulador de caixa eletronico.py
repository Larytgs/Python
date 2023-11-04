print("=-"*20)
print("{:=^40}".format('\033[35m BANCO LARY \033[m'))
print("=-"*20)

valor = int(input("Que valor voce que sacar? R$"))
total = valor
ced = 50 #cedula atual
totced = 0 #total de cedulas
while True:
    if total >= ced: #se o total for maior ou igual q as cedulas
        total = total - ced
        total += 1 #qnts vezes vai tirar a cedula de R$50 do total
    else: #se n der p tirar a cedula atual..
        if totced > 0:
            print(f"Total de {totced} cedulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        totced = 0
        if total == 0:
            break
print("=-"*20)
print("\033[32mVolte Sempre ao Banco Lary! Tenha um bom dia!\033[m")
#NAO FUNCIONOU