import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://youtube.com')
except urllib.error.URLError:
    print('O site não está acessivel no momento.')
else:
    print('Conseguiu acessar o site com sucesso!')