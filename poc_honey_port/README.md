# Honeypot en puerto
## Objetivo
Desarrollar un sistema con un puerto abierto cuyo único fin es detectar las conexiones de agentes maliciosos y poder extraer información de los mismos.

## Levantar el servicio
```
python3 main.py -a <ip>
```
`ip`: Dirección IP del servicio 

## Conectarse al servicio
```
telnet <ip> 3389
```
`ip`: Dirección IP del servicio.