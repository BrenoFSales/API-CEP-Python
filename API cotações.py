import requests as api
import json

try:
    cotacoes = api.get("https://economia.awesomeapi.com.br/last/USD-BRL,USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes = cotacoes.json()
    
    dolarValor = cotacoes['USDBRL']['bid']
    print(dolarValor)

    euroValor = cotacoes['EURBRL']['bid']
    print(euroValor)

    btcValor = float(cotacoes['BTCBRL']['bid'])
    print(f"{btcValor:.2f}")
          
except:
    print('Deu merda LEK')
