lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
print(len(lanche))
print(sorted(lanche)) #organizado

#for comida in lanche:
#    print(f"Eu vou comer {comida}")

#for cont in range(0, len(lanche)):
#    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

print("Comi pra caramba!")