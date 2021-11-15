# Honeypot en puerto
## Objetivo
Desarrollar un sistema con un puerto abierto cuyo único fin es detectar las conexiones de agentes maliciosos y poder extraer información de los mismos.

## Ejemplo práctico

Podemos levantar el honeypot de tal manera que simule ser un servicio de postgres en el well-known-port 5432

```
python3 main.py -p 5432 -t 30
```

Y desde otra terminal, podemos simular ser atacantes probando suerte con las credenciales por defecto, de la siguiente manera:

```
psql -h localhost -U postgres -W postgres
```

Luego, en los logs de nuestro honeypot vamos a ver algo de este estilo

```
(INFO) 11-15-2021 17:55:25 - == BEGIN ==
(INFO) 11-15-2021 17:55:25 - [honeypot] Attacker's IP address: 127.0.0.1
(INFO) 11-15-2021 17:55:25 - [honeypot] Attacker sent:
(INFO) 11-15-2021 17:55:25 - b'\x00\x00\x00\x08\x04\xd2\x16/'
(INFO) 11-15-2021 17:55:26 - [Honeypot] Connection timeout reached
(INFO) 11-15-2021 17:55:26 - [Honeypot] Closed connection
(INFO) 11-15-2021 17:55:26 - == END ==
```

## Documentación para levantar el servicio
```
python3 main.py --help
```

## Conectarse al servicio
### Telnet
```
telnet <IP> <PORT>
```
`IP`: Dirección IP del servicio.  
`PORT`: Puerto el servicio esta escuchando
#### Cerrar Telnet
`Ctrl`+`¿`
```
telnet> quit
```