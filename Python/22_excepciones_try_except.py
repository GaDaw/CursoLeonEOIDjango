from libs.urlloader import load_url

from urllib.error import HTTPError

try:
    raise Exception('esto no funciona')
    print('funcionará')
except Exception as error:
    print('Ha fallado', repr(error))

try:
    load_url('https://swapi.com/api/peo')
except HTTPError as error:
    print ('Error al cargar la url', repr(error))    

except Exception as ex:
    print('Error generico', repr(ex))
