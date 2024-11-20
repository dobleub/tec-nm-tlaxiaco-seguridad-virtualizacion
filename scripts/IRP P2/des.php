<?php
session_start(); // Inicia la sesión
session_destroy(); // Destruye todos los datos de la sesión
header("Location: index.html"); // Redirige al usuario a la página de inicio
exit();
?>
