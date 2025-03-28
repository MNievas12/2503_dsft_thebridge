
def json_to_dict(json, news_dict):
    for noticia in json:
        news_dict['autor'].append(noticia['author'])
        news_dict['titulo'].append(noticia['title'])
        news_dict['descripcion'].append(noticia['description'])
        news_dict['url'].append(noticia['url'])
        news_dict['fuente'].append(noticia['source'])
        news_dict['fecha_publicacion'].append(noticia['published_at'])
    return news_dict