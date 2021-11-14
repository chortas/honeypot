# Honeypot en formulario

## Objetivo
Implementar un form con campos ocultos a fin de detectar qué ips son las que llenaron dichos campos, extraer información de las mismas y luego ignorar sus requests.

## Instalar dependencias
```
pip install -r app/requirements.txt
pip install -r scrapper/requirements.txt
```

## Instalar chromedriver
```
sudo apt-get install unzip
wget -N http://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip -P ~/Downloads
unzip ~/Downloads/chromedriver_linux64.zip -d ~/Downloads
sudo mv -f ~/Downloads/chromedriver /usr/local/share/
sudo chmod +x /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
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