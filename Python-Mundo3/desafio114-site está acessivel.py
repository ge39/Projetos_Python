'''
    crie um código em Python que teste se o site Pudim está
    acessivel pelo computador do usado.
'''

import urllib
import urllib.request

try:
    link = 'http://foodsti.epizy.com'
    site = urllib.request.urlopen('http://foodsti.epizy.com')
except urllib.error.URLError:
    print(f'O site {link} não está acessivel no momento')
else:
    print(f'Site {link} está acessivel')
    print(site.read())
