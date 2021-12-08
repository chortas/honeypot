# Honeypot en formulario

Aplicacion web donde al ingreso nos encontramos con el siguiente formulario:

![image](https://user-images.githubusercontent.com/26822362/145240235-949f3bd7-b07b-4b97-8929-8a1c80f253f5.png)

Luego si se pasa la prueba se redirige al __contenido sensible__ que se encuentra en `/person`:

![image](https://user-images.githubusercontent.com/26822362/145240684-f748c03e-f39a-47e8-9354-3a16f22a3086.png)

En caso de completar los campos ocultos inspeccionando el HTML nos redirige a otra pagina `/bot`:

![image](https://user-images.githubusercontent.com/26822362/145240805-28f21778-ee54-4c66-bc70-842df180f939.png)

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
