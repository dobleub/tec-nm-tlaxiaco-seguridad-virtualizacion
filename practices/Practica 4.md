# Practica 4 - Inyeccion SQL

## Objetivo

Crear una base de datos vulnerable a inyección de código y demostrar como se puede explotar esta vulnerabilidad.

## Desarrollo

1. Crear una base de datos con una tabla que contenga al menos 3 registros.

2. Crear una aplicación web que permita buscar un registro por su id, nombre o descripción.
  
  - Esta aplicación debe ser vulnerable a inyección de código, esto significa que si el usuario ingresa un valor malicioso en el campo de búsqueda, la aplicación debe mostrar información que no debería ser accesible o permitir realizar acciones que no deberían ser posibles.

  ```python
  # Ejemplo en Python con Flask y SQLite (no usar en producción)
  from flask import Flask, request
  import sqlite3

  app = Flask(__name__)

  @app.route('/')
  def index():
      return '''
      <form action="/search" method="get">
          <input type="text" name="query" placeholder="Buscar">
          <input type="submit" value="Buscar">
      </form>
      '''

  @app.route('/search')

  def search():
      query = request.args.get('query')
      conn = sqlite3.connect('database.db')
      c = conn.cursor()
      # Vulnerable a inyección de código
      c.execute(f"SELECT * FROM table WHERE id = '{query}' OR name = '{query}' OR description = '{query}'")
      # Se puede inyectar código SQL en el campo de búsqueda y obtener información no deseada
      # ejemplo: 
      #  - Buscar por id = 1 OR 1=1 -- Esto devolverá todos los registros de la tabla (lo que no queremos), ya que 1=1 siempre es verdadero y se ignorará el resto de la condición
      #  - Buscar por name = ' OR 1=1 --Esto devolverá todos los registros de la tabla (lo que no queremos), ya que 1=1 siempre es verdadero y se ignorará el resto de la condición
      # - Buscar por name = ' OR 1=1; DROP TABLE table; -- Esto eliminará la tabla (lo que no queremos), esto sucede si el usuario ingresa un valor malicioso en el campo de búsqueda y el usuario de la BD tiene permisos para eliminar tablas
      result = c.fetchall()
      conn.close()
      return str(result)
  
  if __name__ == '__main__':
      app.run()
  ```

3. Realizar pruebas de inyección de código en la aplicación web.

4. Documentar los resultados obtenidos y las posibles acciones que se pueden realizar para prevenir este tipo de vulnerabilidades.

5. Investiga y describe los siguientes conceptos:

    - Inyección de SQL
    - Blind SQL Injection
    - SQL Injection basada en errores
    - SQL Injection basada en tiempo
    - SQL Injection en procedimientos almacenados
    - SQL Injection en ORM
    - Herramientas para detectar y prevenir SQL Injection

## Entregables

- Documento en formato PDF que contenga la información solicitada en las instrucciones.

## Evaluación

- El documento deberá contener la información solicitada en las instrucciones.
- El documento deberá tener una extensión mínima de 3 cuartillas.
- El documento deberá tener una portada con los datos del alumno y el nombre de la práctica.
- El documento deberá tener un índice con los temas investigados.
- El documento deberá tener una conclusión con los aprendizajes obtenidos.
- El documento deberá tener una bibliografía con las fuentes consultadas.

## Referencias

- [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [SQL Injection Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [SQL Labs](https://portswigger.net/web-security/all-labs#sql-injection)

## Deadline

- Miercoles 02 de Octubre a las 23:59 hrs
