# Taller_2

Este proyecto consiste en la extraccion de datos desde una API de noticias para su posterior analisis. Se desarrollo un script en Python que realiza una solicitud a la API, descarga un conjunto de noticias recientes y las almacena en un formato estructurado.

Los datos obtenidos incluyen informacion relevante como el titulo de la noticia, una breve descripcion, la fuente, la fecha de publicacion y un enlace a la noticia completa, pero se limito a trabajar con el contenido de la noticia, especificamente con noticias relacionadas a cine en esta oportunidad.
Posteriormente, esta informacion es utilizada en un notebook para realizar una exploracion inicial del contenido.

## Instalación
1. Clonar repositorio:
```
git clone https://github.com/arely585/Taller_2
cd Taller_2
```
2. Crear y activar entorno virtual (recomendado):
```
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```
3. Instalar dependencias:
```
pip install -r requirements.txt
Configurar API:
cp .env.example .env
# Editar .env con tu API key
```
## Uso
1. Ejecutar extracción:
```
python app.py
```
2. Analizar datos:
```
jupyter notebook notebooks/notebook_app.ipynb
```
