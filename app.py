import requests
import pandas as pd
import time

def obtener_productos(paginas=5, productos_por_pagina=100):
    url = 'https://world.openfoodfacts.org/cgi/search.pl'
    todos_los_productos = []

    for page in range(1, paginas + 1):
        params = {
            'search_terms': '',  # sin filtro
            'search_simple': 1,
            'action': 'process',
            'json': 1,
            'page_size': productos_por_pagina,
            'page': page,
        }

        print(f'Obteniendo pagina {page}...')
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            productos = data.get('products', [])

            for p in productos:
                todos_los_productos.append({
                    'product_name': p.get('product_name', ''),
                    'brands': p.get('brands', ''),
                    'categories': p.get('categories', ''),
                    'nutriscore_grade': p.get('nutriscore_grade', ''),
                    'energy_kcal': p.get('nutriments', {}).get('energy-kcal_100g', None),
                    'fat_100g': p.get('nutriments', {}).get('fat_100g', None),
                    'sugars_100g': p.get('nutriments', {}).get('sugars_100g', None),
                    'salt_100g': p.get('nutriments', {}).get('salt_100g', None),
                })
        else:
            print(f'Error en la pagina {page}:', response.status_code)
        
        time.sleep(1)  # pausa para no sobrecargar la API

    return pd.DataFrame(todos_los_productos)

# Obtener 500 productos en total (5 paginas de 100 productos cada una)
df = obtener_productos(paginas=5, productos_por_pagina=100)

# Guardar a CSV
df.to_csv('productos.csv', index=False)
print('Archivo productos.csv guardado con', len(df), 'productos.')
