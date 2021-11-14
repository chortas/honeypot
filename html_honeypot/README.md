# Honeypot en formulario

## Objetivo
Implementar un form con campos ocultos a fin de detectar qué ips son las que llenaron dichos campos, extraer información de las mismas y luego ignorar sus requests.

## Instalar dependencias
```
pip install -r app/requirements.txt
pip install -r scrapper/requirements.txt
```

## Levantar el servicio
```
python3 app/main.py
```

## Levantar el scrapper

Es necesario tener levantado el servicio y correr:

```
python3 scrapper/main.py
```

## Acceder al formulario
```
http://0.0.0.0:5000/form
```