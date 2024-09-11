<?php

session_start();
if (isset($_SESSION['nombre'])) {
    $nombre = $_SESSION['nombre'];
    echo "Hola, " . htmlspecialchars($nombre) . "!";

// Tiempo en segundos para contar (5 minutos = 300 segundos)
$tiempo_total = 10;
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Page Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css">
    <script src="main.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            height: 100vh;
            margin: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .container {
            text-align: center;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            position: relative;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
        .buttons {
            position: absolute;
            top: 10px;
            right: 10px;
        }
        button {
            padding: 10px 15px;
            margin-left: 10px;
            background-color: #5cb85c;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #4cae4c;
        }
    </style>
   <script type="text/javascript">
        // Inicializa el tiempo restante
        var tiempo_restante = <?php echo $tiempo_total; ?>;

        function iniciarContador() {
            var contador = setInterval(function() {
                if (tiempo_restante <= 0) {
                    clearInterval(contador);
                    document.getElementById("contador").innerHTML = "¡Tiempo terminado!";
                    // Destruir la sesión y redirigir al inicio
                    var xhr = new XMLHttpRequest();
                    xhr.open("GET", "des.php", true);
                    xhr.onreadystatechange = function () {
                        if (xhr.readyState == 4 && xhr.status == 200) {
                            window.location.href = 'index.html';
                        }
                    };
                    xhr.send();
                } else {
                    tiempo_restante--;
                    var minutos = Math.floor(tiempo_restante / 60);
                    var segundos = tiempo_restante % 60;
                    document.getElementById("contador").innerHTML = minutos + "m " + segundos + "s ";
                }
            }, 1000);
        }
    </script>
</head>
<body onload="iniciarContador()">
    <div class="container">
        <h1>Bienvenido a nuestra aplicación ADMIN</h1>
        <p>Esta es la página de inicio. Elige si deseas iniciar sesión o registrarte usando los botones de arriba.</p>
        <!-- Barra de navegación superior -->
        <div class="navbar">
            <button onclick="location.href='des.php'">Cerrar Seccion</button>
        </div>
        <div id="contador"></div>
    </div>
</body>
</html>
<?php
} else {
    echo "No hay nombre en la sesión.";
    session_destroy(); // Destruye todos los datos de la sesión
}
?>