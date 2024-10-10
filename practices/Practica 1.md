# Practica 1 - Unidad 1 Introduccion a la seguridad - CONTRASEÑAS Y CERTIFICADOS

## Objetivo

El objetivo de esta práctica es que el alumno conozca y aplique los conceptos de contraseñas y certificados digitales en la seguridad de la información.

## Instrucciones

1. Crea un programa en Python que permita al usuario ingresar una contraseña y que valide si la contraseña es segura o no. Una contraseña segura debe cumplir con los siguientes criterios basados en las [recomendaciones de Google](https://support.google.com/accounts/answer/32040?hl=es-419/#zippy=%2Chow-do-i-make-my-passwords-unique%2Chow-can-i-make-my-passwords-memorable%2Cwhat-words-should-i-avoid-in-my-passwords%2Chow-do-i-hide-written-passwords%2Chow-do-i-manage-passwords-with-a-tool):
    - Tener al menos 8 caracteres.
    - Tener al menos una letra mayúscula (A-Z).
    - Tener al menos una letra minúscula (a-z).
    - Tener al menos un número (0-9).
    - Tener al menos un carácter especial (`!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `(`, `)`, `-`, `_`, `=`, `+`, `[`, `]`, `{`, `}`, `|`, `\`, `;`, `:`, `'`, `"`, `,`, `.`, `<`, `>`, `/`, `?`, `~`, `` ` ``).
    - No debe contener espacios en blanco.
    - No debe tener más de 2 caracteres iguales consecutivos.
    - Si la contraseña cumple con los criterios, el programa deberá mostrar un mensaje indicando que la contraseña es segura, de lo contrario, deberá mostrar un mensaje indicando que la contraseña no es segura.

2. Crea un programa que me recomiende una contraseña segura. La contraseña debe cumplir con los criterios de la instrucción anterior.

3. Crea un certificado SSH, clave pública y clave privada, añade el certificado SSH a tu cuenta de GitHub y realiza un `git clone` de **un repositorio nuevo** utilizando la ruta SSH del repositorio.

4. Crea un certificado SSL autofirmado con una validez de 365 días y añádelo a un servidor web local. Realiza una petición `GET` al servidor web local utilizando `curl` y muestra el certificado SSL.

5. Investiga y describe los siguientes conceptos:
    - Contraseña
    - Certificado digital
    - Firma digital
    - Cifrado simétrico
    - Cifrado asimétrico
    - Hash
    - Encrptación

6. Investiga y describe los siguientes algoritmos de cifrado:
    - AES
    - RSA
    - SHA-256

7. Investiga y describe los siguientes estándares de cifrado:
    - SSL
    - TLS

8. Investiga y describe los siguientes protocolos de seguridad:
    - HTTPS
    - SFTP
    - SSH

## Entregables

- Documento en formato PDF que contenga la información solicitada en las instrucciones.

## Evaluación

- El documento deberá contener la información solicitada en las instrinstrucciones.
- El documento deberá tener una extensión mínima de 3 cuartillas.
- El documento deberá tener una portada con los datos del alumno y el nombre de la práctica.
- El documento deberá tener un índice con los temas investigados.
- El documento deberá tener una conclusión con los aprendizajes obtenidos.
- El documento deberá tener una bibliografía con las fuentes consultadas.
