import requests
import requests as requests

datos= requests.get("http://google.es")
print(datos.cookies)