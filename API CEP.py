import requests
import json

cep = str(input('Digite o CEP: '))

pronto = f'https://viacep.com.br/ws/'+ cep +'/json/'
link = requests.get(pronto)
link = link.json()

rua = link['logradouro']
print(rua)

bairro = link['bairro']
print(bairro)

cidade = link['localidade']
print(cidade)

uf = link['uf']
print(uf)



