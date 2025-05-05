import requests
import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import nltk
import pandas as pd 
from sklearn.decomposition import PCA

api_key = 'f76546bce033451fb83c2e807a3763ff'
url = f'https://newsapi.org/v2/everything'
params = {
    'q': 'cine',
    'language': 'es', 
    'apiKey': api_key  
}
# Hacer la solicitud GET
response = requests.get(url, params=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    articles = data.get('articles', [])
    
    # Contar el número de noticias
    num_articles = len(articles)
    print(f"Se encontraron {num_articles} noticias sobre {params['q']}.")
    
    # Opcional: Imprimir los títulos de las noticias
    for article in articles:
        print(f"- {article['title']}")
else:
    print("Error al obtener las noticias:", response.status_code)

df=pd.DataFrame(articles)
df=df['content']
df.head()
