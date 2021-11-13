# Honeypot en puerto
## Objetivo
Desarrollar un sistema con un puerto abierto cuyo único fin es detectar las conexiones de agentes maliciosos y poder extraer información de los mismos.

## Levantar el servicio
```
python3 main.py -p <PORT>
```
`PORT`: Puerto donde el servicio escuchará conexiones.
El servicio se levanta en localhost o 127.0.0.1 

## Conectarse al servicio
Si el servicio esta levantado en nuestra MISMA maquina
```
telnet 127.0.0.1 <PORT>
```
O
```
telnet localhost <PORT>
```
`PORT`: Puerto donde se levanto el servicio.  
  
Si el servicio esta levantado en OTRA maquina.
```
telnet <IP> <PORT>
```
`IP`: Dirección IP del servicio.  
`PORT`: Puerto donde se levanto el servicio.  