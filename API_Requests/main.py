#%%
#imports
import requests
import json

#%%
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
ret = requests.get(url)


# %%
dolar = json.loads(ret.text)['USDBRL']

# %%
print( f" 20 dólares hoje custam {float(dolar['bid']) * 20} reais")
# %%


def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print( 
          f" {valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]} " )
# %%
cotacao(20,'USD-BRL')

        
# %%
multi_moeda(20)
# %%
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func

@error_check
def multi_moeda(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print( 
        f" {valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]} " )
        
# %%
multi_moeda(20,'USD-BRL')
multi_moeda(20,'EUR-BRL')
multi_moeda(20,'BTC-BRL')
multi_moeda(20,'RPL-BRL')
multi_moeda(20,'JPY-BRL')
# %%
import backoff
import random

@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=2)
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
          RND: {rnd}
          args: {args if args else 'sem args'}
          kargs: {kargs if kargs else 'sem kargs'}
          """)
    if rnd < .2:
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "OK!"
# %%
