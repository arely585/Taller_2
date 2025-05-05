
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

#preprocesar datos
def preprocesador(text):
    text = re.sub(r'[\W]+', ' ', text.lower())
    text = re.sub(r'\d','', text)
    text = text.strip()
    return text

df=df.apply(preprocesador)
df.shape
#vectorizar en bigramas con bolsa de palabras, usando "bow_vectorizer = CountVectorizer(...)"
Stopwords_es=nltk.corpus.stopwords.words('spanish')

bow_vectorizer = CountVectorizer(ngram_range=(1,2),max_df=0.90 ,min_df=2,stop_words=Stopwords_es)

# ngram_range=(1,2) para unigramas y bigramas # cantidad minima(primera entrada) de ngramas y maxima(segunda entrada)
# max_df=0.95 para eliminar palabras que aparecen en más del 95% de los documentos
# min_df=2 para eliminar palabras que aparecen en menos de 2 documentos

bow=bow_vectorizer.fit_transform(df)

bow.shape
lexico = bow_vectorizer.get_feature_names()

pca = PCA(n_components=5)
pca = pca.fit(bow.toarray())

pca_topic_vectors = pca.transform(bow.toarray()) 
pca_topic_vectors.shape 

n_top_words = 5 
feature_names = bow_vectorizer.get_feature_names() #lexico

for component_idx, component in enumerate(pca.components_): #components = topicos
    top_features_idx = component.argsort()[:-n_top_words - 1:-1] #ordenar por importancia
    top_features = [feature_names[i] for i in top_features_idx] #obtener palabras más comunes del lexico
    print(f"Tópico {component_idx + 1}: {', '.join(top_features)}") #imprimimos el tópico y sus respectivas topwords
    