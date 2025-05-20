# Taller_2

Este proyecto consiste en la extraccion de datos desde la API de Open Food Facts que incluye datos nutricionales sobre comidas. Se desarrollo un script en Python que realiza solicitudes a la API.

Los datos obtenidos incluyen informacion relevante como el nombre del producto, la marca, las categorias a las que pertenece, su calificacion de Nutri-Score y algunos valores nutricionales por cada 100 gramos, como energia (kcal), grasa, azucares y sal. Ademas, se filtro el conjunto de datos para conservar solo aquellos productos con calificacion nutricional A o B, con el plan de predecir el nutri score segun las variables entregadas.

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
