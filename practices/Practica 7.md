# Practica 7 - Creación de un laboratorio de seguridad P2

## Objetivo

Implementar un laboratorio de seguridad en VirtualBox o VMWare con las siguientes características:

- Una máquina virtual con OpnSense o pfSense configurada como firewall.

- Una máquina virtual con Kali Linux configurada como sistema de detección de intrusos.

- Una maquina virtual vulnerable por diseño como MetaSploitable2.

- Ping satisfactorio entre las máquinas virtuales.

## Desarrollo

1. Instalar VMWare o VirtualBox.

2. Instalar OpnSense o pfSense en una máquina virtual y configurar un firewall.

- Cara la instalación de OpnSense o pfSense, se recomienda seguir la documentación oficial:

  - [Instalación de OpnSense](https://docs.opnsense.org/manual/install.html)

  - [Configuración de OpnSense](https://docs.opnsense.org/manual/how-tos.html)

  - [Instalación de pfSense](https://docs.netgate.com/pfsense/en/latest/install/index.html)

  - [Configuración de pfSense](https://docs.netgate.com/pfsense/en/latest/book/index.html)

  - Para configurar el firewall, se recomienda seguir los siguientes pasos:

    - Configurar las interfaces de red.

    - Configurar las reglas de firewall.

    - Configurar el NAT.

    - Configurar el DHCP.

    - Configurar el DNS.

    - Asignar una dirección IP estática al firewall.

3. Instalar Kali Linux en una máquina virtual y configurar un sistema de detección de intrusos.

- Para la instalación de Kali Linux, se recomienda seguir la documentación oficial:

  - [Instalación de Kali Linux](https://www.kali.org/docs/installation/)

  - [Configuración de Kali Linux](https://www.kali.org/docs/)

  - Para configurar el sistema de detección de intrusos, se recomienda seguir los siguientes pasos:

    - Instalar un sistema de detección de intrusos como Snort o Suricata.

    - Configurar las reglas de detección de intrusos.

    - Configurar las alertas de detección de intrusos.

    - Asignar una dirección IP estática a Kali Linux.

4. Crear una máquina virtual vulnerable por diseño como MetaSploitable2.

- Para la instalación de MetaSploitable2, se recomienda seguir la documentación oficial:

  - [Descarga de MetaSploitable2](https://sourceforge.net/projects/metasploitable/files/Metasploitable2/)

  - [Instalación de MetaSploitable2](https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide/)

  - Para configurar MetaSploitable2, se recomienda seguir los siguientes pasos:

    - Asignar una dirección IP estática a MetaSploitable2.

5. Ping satisfactorio entre las máquinas virtuales.

- Para realizar un ping satisfactorio entre las máquinas virtuales, se recomienda seguir los siguientes pasos:

  - Configurar las interfaces de red de las máquinas virtuales.

  - Configurar las reglas de firewall para permitir el tráfico de ping.

  - Realizar un ping entre las máquinas virtuales.

## Entregable

- Documentación de la creación de un laboratorio de seguridad en VirtualBox o VMWare.
  - Documentación de la instalación y configuración de OpnSense o pfSense.
    - Capturas de pantalla de la configuración de OpnSense o pfSense.

  - Documentación de la instalación y configuración de Kali Linux.
    - Capturas de pantalla de la configuración de Kali Linux.

  - Documentación de la instalación y configuración de MetaSploitable2.
    - Capturas de pantalla de la configuración de MetaSploitable2.

## Evaluación

- La evaluación de esta práctica se realizará en base a la documentación entregada y la correcta configuración de los sistemas en el laboratorio de seguridad.

- La documentación deberá contener la información solicitada en las instrucciones.
- La documentación deberá tener una extensión mínima de 3 cuartillas.
- La documentación deberá tener una portada con los datos del alumno y el nombre de la práctica.
- La documentación deberá tener un índice con los temas investigados.
- La documentación deberá tener una conclusión con los aprendizajes obtenidos.
- La documentación deberá tener una bibliografía con las fuentes consultadas.

## Deadline

- Jueves 24 de octubre a las 23:59 hrs.
