campionato = ('Bota fogo', 'Paleiras', 'Gremio', 'Flamengo', 'Fluminense', 'Bragantino', 'Atletico-PR', 'Fortaleza', 'Atletico-MG', 'Cuiaba')
print("A lista de times do Brasileirão:",campionato)
print("="*130)
print("Os 5 primeiros são:", campionato[0:5])
print("="*130)
print("Os 4 ultimos são:", campionato[6:])
print("="*130)
print("Time em ordem alfabetica:", sorted(campionato))
print("="*130)
print(f"A Fortaleza esta na {campionato.index('Fortaleza')+1}º posição")