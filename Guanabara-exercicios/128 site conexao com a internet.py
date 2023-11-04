import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim nao esta acessivel no momento.')
else:
    print('Consegui acessar osite com sucesso.')
    print(site.read()) #conteudo do HTML do site