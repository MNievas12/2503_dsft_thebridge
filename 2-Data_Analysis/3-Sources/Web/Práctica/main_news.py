import requests
import pandas as pd
import json
from utils import json_to_dict
from dotenv import dotenv_values

config = dotenv_values(".env")

url = f"http://api.mediastack.com/v1/news?access_key={config['access_key']}"

params = {'sources': 'antena3, lasextanoticias',
          'countries': 'es',
          'languages': 'es',
          'date': '2024-12-12',
          'limit': 100,
          'offset': 0}

my_news = {
            "autor": [],
            "titulo": [],
            "descripcion": [],
            "url": [],
            "fuente": [],
            "fecha_publicacion": []
            }
response = requests.get(url, params=params)
i=1
while len(my_news['autor']) < json.loads(response.content)['pagination']['total']:
    print("Nueva llamada:", i)
    if i != 1:
        response = requests.get(url, params=params)
    my_news = json_to_dict(json.loads(response.content)['data'], my_news)
    params['offset'] = params['offset'] + 100
    i = i + 1


df_news = pd.DataFrame(my_news)
df_news.to_csv('./data/news_' + params['date'] + '.csv')
print("Dataset guardado en "+ './data/news_' + params['date'] + '.csv')