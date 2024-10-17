# Practica 3 - Unidad 1 Introduccion a la seguridad - Bases de datos seguras

## Objetivo

El objetivo de esta práctica es que el alumno conozca y aplique los conceptos de bases de datos seguras en la seguridad de la información, así como los conceptos de SQL Injection.

## Instrucciones

1. Crea una base de datos en MySQL con una BD que contenga los siguientes campos en tres tablas diferentes:

```sql
CREATE DATABASE IF NOT EXISTS `secure_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `secure_db`;

CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(45) NOT NULL,
    `password` VARCHAR(45) NOT NULL,
    `customer_id` VARCHAR(45) NOT NULL REFERENCES customers(customer_id),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `address` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `company` VARCHAR(45) NOT NULL,
    `city` VARCHAR(45) NOT NULL,
    `country` VARCHAR(45) NOT NULL,
    `phone_1` VARCHAR(45) NOT NULL,
    `phone_2` VARCHAR(45) NOT NULL,
    `customer_id` VARCHAR(45) NOT NULL REFERENCES customers(customer_id),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `customers` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `customer_id` VARCHAR(45) NOT NULL,
    `first_name` VARCHAR(45) NOT NULL,
    `last_name` VARCHAR(45) NOT NULL,
    `subscription_date` DATE NOT NULL,
    `website` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`id`))
ENGINE = InnoDB;

2. Crea un script en Python que permita insertar los datos del archivo `customers-2000000.csv`

3. Crea tres usuarios en MySQL con los siguientes permisos:
    - Usuario 1: Permisos de lectura en la tabla `customers`
    - Usuario 2: Permisos de lectura y escritura en la tabla `address`
    - Usuario 3: Permisos de lectura, escritura y eliminación en la tabla `users`

4. Crea un script en Python que permita realizar una inyección de SQL en la tabla `users` y que muestre los datos de la tabla `users` en la consola.

5. Crea un backup de la base de datos `secure_db` y restaura la base de datos en un servidor diferente.

6. Crea un documento en formato PDF que contenga la información solicitada en los puntos anteriores.

7. Investiga y describe los conceptos de SQL Injection y cómo se pueden prevenir.

8. Investiga y describe los conceptos de bases de datos seguras y cómo se pueden implementar.

## Entregables

- Documento en formato PDF que contenga la información solicitada en las instrucciones.

## Evaluación

- El documento deberá contener la información solicitada en las instrinstrucciones.
- El documento deberá tener una extensión mínima de 3 cuartillas.
- El documento deberá tener una portada con los datos del alumno y el nombre de la práctica.
- El documento deberá tener un índice con los temas investigados.
- El documento deberá tener una conclusión con los aprendizajes obtenidos.
- El documento deberá tener una bibliografía con las fuentes consultadas.
