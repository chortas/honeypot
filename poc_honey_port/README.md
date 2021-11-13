# Honeypot en puerto
## Objetivo
Desarrollar un sistema con un puerto abierto cuyo único fin es detectar las conexiones de agentes maliciosos y poder extraer información de los mismos.

## Documentación para levantar el servicio
```
python3 main.py --help
```

## Conectarse al servicio
```
telnet <IP> <PORT>
```
`IP`: Dirección IP del servicio.  
`PORT`: Puerto el servicio esta escuchando